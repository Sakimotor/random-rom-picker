# Random ROM Picker

Small program that selects and downloads a random ROM from [minerva's Database](https://minerva.erista.me/files/). The user can select which consoles and languages the potential downloaded game can be one. **TODO**: rewrite it to auto-download the torrents.

Supported websites:

- Minerva
- MyAbandonware
- Final Burn NEO
- Abandonware-France
- DoujinStyle

Can also (and mostly) serve as a mere game picker (without any download). 

**Note:** for Final Burn NEO titles, the romset is taken from [lofi1048's FightCade 2 JSON Pack](https://lofi.netlify.app/post/fc2-json-pack-auto-download-roms-from-fightcade-2/)

## Requirements

You will need to have [Python 3](https://www.python.org/downloads/) installed, as well as the following modules:

- tqdm
- Werkzeug
- requests
- beautifulsoup4

You can automatically install said modules by running `pip install -r requirements.txt` after cloning this repository.

## Usage

After cloning/downloading the repo, you can run the program with the command `python rom_picker.py`.

When launching the program, you will be asked if you want to reconfigure your settings (add/remove potential languages/consoles), which would automatically modify the configuration file located at `cfg/user_config.json` through a series of questions.

Once the configuration is finished, a random ROM will be picked from the list stored at `res/roms.json`. During the configuration process, said list can be updated with the latest links found on minerva's Website.

## Extra

It is possible to provide the program with your own custom ROM list, as long as you follow the current file scheme to make your own `res/roms.json`:

```json
{"Console": [
    {"title": "Game (USA)", "link": "https://example.com/Game.zip", "language": "ENG"},
    {"title": "Game 2 (Japan)", "link": "https://example.com/Game2.zip", "language": "JAP"},
    ...
    {"title": "Game X (Germany)", "link": "https://example.com/GameX.zip", "language": "OTHER"}
            ],
 ...
 "Console Y": [
    ...
 ]
}
```

You can also modify the behavior of the link crawler inside of `lib/minerva_to_json.py` function to automatically generate a JSON from a source of yours.

Finally, it is possible to modify the user configuration file at `cfg/user_config.json` by hand by setting as `true` the consoles/languages you want to keep, and `false` the rest.

```json
{
    "languages": {
        "ENG": true,
        "JAP": true,
        "OTHER": false,
        "ABND": true
    },
    "consoles": {
        "Nintendo Entertainment System": true,
        "Famicom Disk System": true,
        "Master System": true,
        "Game Boy": true,
        "Game Boy Color": true,
        "Game Boy Advance": true,
        "Game Gear": true,
        "Atari Lynx": true,
        "WonderSwan": true,
        "WonderSwan Color": true,
        "Mega Drive": true,
        "SegaCD (CUE)": true,
        "SegaCD (CHD)": false,
        "Sega 32X": true,
        "Super NES": true,
        "PlayStation 1 (CUE)": true,
        "PS1 (CHD)": false,
        "Sega Saturn (CUE)": true,
        "Saturn (CHD)": false,
        "Nintendo 64": true,
        "Nintendo 64DD": true,
        "Dreamcast (CUE)": true,
        "Dreamcast (CHD)": false,
        "PlayStation 2": true,
        "PlayStation Portable": true,
        "Nintendo DS": true,
        "Nintendo Gamecube": true,
        "Microsoft Xbox": true,
        "Nintendo Wii": true,
        "PlayStation 3": false,
        "Microsoft Xbox 360": false,
        "PC-Engine": true,
        "PC-Engine CD": true,
        "Virtual Boy": true,
        "Casio Loopy": true,
        "Atari Jaguar": true,
        "MSX": true,
        "PC-88": true,
        "PC-98": true,
        "Sharp X68000": true,
        "Commodore Amiga": true,
        "FMTowns": true,
        "Final Burn NEO": true,
        "PC Abandonware": true
    }
}
```

## TODO

- [X] Add support for Final Burn NEO ROMs, which will require checking a ROM's dependancy with system files, and other ROMs (common with a game's upgraded/localized version).
- [ ] Potentially auto-download emulators and BIOS files.
