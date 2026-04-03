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




def parse_myabandonware_page(url):
    time.sleep(random.uniform( 0.4, 0.8)) #thanks for the IP ban I guess
    
    site_request = session.get(url)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body



    games_from_this_page = []
    games = body.find_all("div", {"class": "itemListGame"})
    for game in games:
        game_name_and_link = game.find("a", {"class": "c-item-game__name"})
        name = game_name_and_link.contents[0] 
        link = 'https://www.myabandonware.com' + game_name_and_link.get('href')
        

        games_from_this_page.append(
            dict(
                title= name,
                link = link,
                language = "ABND"
            )
        )
    return games_from_this_page
    

def rom_list_from_myabandonware(pc, link):
    roms = {}    
    site_request = requests.get(link)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body

    pagination = body.find("div", {"class": "pagination"})
    pagination_links = pagination.find_all("a")
    first_page = 1
    last_page = int(pagination_links[-1].contents[0])
    print(last_page)

    for i in range(first_page, last_page+1):
        print(i)
        if i == first_page:
            roms[pc] = parse_myabandonware_page(link + '/page/' + str(i))
        else:
            roms[pc] += parse_myabandonware_page(link + '/page/' + str(i))


    return roms


def update_myabandonware_json():


    roms_pc = rom_list_from_myabandonware(Console.PC, "https://www.myabandonware.com/browse/platform/windows")
    roms_dos = rom_list_from_myabandonware(Console.DOS, "https://www.myabandonware.com/browse/platform/dos")
    romlist = {}
    print("Updating MyAbandonware roms...")
    with open('res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        merge_unique_by_name(romlist.setdefault(Console.PC, []), roms_pc)
        merge_unique_by_name(romlist.setdefault(Console.DOS, []), roms_dos)
    
    with open('res/roms.json', 'w', encoding='utf-8') as roms_file:
        json.dump(romlist, roms_file, ensure_ascii=False)


if __name__ == "__main__":
    roms_pc = rom_list_from_myabandonware(Console.PC, "https://www.myabandonware.com/browse/platform/windows")
    roms_dos = rom_list_from_myabandonware(Console.DOS, "https://www.myabandonware.com/browse/platform/dos")
    romlist = {}
    with open('../res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        merge_unique_by_name(romlist.setdefault(Console.PC, []), roms_pc)
        merge_unique_by_name(romlist.setdefault(Console.DOS, []), roms_dos)
    
    with open('../res/roms.json', 'w', encoding='utf-8') as roms_file:
        json.dump(romlist, roms_file, ensure_ascii=False)
