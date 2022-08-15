#!/usr/bin/env python
# Display a runtext with double-buffering.
from ast import If
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json
from PIL import Image

userFile = open("/home/pi/rpi-rgb-led-matrix/user.json")


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t",
            "--text",
            help="The text to scroll on the RGB LED panel",
            default="Hello world!",
        )

    def run(self):
        userJSON = json.load(userFile)
        teamLogos = {
            "MLB": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "NFL": Image.open(
                requests.get(
                    "https://pixy.org/src/147/thumbs350/1471745.jpg", stream=True
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Yankees": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Nationals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Texas Rangers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Mets": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Marlins": Image.open(
                requests.get(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgLvfw0fwbJoD01YsU124hsHEx7yjgD6sKBk4-cTdhQg&s",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oakland Athletics": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas City Royals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Toronto Blue Jays": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Milwaukee Brewers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Boston Red Sox": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Guardians": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Reds": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Francisco Giants": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Colorado Rockies": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Twins": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Dodgers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Braves": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seattle Mariners": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Angels": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Tigers": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2016/04/Detroit_Tigers_Insignia_logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Diamondbacks": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia Phillies": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Diego Padres": Image.open(
                requests.get(
                    "https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pittsburgh Pirates": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tampa Bay Rays": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Baltimore Orioles": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago White Sox": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "St. Louis Cardinals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Cubs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Astros": Image.open(
                requests.get(
                    "https://images.ctfassets.net/iiozhi00a8lc/t117_favicon117_qgouernt_ehw9pj78_png/700d0ebafa92b5499f3dc09bf465fc98/t117_favicon.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Cardinals": Image.open(
                requests.get(
                    "https://seeklogo.com/images/A/arizona-cardinals-logo-60AFACA5B9-seeklogo.com.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Falcons": Image.open(
                requests.get(
                    "https://cdn.freebiesupply.com/images/large/2x/atlanta-falcons-logo-on-black.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Baltimore Ravens": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b09.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Buffalo Bills": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/03/Buffalo_Bills_logo_blue-700x502.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Carolina Panthers": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/02/Carolina_Panthers_logo_blue-700x380.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Bears": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b16.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Bengals": Image.open(
                requests.get(
                    "https://cdn.freebiesupply.com/images/thumbs/1x/cincinnati-bengals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Browns": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/03/Cleveland_Browns_logo_b-700x432.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Jacksonville Jaguars": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b2f.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Las Vegas Raiders": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-oakland-raiders-team-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Dallas Cowboys": Image.open(
                requests.get(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/1076px-Dallas_Cowboys.svg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Denver Broncos": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b21.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Lions": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-detroit-lions-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Green Bay Packers": Image.open(
                requests.get(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Green_Bay_Packers_logo.svg/1280px-Green_Bay_Packers_logo.svg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Texans": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b29.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indianapolis Colts": Image.open(
                requests.get(
                    "https://cdn.freebiesupply.com/images/large/2x/indianapolis-colts-logo-transparent.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Chargers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-los-angeles-chargers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Rams": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/los-angeles-rams-2020-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Dolphins": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/02/Miami_Dolphins_logo_bright-609x700.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Vikings": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-minnesota-vikings-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas City Chiefs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-kansas-city-chiefs-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New England Patriots": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-england-patriots-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New Orleans Saints": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-orleans-saints-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Giants": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-york-giants-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Jets": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-york-jets-team-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia Eagles": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-philadelphia-eagles-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pittsburgh Steelers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-pittsburgh-steelers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Francisco 49ers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seattle Seahawks": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-seattle-seahawks-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tampa Bay Buccaneers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/tampa-bay-buccaneers-2020-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tennessee Titans": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-tennessee-titans-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Commanders": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/washington-commanders-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # "Pittsburgh Panthers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/221.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "West Virginia Mountaineers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/277.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oklahoma State Cowboys": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/197.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Central Michigan Chippewas": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2117.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Kansas Jayhawks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tennessee Tech Golden Eagles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2635.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Colorado Buffaloes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/38.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "TCU Horned Frogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2628.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Iowa State Cyclones": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/66.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Southeast Missouri State Redhawks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2546.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oklahoma Sooners": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/201.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UTEP Miners": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2638.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Kansas State Wildcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2306.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "South Dakota Coyotes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/233.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Baylor Bears": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/239.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Albany Great Danes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/399.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Texas Tech Red Raiders": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2641.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Murray State Racers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/93.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Texas Longhorns": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/251.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UL Monroe Warhawks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2433.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Hawai'i Rainbow Warriors": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/62.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Vanderbilt Commodores": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/238.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tennessee Volunteers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2633.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Ball State Cardinals": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2050.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Missouri Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/142.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Louisiana Tech Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2348.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Texas A&M Aggies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/245.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Sam Houston Bearkats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2534.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arkansas Razorbacks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/8.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cincinnati Bearcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2132.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Georgia Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/61.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oregon Ducks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2483.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Ole Miss Rebels": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/145.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Troy Trojans": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2653.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Auburn Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Mercer Bears": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2382.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida Gators": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/57.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Utah Utes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/254.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Kentucky Wildcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/96.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Miami (OH) RedHawks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/193.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Vanderbilt Commodores": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/238.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Elon Phoenix": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2210.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Alabama Crimson Tide": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/333.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Utah State Aggies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/328.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Mississippi State Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/344.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Memphis Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/235.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "South Carolina Gamecocks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2579.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Georgia State Panthers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2247.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "LSU Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/99.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida State Seminoles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/52.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arizona State Sun Devils": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/9.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Northern Arizona Lumberjacks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2464.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Colorado Buffaloes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/38.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "TCU Horned Frogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2628.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UCLA Bruins": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/26.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Bowling Green Falcons": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/189.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Georgia Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/61.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oregon Ducks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2483.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "San Diego State Aztecs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/21.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arizona Wildcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/12.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "California Golden Bears": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/25.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UC Davis Aggies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/302.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "USC Trojans": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/30.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Rice Owls": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/242.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida Gators": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/57.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Utah Utes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/254.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Stanford Cardinal": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/24.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Colgate Raiders": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2142.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Washington State Cougars": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/265.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Idaho Vandals": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/70.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oregon State Beavers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/204.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Boise State Broncos": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/68.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Washington Huskies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/264.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Kent State Golden Flashes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2309.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida State Seminoles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/52.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Duquesne Dukes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2184.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "North Carolina Tar Heels": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/153.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida A&M Rattlers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/50.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Pittsburgh Panthers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/221.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "West Virginia Mountaineers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/277.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Wake Forest Demon Deacons": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/154.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "VMI Keydets": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2678.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Old Dominion Monarchs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/295.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Virginia Tech Hokies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/259.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Duke Blue Devils": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Temple Owls": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/218.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Boston College Eagles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/103.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Rutgers Scarlet Knights": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/164.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Appalachian State Mountaineers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2026.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "North Carolina Tar Heels": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/153.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "East Carolina Pirates": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/151.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "NC State Wolfpack": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/152.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Virginia Cavaliers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/258.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Richmond Spiders": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/257.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Miami Hurricanes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2390.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Bethune-Cookman Wildcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2065.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Syracuse Orange": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/183.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Louisville Cardinals": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/97.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "LSU Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/99.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Florida State Seminoles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/52.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Georgia Tech Yellow Jackets": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/59.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Clemson Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/228.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UCF Knights": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2116.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "South Carolina State Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2569.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Duke Blue Devils": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/150.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Temple Owls": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/218.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "East Carolina Pirates": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/151.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "NC State Wolfpack": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/152.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Navy Midshipmen": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2426.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Delaware Blue Hens": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/48.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arkansas Razorbacks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/8.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cincinnati Bearcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2132.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Wyoming Cowboys": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2751.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tulsa Golden Hurricane": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/202.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UTSA Roadrunners": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2636.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Houston Cougars": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/248.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "South Florida Bulls": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/58.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "BYU Cougars": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/252.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tulane Green Wave": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2655.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "UMass Minutemen": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/113.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Mississippi State Bulldogs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/344.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Memphis Tigers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/235.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "North Texas Mean Green": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/249.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "SMU Mustangs": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2567.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Northwestern Wildcats": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/77.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Nebraska Cornhuskers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/158.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Illinois Fighting Illini": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/356.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Wyoming Cowboys": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2751.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Purdue Boilermakers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2509.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Penn State Nittany Lions": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/213.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Minnesota Golden Gophers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/135.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "New Mexico State Aggies": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/166.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Michigan State Spartans": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/127.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Western Michigan Broncos": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2711.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Indiana Hoosiers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/84.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Illinois Fighting Illini": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/356.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Iowa Hawkeyes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2294.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "South Dakota State Jackrabbits": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2571.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Maryland Terrapins": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/120.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Buffalo Bulls": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2084.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Michigan Wolverines": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/130.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Colorado State Rams": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/36.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Boston College Eagles": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/103.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Rutgers Scarlet Knights": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/164.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Nebraska Cornhuskers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/158.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "North Dakota Fighting Hawks": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/155.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Wisconsin Badgers": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/275.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Illinois State Redbirds": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/2287.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Ohio State Buckeyes": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/194.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Notre Dame Fighting Irish": Image.open(
            #     requests.get(
            #         "https://a.espncdn.com/i/teamlogos/ncaa/500/87.png", stream=True
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
        }
        while True:
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            white = graphics.Color(255, 255, 255)
            bFont = graphics.Font()
            bFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/8x13.bdf")
            font = graphics.Font()
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
            smallestFont = graphics.Font()
            smallestFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")
            alilbiggerFont = graphics.Font()
            alilbiggerFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x7.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            print("getting responseArrrrrrrrr")
            user = userJSON["user"]
            url = requests.get(
                f"https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/{user}"
            )
            responseArr = json.loads(url.text)
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            print(offscreen_canvas)
            pos = offscreen_canvas.width
            color = green
            print(responseArr)
            for arr in responseArr:
                running = True
                print("-------------------------------")
                print(arr)
                print("-------------------------------")
                while running:
                    offscreen_canvas.Clear()
                    buffer = 6
                    pos -= 1
                    offset = 0
                    if isinstance(arr, list) and "mlb logo" in arr[0][0]:
                        for game in arr:
                            if "mlb logo" in game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogos["MLB"], pos + offset, -9
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    statusString,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + versus,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallestFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayTeam,
                                    12,
                                    white,
                                    awayTeamStatusString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallestFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam,
                                    26,
                                    white,
                                    homeTeamStatusString,
                                )
                                if awayTeam > homeTeam:
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus
                                        + buffer,
                                        12,
                                        green,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus
                                        + buffer,
                                        26,
                                        green,
                                        homeOddsString,
                                    )
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        12,
                                        green,
                                        "O/U",
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        26,
                                        green,
                                        overUnderString,
                                    )
                                else:
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus
                                        + buffer,
                                        12,
                                        green,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus
                                        + buffer,
                                        26,
                                        green,
                                        homeOddsString,
                                    )
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        12,
                                        green,
                                        "O/U",
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        26,
                                        green,
                                        overUnderString,
                                    )
                                if awayTeam > homeTeam:
                                    awayPitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        12,
                                        yellow,
                                        awayPitcherString,
                                    )
                                    homePitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        26,
                                        yellow,
                                        homePitcherString,
                                    )
                                else:
                                    awayPitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        12,
                                        yellow,
                                        awayPitcherString,
                                    )
                                    homePitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogos[game[10]].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        26,
                                        yellow,
                                        homePitcherString,
                                    )
                            if "inProgress" in game[0]:
                                bases = [[10, 5], [6, 0], [2, 5]]
                                outs = [[2, 20], [8, 20], [14, 20]]
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                pitcherNameString = game[17]
                                batterNameString = game[19]
                                inningString = game[20]
                                countString = game[21]
                                outsString = game[22]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                baseSize = 6
                                outsSize = 4
                                baseHalf = abs(baseSize / 2)
                                for base in bases:
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1],
                                        pos + offset + runningTotal + base[0],
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1],
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseSize,
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1] + baseSize,
                                        pos + offset + runningTotal + base[0],
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1] + baseSize,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseSize,
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                for out in outs:
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0],
                                        out[1],
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1],
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0],
                                        out[1],
                                        pos + offset + runningTotal + out[0],
                                        out[1] + outsSize,
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1] + outsSize,
                                        pos + offset + runningTotal + out[0],
                                        out[1] + outsSize,
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1] + outsSize,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1],
                                        red,
                                    )
                                if (
                                    "1st" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[0][0]
                                    y = bases[0][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    "2nd" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[1][0]
                                    y = bases[1][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    "3rd" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[2][0]
                                    y = bases[2][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    outsString == 1
                                    or outsString == 2
                                    or outsString == 3
                                ):
                                    x = outs[0][0]
                                    y = outs[0][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                if outsString == 2 or outsString == 3:
                                    x = outs[1][0]
                                    y = outs[1][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                if outsString == 3:
                                    x = outs[2][0]
                                    y = outs[2][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                situation = graphics.DrawText(
                                    offscreen_canvas,
                                    alilbiggerFont,
                                    pos + offset + runningTotal + 3,
                                    19,
                                    yellow,
                                    countString,
                                )
                                inning = graphics.DrawText(
                                    offscreen_canvas,
                                    alilbiggerFont,
                                    pos + offset + runningTotal - 5,
                                    31,
                                    yellow,
                                    inningString,
                                )
                            if "final" in game[0]:
                                bases = [[2, 5], [6, 0], [10, 5]]
                                outs = [[3, 20], [9, 20], [15, 20]]
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                pitcherNameString = game[17]
                                batterNameString = game[19]
                                inningString = game[20]
                                countString = game[21]
                                outsString = game[22]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                            if "pregame" in game[0]:
                                offset = offset + 190
                        time.sleep(0.01)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "nfl logo" in arr[0][0]:
                        for game in arr:
                            if "nfl logo" in game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogos["NFL"],
                                    pos + offset,
                                    -9,
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    statusString,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + versus,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                # awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 12, green, awayOddsString)
                                # homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 26, green, homeOddsString)
                                # overUnderStr = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer+ buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + homeTeam, 12, green, 'O/U')
                                # overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer+ homeTeam, 26, green, overUnderString)
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                if possession == "away":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "•",
                                    )
                                elif statusString == "Halftime":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                else:
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        26,
                                        green,
                                        "•",
                                    )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    12,
                                    yellow,
                                    statusString,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    26,
                                    yellow,
                                    situationString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 190
                            if "inProgress" in game[0]:
                                offset = offset + 190
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                        time.sleep(0.01)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "ncaa" in arr[0][0]:
                        for game in arr:
                            if "conference" in game[0]:
                                conferenceName = graphics.DrawText(
                                    offscreen_canvas,
                                    font,
                                    pos + offset,
                                    24,
                                    green,
                                    game[1],
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam
                                    + buffer,
                                    12,
                                    green,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam
                                    + buffer,
                                    26,
                                    green,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam,
                                    12,
                                    green,
                                    overUnderText,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam,
                                    26,
                                    green,
                                    overUnderString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                if possession == "away":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "•",
                                    )
                                elif statusString == "Halftime":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                else:
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        26,
                                        green,
                                        "•",
                                    )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    12,
                                    yellow,
                                    statusString,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    26,
                                    yellow,
                                    situationString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 190
                            if "inProgress" in game[0]:
                                offset = offset + 190
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    green,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                        time.sleep(0.01)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "stocks" in arr[0]:
                        for game in arr[1]:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "up" in game[5]:
                                color = green
                            if "down" in game[5]:
                                color = red
                            logo = game[0]
                            stockStr = game[4]
                            # offscreen_canvas.SetImage(logo, pos + offset, -10)
                            string = graphics.DrawText(
                                offscreen_canvas,
                                font,
                                pos + offset + buffer,
                                24,
                                color,
                                stockStr,
                            )
                            offset = offset + string + 80
                        time.sleep(0.015)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "rssFeed" in arr[0]:
                        blackVs = graphics.DrawText(
                            offscreen_canvas, bFont, -1000, 12, green, arr[1]
                        )
                        versus = graphics.DrawText(
                            offscreen_canvas,
                            bFont,
                            ((offscreen_canvas.width / 2) - (blackVs / 2)),
                            12,
                            blue,
                            arr[1],
                        )
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 26, green, arr[2]
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif arr == None:
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == False:
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == "":
                        print("it was empty string")
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == "MANCAVEDISPLAYS":
                        www = graphics.DrawText(
                            offscreen_canvas, middleFont, pos, 26, green, "www."
                        )
                        mancavedisplays = graphics.DrawText(
                            offscreen_canvas, font, pos + www, 26, green, arr
                        )
                        com = graphics.DrawText(
                            offscreen_canvas,
                            middleFont,
                            pos + www + mancavedisplays,
                            26,
                            green,
                            ".com",
                        )
                        pos -= 1
                        if pos + com < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif isinstance(arr, list) and (
                        arr[0] == "golf" or "rankings" in arr[0]
                    ):
                        blackVs = graphics.DrawText(
                            offscreen_canvas, bFont, -1000, 12, green, arr[1]
                        )
                        versus = graphics.DrawText(
                            offscreen_canvas,
                            bFont,
                            ((offscreen_canvas.width / 2) - (blackVs / 2)),
                            12,
                            blue,
                            arr[1],
                        )
                        # versus2 = graphics.DrawText(offscreen_canvas, bFont,(offscreen_canvas.width / 2)+ versus + 25, 12, blue, arr[2])
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 26, green, arr[3]
                        )
                        pos -= 1
                        time.sleep(0.020)
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                    else:
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 20, green, arr
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.03)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
