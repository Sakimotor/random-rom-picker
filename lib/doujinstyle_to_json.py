import requests
from bs4 import BeautifulSoup
from lib.consoles_enum import Console
import json
from lib.handle_dupes import merge_unique_by_name

import time
import random

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
session.headers.update(headers)




def parse_doujinstyle_page(url):
    time.sleep(random.uniform(0.2, 0.8)) #thanks for the IP ban I guess
    site_request = session.get(url)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body

    games_from_this_page = []
    games = body.find_all("span", {"class": "s1"})
    games = games[1:]
    for game in games:
        
        game_name = game.find("a")
        name = game_name.contents[0]
        link = 'https://doujinstyle.com' + game_name.get('href')[1:]
        games_from_this_page.append(
            dict(
                title= name,
                link = link,
                language = "DOUJIN"
            )
        )
    return games_from_this_page
    

def rom_list_from_doujinstyle(pc, link):
    print("Updating DoujinStyle roms...")

    roms = {}

    #trying to follow the usual flow: loading main page, changing layout to video games, then to list
    session.get(link)

    data = {
    "source": "2",
    "target": "home",
    "page": "0",
    "layout": "2",
    "change_display": ""
    }
    session.post(link, data=data)

    data = {
    "source": "1",
    "target": "home",
    "page": "0",
    "layout": "1",
    "change_display": ""
    }
    session.post(link, data=data)

    site_request = session.get(link)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    body = soup.body


    last_page_tag = body.find("a", title="Oldest")
    href = last_page_tag.get("href")
    first_page = 0
    last_page = int(href.split("page=")[-1])
    print(f"page count: {last_page}")

    for i in range(first_page, last_page+1):
        if i == first_page:
            roms[pc] = parse_doujinstyle_page(link + '&page=' + str(i))
        else:
            roms[pc] += parse_doujinstyle_page(link + '&page=' + str(i))


    return roms


def update_doujinstyle_json():


    roms_pc = rom_list_from_doujinstyle(Console.PC, "https://doujinstyle.com/?p=home")
    romlist = {}
    with open('res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        merge_unique_by_name(romlist.setdefault(Console.PC, []), roms_pc)
    
    with open('res/roms.json', 'w', encoding='utf-8') as roms_file:
        json.dump(romlist, roms_file, ensure_ascii=False)


if __name__ == "__main__":
    roms_pc = rom_list_from_doujinstyle(Console.PC, "https://doujinstyle.com/?p=home")
    romlist = {}
    with open('../res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        merge_unique_by_name(romlist.setdefault(Console.PC, []), roms_pc)
    
    with open('../res/roms.json', 'w', encoding='utf-8') as roms_file:
        json.dump(romlist, roms_file, ensure_ascii=False)
