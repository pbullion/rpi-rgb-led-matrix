#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import math
import time
import requests, json
import json
import random
from PIL import Image
import requests

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        teamLogos = {
                'MLB': Image.open(requests.get('https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'NFL': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-league-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'NHL': Image.open(requests.get('https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'NHL': Image.open(requests.get('https://upload.wikimedia.org/wikipedia/en/3/3a/05_NHL_Shield.svg', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Tampa Bay Lightning': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nhl-tampa-bay-lightning-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Colorado Avalanche': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nhl-colorado-avalanche-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'New York Yankees': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Washington Nationals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Texas Rangers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'New York Mets': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Miami Marlins': Image.open(requests.get('https://i.pinimg.com/originals/de/28/5a/de285a2a2a4656fc4c0be916c068df03.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Oakland Athletics': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Kansas City Royals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Toronto Blue Jays': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Milwaukee Brewers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Boston Red Sox': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Cleveland Guardians': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Cincinnati Reds': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'San Francisco Giants': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Colorado Rockies': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Minnesota Twins': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Los Angeles Dodgers': Image.open(requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/LA_Dodgers_cap_logo.svg/1200px-LA_Dodgers_cap_logo.svg.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Los Angeles Dodgers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Atlanta Braves': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Seattle Mariners': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Los Angeles Angels': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Detroit Tigers': Image.open(requests.get('https://logos-download.com/wp-content/uploads/2016/04/Detroit_Tigers_Insignia_logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Arizona Diamondbacks': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Philadelphia Phillies': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'San Diego Padres': Image.open(requests.get('https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Pittsburgh Pirates': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Tampa Bay Rays': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Baltimore Orioles': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Chicago White Sox': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'St. Louis Cardinals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Chicago Cubs': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Houston Astros': Image.open(requests.get('https://images.ctfassets.net/iiozhi00a8lc/t117_favicon117_qgouernt_ehw9pj78_png/700d0ebafa92b5499f3dc09bf465fc98/t117_favicon.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Arizona Cardinals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-arizona-cardinals-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Atlanta Falcons': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-atlanta-falcons-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Baltimore Ravens': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-baltimore-ravens-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Buffalo Bills': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-buffalo-bills-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Carolina Panthers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-carolina-panthers-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Chicago Bears': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-chicago-bears-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Cincinnati Bengals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-cincinnati-bengals-team-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Cleveland Browns': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nfl-cleveland-browns-team-logo-2.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Jacksonville Jaguars': Image.open(requests.get('https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/jax.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Las Vegas Raiders': Image.open(requests.get('https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/lv.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'Arizona': Image.open(requests.get('', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
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
            print('getting responseArrrrrrrrr')
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/spectatorsBarAndGrill")
            responseArr = json.loads(url.text)
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            print(offscreen_canvas)
            pos = offscreen_canvas.width
            color = green
            print(responseArr)
            for arr in responseArr:
                running = True
                print('-------------------------------')
                print(arr)
                print('-------------------------------')
                while running:
                    offscreen_canvas.Clear()
                    buffer = 6
                    pos -= 1
                    offset = 0
                    if isinstance(arr, list) and 'mlb logo' in arr[0][0]:
                        for game in arr:
                            if 'mlb logo' in game[0]:
                                offscreen_canvas.SetImage(teamLogos['MLB'], pos + offset, -9)
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if 'pregame' in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19] 
                                awayOddsString = game[15]
                                homeOddsString = String = game[16]
                                overUnderString = verUnderString = game[17]
                                offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, statusString)
                                offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + versus, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 12, white, awayTeamString)
                                awayTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer + awayTeam, 12, white, awayTeamStatusString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 26, white, homeTeamString)
                                homeTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + homeTeam, 26, white, homeTeamStatusString)
                                awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + homeTeamStatus + buffer, 12, green, awayOddsString)
                                homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + homeTeamStatus + buffer, 26, green, homeOddsString)
                                overUnderStr = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer+ buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + homeTeam + homeTeamStatus, 12, green, 'O/U')
                                overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer+ homeTeam + homeTeamStatus, 26, green, overUnderString)
                                if awayTeam > homeTeam:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + overUnderStr + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + awayTeam + awayTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + overUnderStr + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer + awayTeam + awayTeamStatus, 26, yellow, homePitcherString)
                                else:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + overUnderStr + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + overUnderStr + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + buffer + buffer + buffer + buffer + homeTeam + homeTeamStatus, 26, yellow, homePitcherString)
                            if 'inProgress' in game[0]:
                                bases =  [[10,5],[6,0],[2,5]]
                                outs = [[2,20],[8,20],[14,20]]
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
                                if int(awayTeamStatusString) < int(homeTeamStatusString):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(homeTeamStatusString):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, 'vs')
                                offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + buffer + buffer + buffer, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 12, awayColor, awayTeamString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 26, homeColor, homeTeamString)
                                scoreLocation = 0
                                if (homeTeam > awayTeam):
                                    scoreLocation = homeTeam + buffer + teamLogos[game[5]].width + versus + teamLogos[game[10]].width
                                else:
                                    scoreLocation = awayTeam + buffer + teamLogos[game[5]].width + versus + teamLogos[game[10]].width
                                awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + buffer + buffer + buffer + scoreLocation + buffer, 12, awayColor, awayTeamStatusString)
                                homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + buffer + buffer + buffer + scoreLocation + buffer, 26, homeColor, homeTeamStatusString)
                                runningTotal = scoreLocation + buffer + buffer + awayTeamStatus + buffer + buffer + buffer + buffer + buffer 
                                baseSize = 6
                                outsSize = 4
                                baseHalf = abs(baseSize/2)
                                for base in bases:
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + base[0] + baseHalf, base[1], pos + offset + runningTotal + base[0], base[1]+ baseHalf, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + base[0] + baseHalf, base[1], pos + offset + runningTotal + base[0] + baseSize, base[1]+ baseHalf, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + base[0] + baseHalf, base[1]+ baseSize, pos + offset + runningTotal + base[0], base[1]+ baseHalf, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + base[0] + baseHalf, base[1]+ baseSize, pos + offset + runningTotal + base[0] + baseSize, base[1]+ baseHalf, yellow)
                                for out in outs:
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + out[0], out[1], pos + offset + runningTotal + out[0] + outsSize, out[1], red)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + out[0], out[1], pos + offset + runningTotal + out[0], out[1] + outsSize, red)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + out[0] + outsSize, out[1] + outsSize, pos + offset + runningTotal + out[0], out[1] + outsSize, red)
                                    graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + out[0] + outsSize, out[1] + outsSize, pos + offset + runningTotal + out[0] + outsSize, out[1], red)
                                if '1st' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                    x = bases[0][0]
                                    y = bases[0][1]
                                    size = 6
                                    half = round(abs(size/2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + size - testing, pos + offset + runningTotal + x + half + testing, y + size - testing, yellow)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + testing, pos + offset + runningTotal + x + half + testing, y + testing, yellow)
                                if '2nd' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                    x = bases[1][0]
                                    y = bases[1][1]
                                    size = 6
                                    half = round(abs(size/2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + size - testing, pos + offset + runningTotal + x + half + testing, y + size - testing, yellow)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + testing, pos + offset + runningTotal + x + half + testing, y + testing, yellow)
                                if '3rd' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                    x = bases[2][0]
                                    y = bases[2][1]
                                    size = 6
                                    half = round(abs(size/2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + size - testing, pos + offset + runningTotal + x + half + testing, y + size - testing, yellow)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x + half - testing, y + testing, pos + offset + runningTotal + x + half + testing, y + testing, yellow)
                                if outsString == 1 or outsString == 2 or outsString == 3:
                                    x = outs[0][0]
                                    y = outs[0][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x, y + y_offset, pos + runningTotal + offset + x + outsSize, y + y_offset, red)
                                if outsString == 2 or outsString == 3:
                                    x = outs[1][0]
                                    y = outs[1][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x, y + y_offset, pos + runningTotal + offset + x + outsSize, y + y_offset, red)
                                if outsString == 3:
                                    x = outs[2][0]
                                    y = outs[2][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + x, y + y_offset, pos + runningTotal + offset + x + outsSize, y + y_offset, red)
                                situation = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos + offset + runningTotal + 3, 19, yellow, countString)
                                inning = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos + offset + runningTotal - 5, 31, yellow, inningString)
                            if 'final' in game[0]:
                                bases =  [[2,5],[6,0],[10,5]]
                                outs = [[3,20],[9,20],[15,20]]
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
                                if int(awayTeamStatusString) < int(homeTeamStatusString):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(homeTeamStatusString):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, 'vs')
                                offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + buffer + buffer + buffer, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 12, awayColor, awayTeamString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 26, homeColor, homeTeamString)
                                scoreLocation = 0
                                if (homeTeam > awayTeam):
                                    scoreLocation = homeTeam + buffer + teamLogos[game[5]].width + versus + teamLogos[game[10]].width
                                else:
                                    scoreLocation = awayTeam + buffer + teamLogos[game[5]].width + versus + teamLogos[game[10]].width
                                awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + buffer + buffer + buffer + scoreLocation + buffer, 12, awayColor, awayTeamStatusString)
                                homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + buffer + buffer + buffer + scoreLocation + buffer, 26, homeColor, homeTeamStatusString)
                                runningTotal = scoreLocation + buffer + buffer + awayTeamStatus + buffer + buffer + buffer + buffer + buffer 
                                finalString = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + runningTotal, 12, yellow, oddsString)
                                headlineString = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + buffer + runningTotal, 26, green, headline)
                            if awayTeam > homeTeam:
                                offset = offset + awayTeam + awayTeamStatus + headlineString + 240
                            else:
                                offset = offset + homeTeam + homeTeamStatus + headlineString + 240
                            if 'pregame' in game[0]:
                                offset = offset + 190
                        time.sleep(0.01)
                        if (pos + offset < 0):
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and 'nfl logo' in arr[0][0]:
                        for game in arr:
                            if 'nfl logo' in game[0]:
                                offscreen_canvas.SetImage(teamLogos['NFL'], pos + offset, -9)
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            if 'pregame' in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = String = game[16]
                                overUnderString = verUnderString = game[17]
                                offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, statusString)
                                offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + versus, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 12, white, awayTeamString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 26, white, homeTeamString)
                                # awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 12, green, awayOddsString)
                                # homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 26, green, homeOddsString)
                                # overUnderStr = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer+ buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + homeTeam, 12, green, 'O/U')
                                # overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer+ homeTeam, 26, green, overUnderString)
                            if awayTeam > homeTeam:
                                offset = offset + awayTeam + 240
                            else:
                                offset = offset + homeTeam + 240
                            if 'pregame' in game[0]:
                                offset = offset + 190
                        time.sleep(0.01)
                        if (pos + offset < 0):
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and 'stocks' in arr[0]:
                        for game in arr[1]:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if 'up' in game[5]:
                                color = green
                            if 'down' in game[5]:
                                color = red
                            logo = game[0]
                            stockStr = game[4]
                            # offscreen_canvas.SetImage(logo, pos + offset, -10)
                            string = graphics.DrawText(offscreen_canvas, font, pos + offset + buffer, 24, color, stockStr)
                            offset = offset + string + 80
                        time.sleep(0.015)
                        if (pos + offset < 0):
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and 'rssFeed' in arr[0]:
                        blackVs = graphics.DrawText(offscreen_canvas, bFont, -1000, 12, green, arr[1])
                        versus = graphics.DrawText(offscreen_canvas, bFont, ((offscreen_canvas.width / 2) - (blackVs / 2)), 12, blue, arr[1])
                        length = graphics.DrawText(offscreen_canvas, bFont, pos, 26, green, arr[2])
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif arr == False:
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == '':
                        print('it was empty string')
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == 'MANCAVEDISPLAYS':
                        www = graphics.DrawText(offscreen_canvas, middleFont, pos, 26, green, 'www.')
                        mancavedisplays = graphics.DrawText(offscreen_canvas, font, pos + www, 26, green, arr)
                        com = graphics.DrawText(offscreen_canvas, middleFont, pos + www + mancavedisplays, 26, green, '.com')
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif isinstance(arr, list) and arr[0] == 'golf':
                        blackVs = graphics.DrawText(offscreen_canvas, bFont, -1000, 12, green, arr[1])
                        versus = graphics.DrawText(offscreen_canvas, bFont, ((offscreen_canvas.width / 2) - (blackVs / 2)), 12, blue, arr[1])
                        # versus2 = graphics.DrawText(offscreen_canvas, bFont,(offscreen_canvas.width / 2)+ versus + 25, 12, blue, arr[2])
                        length = graphics.DrawText(offscreen_canvas, bFont, pos, 26, green, arr[3])
                        pos -= 1
                        time.sleep(0.020)
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                    else:
                        length = graphics.DrawText(offscreen_canvas, bFont, pos, 20, green, arr)
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.03)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()