# Random ROM Picker

Small program that selects and downloads a random ROM from [Myrient's Database](https://myrient.erista.me/files/). The user can select which consoles and languages the potential downloaded game can be one.

## Requirements

You will need to have [Python 3](https://www.python.org/downloads/) installed, as well as the following modules:

- tqdm
- Werkzeug
- requests
- beautifulsoup4

You can automatically install said modules by running `pip install -r requirements.txt` after cloning this repository.

## Usage

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
            ]
}
```

You can also modify the behavior of the link crawler inside of `lib/myrient_to_json.py` function to automatically generate a JSON from a source of yours.

## TODO

- Add support for MAME and Final Burn NEO ROMs, which will require checking a ROM's dependancy with system files, and other ROMs (common with a game's upgraded/localized version).
