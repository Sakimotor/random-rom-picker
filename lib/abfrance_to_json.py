import requests
from bs4 import BeautifulSoup
from lib.consoles_enum import Console
import json

import time
import random

from lib.handle_dupes import merge_unique_by_name

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
session.headers.update(headers)




def parse_abfrance_page(url):
    #time.sleep(random.uniform(1, 3)) #thanks for the IP ban I guess
    
    site_request = session.get(url)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body



    games_from_this_page = []
    games = body.find_all("div", {"class": "tab_jeu_1"})
    for game in games:
        game_name_and_link = game.find("a")
        name = game_name_and_link.contents[0] 
        link = 'https://www.abandonware-france.org/ltf_abandon/' + game_name_and_link.get('href')
        

        games_from_this_page.append(
            dict(
                title= name,
                link = link,
                language = "ABND"
            )
        )
    
    return games_from_this_page
    

def rom_list_from_abfrance(pc, url):
    roms = {}    
    site_request = requests.get(url)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body

    pagination = body.find("div", {"id": "lettres_search"})
    links = pagination.find_all("a")[1:-1]
    first = True
    for link in links:
        if first:
            roms[pc] = parse_abfrance_page(url + link.get('href'))
            first = False
            continue
        roms[pc] += parse_abfrance_page(url + link.get('href'))
        

    return roms


def update_abfrance_json():
    print("Updating Abandonware-France roms...")

    roms_pc = rom_list_from_abfrance(Console.PC, "https://www.abandonware-france.org/ltf_abandon/ltf_listes_jeux.php")
    romlist = {}
    with open('res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        merge_unique_by_name(romlist.setdefault(Console.PC, []), roms_pc)
    
    with open('res/roms.json', 'w', encoding='utf-8') as roms_file:
        json.dump(romlist, roms_file, ensure_ascii=False)



