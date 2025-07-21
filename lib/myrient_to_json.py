import requests
from bs4 import BeautifulSoup
from lib.consoles_enum import Console
import json

def parse_myrient_page(url):
    rows = []
    
    site_request = requests.get(url)
    soup = BeautifulSoup(site_request.text, 'html.parser')
    table = soup.table.tbody
    for tr in table.find_all("tr")[1:]:
        td = tr.find("td")
        title = td.a.get('title').replace(".zip", "").replace(".chd", "")
        if "[BIOS]" not in title:
            rows.append(dict(title=title, 
                            link=url + td.a.get('href'), 
                            language= "JAP" if ("Japan" in title and "(En" not in title) else "ENG" if "USA" in title or "Europe" in title or "(World)" in title or "(En" in title or "UK" in title or "Australia" in title or "United Kingdom" in title else "OTHER"))
    return rows

roms = {}    

def rom_list_for_console(console, link):
    roms[console] = parse_myrient_page(link)


def update_roms_json():
    rom_list_for_console(Console.GBA,"https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Advance/")
    rom_list_for_console(Console.NES, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headerless%29/")
    rom_list_for_console(Console.GB, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy/")
    rom_list_for_console(Console.GBC, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Color/")
    rom_list_for_console(Console.MS, "https://myrient.erista.me/files/No-Intro/Sega%20-%20Master%20System%20-%20Mark%20III/")
    rom_list_for_console(Console.MD, "https://myrient.erista.me/files/No-Intro/Sega%20-%20Mega%20Drive%20-%20Genesis/")
    rom_list_for_console(Console.S32X, "https://myrient.erista.me/files/No-Intro/Sega%20-%2032X/")
    rom_list_for_console(Console.SNES, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Super%20Nintendo%20Entertainment%20System/")
    rom_list_for_console(Console.FDS, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Family%20Computer%20Disk%20System%20%28FDS%29/")
    rom_list_for_console(Console.GG, "https://myrient.erista.me/files/No-Intro/Sega%20-%20Game%20Gear/")
    rom_list_for_console(Console.DC_CHD, "https://myrient.erista.me/files/Internet%20Archive/chadmaster/dc-chd-zstd-redump/dc-chd-zstd/")
    roms[Console.PS1_CHD] = parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_psx/CHD-PSX-USA/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_psx_eur/CHD-PSX-EUR/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_psx_jap/CHD-PSX-JAP/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_psx_jap_p2/CHD-PSX-JAP/")
    roms[Console.SAT_CHD] = parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Europe/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Japan/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/USA/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Translations/")
    roms[Console.MCD_CHD] = parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_segacd/CHD-MegaCD-NTSCJ/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_segacd/CHD-MegaCD-PAL/") + parse_myrient_page("https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_segacd/CHD-SegaCD-NTSC/")
    rom_list_for_console(Console.WS, "https://myrient.erista.me/files/No-Intro/Bandai%20-%20WonderSwan/")
    rom_list_for_console(Console.WSC, "https://myrient.erista.me/files/No-Intro/Bandai%20-%20WonderSwan%20Color/")
    rom_list_for_console(Console.LOOPY, "https://myrient.erista.me/files/No-Intro/Casio%20-%20Loopy%20%28BigEndian%29/")
    rom_list_for_console(Console.AMIGA, "https://myrient.erista.me/files/No-Intro/Commodore%20-%20Amiga/")
    rom_list_for_console(Console.FMT, "https://myrient.erista.me/files/Redump/Fujitsu%20-%20FM-Towns/")
    rom_list_for_console(Console.PS2, "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%202/")
    rom_list_for_console(Console.PSP, "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/")
    rom_list_for_console(Console.VB, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Virtual%20Boy/")
    rom_list_for_console(Console.PS1_CUE, "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/")
    rom_list_for_console(Console.SAT_CUE, "https://myrient.erista.me/files/Redump/Sega%20-%20Saturn/")
    rom_list_for_console(Console.DC_CUE, "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/")
    rom_list_for_console(Console.MCD_CUE, "https://myrient.erista.me/files/Redump/Sega%20-%20Mega%20CD%20%26%20Sega%20CD/")
    rom_list_for_console(Console.N64, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%2064%20%28BigEndian%29/")
    rom_list_for_console(Console.N64DD, "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%2064DD/")
    roms[Console.NDS] =  parse_myrient_page("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20%28Decrypted%29/") + parse_myrient_page("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Digital%29/")
    rom_list_for_console(Console.JAG, "https://myrient.erista.me/files/No-Intro/Atari%20-%20Atari%20Jaguar%20%28ROM%29/")
    rom_list_for_console(Console.LYNX, "https://myrient.erista.me/files/No-Intro/Atari%20-%20Atari%20Lynx%20%28LYX%29/")
    roms[Console.MSX] = parse_myrient_page("https://myrient.erista.me/files/No-Intro/Microsoft%20-%20MSX2/") + parse_myrient_page("https://myrient.erista.me/files/No-Intro/Microsoft%20-%20MSX/")
    rom_list_for_console(Console.PCE, "https://myrient.erista.me/files/No-Intro/NEC%20-%20PC%20Engine%20-%20TurboGrafx-16/")
    rom_list_for_console(Console.PCECD, "https://myrient.erista.me/files/Redump/NEC%20-%20PC%20Engine%20CD%20%26%20TurboGrafx%20CD/")
    rom_list_for_console(Console.PC88, "https://myrient.erista.me/files/TOSEC/NEC/PC-8801/Games/%5BD88%5D/")
    rom_list_for_console(Console.PC98, "https://myrient.erista.me/files/TOSEC/NEC/PC-9801/Games/%5BFDD%5D/")
    rom_list_for_console(Console.X68K, "https://myrient.erista.me/files/Redump/Sharp%20-%20X68000/")


    rom_list_for_console(Console.GCN, "https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/")
    rom_list_for_console(Console.XB, "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox/")
    rom_list_for_console(Console.WII, "https://myrient.erista.me/files/Redump/Nintendo%20-%20Wii%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/")
    rom_list_for_console(Console.PS3, "https://myrient.erista.me/files/No-Intro/Sony%20-%20PlayStation%203%20%28PSN%29%20%28Content%29/")
    rom_list_for_console(Console.XB360, "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox%20360/")


    with open("res/roms.json", "w", encoding='utf-8') as roms_json:
        json.dump(roms, roms_json, ensure_ascii=False)

