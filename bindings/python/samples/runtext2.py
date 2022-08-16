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
                    "https://i.redd.it/1rsnuls0llu71.jpg",
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
                    "https://seeklogo.com/images/G/green-bay-packers-logo-2A5FB2D033-seeklogo.com.png",
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
                    "https://w7.pngwing.com/pngs/281/691/png-transparent-indianapolis-colts-nfl-jacksonville-jaguars-tennessee-titans-super-bowl-nfl-blue-angle-text.png",
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
                    "data:image/jpeg;base64,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",
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
                                    teamLogos["New York Jets"],
                                    pos + offset,
                                    -9,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos["Indianapolis Colts"],
                                    pos + offset + 75,
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
