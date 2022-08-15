#!/usr/bin/env python
# Display a runtext with double-buffering.
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
                    "https://a.espncdn.com/i/teamlogos/mlb/500/scoreboard/mia.png",
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
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/ari.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Falcons": Image.open(
                requests.get(
                    "data:image/png;base64,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",
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
                    "https://loodibee.com/wp-content/uploads/nfl-buffalo-bills-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Carolina Panthers": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/car.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Bears": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/chi.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Bengals": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/cin.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Browns": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/cle.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Jacksonville Jaguars": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/jax.png",
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
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/dal.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Denver Broncos": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/den.png",
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
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/gb.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Texans": Image.open(
                requests.get(
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/hou.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indianapolis Colts": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-indianapolis-colts-team-logo-2.png",
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
                    "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/mia.png",
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
                                    teamLogos["NFL"], pos + offset, -9
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
                            if "ncaa" in game[0][0]:
                                conferenceName = graphics.DrawText(
                                    offscreen_canvas,
                                    font,
                                    pos + offset,
                                    12,
                                    green,
                                    game[0][1],
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
                                # offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                # versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, statusString)
                                # offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + versus, -10)
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
                    elif (
                        isinstance(arr, list)
                        and arr[0] == "golf"
                        or "rankings" in arr[0]
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
