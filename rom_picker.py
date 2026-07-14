from lib.consoles_enum import Console
import json
import random
import os
import requests
import werkzeug
import argparse
from lib.minerva_to_json import update_roms_json
from lib.myabandonware_to_json import update_myabandonware_json
from lib.abfrance_to_json import update_abfrance_json
from lib.doujinstyle_to_json import update_doujinstyle_json
from tqdm import tqdm

#from https://gist.github.com/phineas-pta/d73f9a035b05f8e923af8c01df057175
console_list = list(Console)


def create_roms_folder():
    for console in console_list:
        if not os.path.exists('roms/' + console):
            os.makedirs('roms/' + console)




def configure_program():
    if not os.path.exists("cfg"):
        os.mkdir("cfg")
    lang_choices = {}
    console_choices = {}
    all_choices = {}
        
    use_chd = input("Do you want to use CHDs when possible ? (Y/N)")
    lang_choices["ENG"]  = ("y" == input("Do you allow english games ? (Y/N)").lower() )
    lang_choices["JAP"]  = ("y" == input("Do you allow japanese games ? (Y/N)").lower() )
    lang_choices["OTHER"]  = ("y" == input("Do you allow games in other languages ? (Y/N)").lower() )
    lang_choices["ABND"] = True
    lang_choices["DOUJIN"] = True
    all_choices["languages"] = lang_choices
    i = 0
    for console in console_list:
        if ("CHD" in console and use_chd.lower() == "n") or ("CUE" in console and use_chd.lower() == "y"):
            console_choices[console] = False
            i += 1
            continue
        console_choices[console] = input(f"Add the {console} to the pool ? (Y/N)").lower() == "y"           
        i += 1
    all_choices["consoles"] = console_choices
    with open("cfg/user_config.json", "w", encoding='utf-8') as json_file:
        json.dump(all_choices, json_file, ensure_ascii=False, indent=4)
    
    
    
def pick_random_game(console:Console=None):
    game_found = False
    console_cur = console
    with open('res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        with open('cfg/user_config.json', 'r', encoding='utf-8') as config_file:
            pool_cur = json.load(config_file)
            languages_cur = pool_cur["languages"]
            if console_cur is None:
                pool_cur = pool_cur["consoles"]            
                pool_filtered = {k: v for k, v in pool_cur.items() if v} #we filter out the consoles that are set to False
                console_cur = random.choice(list(pool_filtered.keys())) #we need to transform the dict into a list for it to work with random.choice()
                languages_filtered = {k: v for k, v in languages_cur.items() if v}

                
            
            if console_cur == Console.FB:
                with open('res/fbneo_roms.json', 'r', encoding='utf-8') as fbneo_file:
                    romlist_fbneo = json.load(fbneo_file)
                    pick_current = random.choice(list(romlist_fbneo.keys()))
                    game_current = romlist_fbneo[pick_current]
                    result = dict(title=pick_current, reqs=game_current['require'] if 'require' in game_current else None, link=game_current['download'])
            
            else:
                result = random.choice(romlist[console_cur])
                if console is None:
                    while result["language"] not in languages_filtered:
                        result = random.choice(romlist[console_cur])                   
                    
            
            result['console'] = console_cur
            return result
                  
            
                

def main():
    parser = argparse.ArgumentParser(
                    prog='ROM/Game Picker',
                    description='Picks a random game')
    
    parser.add_argument('-noconf', '--no-config', nargs='*')

    args = parser.parse_args()
    res = None




    if os.path.exists("cfg/user_config.json"):
        if args.no_config is None:
            reconfig = input("Run the configurator again ? (Y/N)")
            if reconfig.lower() == "y":
                configure_program()
    else:
        configure_program()
    
    if args.no_config is None:
        sources = [
            ("Minerva", update_roms_json),
            ("MyAbandonware", update_myabandonware_json),
            ("AB-France", update_abfrance_json),
            ("Doujinstyle", update_doujinstyle_json),
        ]

        for name, func in sources:
            if input(f"Update {name} list? (Y/N): ").strip().lower() == "y":
                func()

    
        if "y" in (input("Pick one specific console ? (Y/N)").lower()):
            picked_console = None
            i = 1
            for console in console_list:
                print(f"{i} - {console}")
                i += 1
            console_input = int(input("Enter the number of the console you want to play:"))
            if console_input > len(console_list) or console_input < 1:
                picked_console = None
            else:
                picked_console = console_list[console_input - 1]
            res = pick_random_game(picked_console)
            
        else:
            res = pick_random_game()
    else:
        res = pick_random_game()
    print(f"Today's ROM will be {res['title']} on the {res['console']}!")
    print(res['link'])
    


if __name__ == "__main__":
    main()