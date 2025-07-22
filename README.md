# Random ROM Picker

Small program that selects and downloads a random ROM from [Myrient's Database](https://myrient.erista.me/files/). The user can select which consoles and languages the potential downloaded game can be one.

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

Once the configuration is finished, a random ROM will be picked from the list stored at `res/roms.json`. During the configuration process, said list can be updated with the latest links found on Myrient's Website.

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

You can also modify the behavior of the link crawler inside of `lib/myrient_to_json.py` function to automatically generate a JSON from a source of yours.

Finally, it is possible to modify the user configuration file at `cfg/user_config.json` by hand by setting as `true` the consoles/languages you want to keep, and `false` the rest.

```json
{
    "ENG": true,
    "JAP": true,
    "OTHER": false,
    "Nintendo Entertainment System": true,
    "Famicom Disk System": true,
    "Master System": true,
    "Game Boy": true,
    "Game Boy Color": true,
    "Game Boy Advance": true,
    "Game Gear": true,
    "Atari Lynx": false,
    "WonderSwan": false,
    "WonderSwan Color": true,
    "Mega Drive": true,
    "SegaCD (BIN/CUE)": false,
    "SegaCD (CHD)": true,
    "Sega 32X": true,
    "Super NES": false,
    "PlayStation 1 (BIN/CUE)": false,
    "PS1 (CHD)": true,
    "Sega Saturn (BIN/CUE)": false,
    "Saturn (CHD)": true,
    "Nintendo 64": true,
    "Dreamcast (BIN/CUE)": false,
    "Dreamcast (CHD)": true,
    "PlayStation 2": true,
    "PlayStation Portable": true,
    "Nintendo DS": true,
    "Nintendo Gamecube": true,
    "Microsoft Xbox": true,
    "Nintendo Wii": true,
    "PlayStation 3": true,
    "Microsoft Xbox 360": true,
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
    "MAME": true
}
```

## TODO

- [ ] Add support for MAME and Final Burn NEO ROMs, which will require checking a ROM's dependancy with system files, and other ROMs (common with a game's upgraded/localized version).
- [ ] Potentially auto-download emulators and BIOS files.
