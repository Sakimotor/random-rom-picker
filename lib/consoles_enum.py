from enum import auto
from enum import StrEnum

class Console(StrEnum):
    NES = 'Nintendo Entertainment System'
    FDS = 'Famicom Disk System'
    MS = 'Master System'
    GB = 'Game Boy'
    GBC = 'Game Boy Color'
    GBA = 'Game Boy Advance'
    GG = 'Game Gear'
    LYNX = 'Atari Lynx'
    WS = 'WonderSwan'
    WSC = 'WonderSwan Color'
    

    
    MD = 'Mega Drive'
    MCD_CUE = 'SegaCD (BIN/CUE)'
    MCD_CHD = 'SegaCD (CHD)'
    S32X = 'Sega 32X'
    SNES = 'Super NES'
    
    PS1_CUE = 'PlayStation 1 (BIN/CUE)'
    PS1_CHD = 'PS1 (CHD)'
    SAT_CUE = 'Sega Saturn (BIN/CUE)'
    SAT_CHD = 'Saturn (CHD)'
    N64 = 'Nintendo 64'
    N64DD = 'Nintendo 64DD'
    DC_CUE = 'Dreamcast (BIN/CUE)'
    DC_CHD = 'Dreamcast (CHD)'
    
    
    
    PS2 = 'PlayStation 2'
    PSP = 'PlayStation Portable'

    NDS = 'Nintendo DS'
    
    GCN = 'Nintendo Gamecube'
    XB = 'Microsoft Xbox'
    WII = 'Nintendo Wii'
    PS3 = 'PlayStation 3'
    XB360 = 'Microsoft Xbox 360'

    PCE = 'PC-Engine'
    PCECD = 'PC-Engine CD'
    VB = 'Virtual Boy'
    LOOPY = 'Casio Loopy'
    JAG = 'Atari Jaguar'

    MSX = 'MSX'
    
    
    PC88 = 'PC-88'
    PC98 = 'PC-98'
    X68K = 'Sharp X68000'  
    AMIGA = 'Commodore Amiga'
    FMT = 'FMTowns'  
    
    FB = 'Final Burn NEO'
    MAME = 'MAME'