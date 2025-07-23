from lib.consoles_enum import Console
import json
import random
import os
import requests
import werkzeug
from lib.myrient_to_json import update_roms_json
from tqdm import tqdm

#from https://gist.github.com/phineas-pta/d73f9a035b05f8e923af8c01df057175
def download(url:str, filename:str="", overwrite:bool=False, chunk_size:int=1) -> None:
    """
    try auto detect file name if left empty
    option to overwrite if file already existed
    chunk_size in MBytes
    """
    HEADERS = {"User-Agent": "my gist code"}  # some sites block if u dont have at least user agent
    with requests.get(url, headers=HEADERS, stream=True) as resp:

        # get file name
        if filename == "":
            MISSING_FILENAME = "missing_name"
            if content_disposition := resp.headers.get("Content-Disposition"):
                param, options = werkzeug.http.parse_options_header(content_disposition)
                if param == "attachment":
                    filename = options.get("filename", MISSING_FILENAME)
                else:
                    filename = MISSING_FILENAME
            else:
                filename = os.path.basename(url)
                fileext = os.path.splitext(filename)[-1]
                if fileext == "":
                    filename = MISSING_FILENAME

        # download file
        if overwrite or not os.path.exists(filename):
            TOTAL_SIZE = int(resp.headers.get("Content-Length", 0))
            CHUNK_SIZE = chunk_size * 10**6
            with (
                open(filename, mode="wb") as file,
                tqdm(total=TOTAL_SIZE, desc=f"download {filename}", unit="B", unit_scale=True) as bar
            ):
                for data in resp.iter_content(chunk_size=CHUNK_SIZE):
                    size = file.write(data)
                    bar.update(size)

console_list = list(Console)


def create_roms_folder():
    for console in console_list:
        if not os.path.exists('roms/' + console):
            os.makedirs('roms/' + console)




def configure_program():
    os.mkdir("cfg")
    choices = {}
    if "y" == input("Do you want to update the roms list ? (Y/N)").lower():
        update_roms_json()
        
    use_chd = input("Do you want to use CHDs when possible ? (Y/N)")
    choices["ENG"]  = ("y" == input("Do you allow english games ? (Y/N)").lower() )
    choices["JAP"]  = ("y" == input("Do you allow japanese games ? (Y/N)").lower() )
    choices["OTHER"]  = ("y" == input("Do you allow games in other languages ? (Y/N)").lower() )
    i = 0
    for console in console_list:
        if ("CHD" in console and use_chd.lower() == "n") or ("CUE" in console and use_chd.lower() == "y"):
            choices[console] = False
            i += 1
            continue
        if input(f"Add the {console} to the pool ? (Y/N)").lower() == "y":
            choices[console] = True
                    
        i += 1
    
    with open("cfg/user_config.json", "w", encoding='utf-8') as json_file:
        json.dump(choices, json_file, ensure_ascii=False, indent=4)
    
    
    
def pick_random_game():
    game_found = False
    with open('res/roms.json', 'r', encoding='utf-8') as roms_file:
        romlist = json.load(roms_file)
        with open('cfg/user_config.json', 'r', encoding='utf-8') as config_file:
            pool_cur = json.load(config_file)
            pool_filtered = {k: v for k, v in pool_cur.items() if v} #we filter out the consoles that are set to False
            random_console = random.choice(list(pool_filtered.keys())) #we need to transform the dict into a list for it to work with random.choice()
            if random_console == Console.FB:
                with open('res/fbneo_roms.json', 'r', encoding='utf-8') as fbneo_file:
                    romlist_fbneo = json.load(fbneo_file)
                    pick_current = random.choice(list(romlist_fbneo.keys()))
                    game_current = romlist_fbneo[pick_current]
                    result = dict(title=pick_current, reqs=game_current['require'] if 'require' in game_current else None, link=game_current['download'])
            else:
                result = random.choice(romlist[random_console])
            result['console'] = random_console
            return result
            

def download_fbrom_and_reqs(res, romlist_fbneo):
    print(f"res: {res}")
    reqs_cur = res['reqs']
    if reqs_cur is not None:
        for req_title in reqs_cur:
            req_cur = romlist_fbneo[req_title]
            print(f"req: {req_cur}")
            res_next = dict(title=req_title, reqs= (req_cur['require'] if 'require' in req_cur  else None), link=req_cur['download'])
            download_fbrom_and_reqs(res_next, romlist_fbneo)
    download(res['link'], 'roms/' + Console.FB + '/' + res['title'] + '.zip')       
            
                

def main():
    if os.path.exists("cfg/user_config.json"):
        reconfig = input("Run the configurator again ? (Y/N)")
        if reconfig.lower() == "y":
            configure_program()
    else:
        configure_program()
    
    res = pick_random_game()
    print(f"Today's ROM will be {res['title']} on the {res['console']}!")
    if not os.path.exists('roms/' + res['console']):
        os.makedirs('roms/' + res['console'])
    if res['console'] == Console.FB:
        with open('res/fbneo_roms.json', 'r', encoding='utf-8') as fbneo_file:
            romlist_fbneo = json.load(fbneo_file)
            download_fbrom_and_reqs(res, romlist_fbneo)
                
    else:
        download(res['link'],'roms/' + res['console'] + '/' + res['title'] + ('.chd' if "CHD" in res['console'] else '.zip'))
    


if __name__ == "__main__":
    main()