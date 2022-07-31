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
                'NHL': Image.open(requests.get('https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'NHL': Image.open(requests.get('https://upload.wikimedia.org/wikipedia/en/3/3a/05_NHL_Shield.svg', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Tampa Bay Lightning': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nhl-tampa-bay-lightning-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Colorado Avalanche': Image.open(requests.get('https://loodibee.com/wp-content/uploads/nhl-colorado-avalanche-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'New York Yankees': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Washington Nationals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Texas Rangers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'New York Mets': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Miami Marlins': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
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
                'Los Angeles Dodgers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Atlanta Braves': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Seattle Mariners': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Los Angeles Angels': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Detroit Tigers': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Arizona Diamondbacks': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Philadelphia Phillies': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                # 'San Diego Padres': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'San Diego Padres': Image.open(requests.get('https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Pittsburgh Pirates': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Tampa Bay Rays': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Baltimore Orioles': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Chicago White Sox': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'St. Louis Cardinals': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Chicago Cubs': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
                'Houston Astros': Image.open(requests.get('https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png', stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS),
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
            print('getting responseArr')
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/spectatorsBarAndGrill")
            # responseArr = json.loads(url.text)
            responseArr = [[['mlb logo'], ['game final mlb', 'https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png', 250, 250, 250, 'Detroit Tigers', 'https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png', 250, 250, 250, 'Toronto Blue Jays', '', '1', '4', 'Final', '', '', '', '', '', '', '', '', '', '', '', '', 'detroit-tigers', 'toronto-blue-jays', 'Chapman homers, Berríos gets win as Jays beat Tigers 4-1'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', 164, 0, 19, 'Arizona Diamondbacks', 'https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', 250, 250, 250, 'Atlanta Braves', 'Bot 7th', '0', '0', 'Bottom 7th', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/mlb/players/full/32968.png', 'M. Kelly • 6.1 IP, 0 ER, 3 H, 6 K, 2 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/29951.png', "T. d'Arnaud • 0-1, BB, K", 'Bot 7th', '1-2', 1, 'arizona-diamondbacks', 'atlanta-braves'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png', 250, 250, 250, 'Kansas City Royals', 'https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', 1, 23, 57, 'New York Yankees', 'Top 6th', '4', '3', 'Top 6th', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/mlb/players/full/36036.png', 'W. Peralta • 0.0 IP, 0 ER, 0 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/40948.png', 'M. Melendez • 1-2, R, K', 'Top 6th', '0-0', 2, 'kansas-city-royals', 'new-york-yankees'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png', 5, 12, 51, 'Milwaukee Brewers', 'https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png', 250, 250, 250, 'Boston Red Sox', 'End 6th', '2', '7', 'End 6th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'End 6th', '0-0', 0, 'milwaukee-brewers', 'boston-red-sox'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', 190, 0, 17, 'Philadelphia Phillies', 'https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png', 17, 17, 17, 'Pittsburgh Pirates', 'Bot 6th', '8', '1', 'Bottom 6th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/33709.png', 'A. Nola • 5.0 IP, ER, 6 H, 7 K, BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/40684.png', 'B. Madris • 0-2', 'Bot 6th', '0-0', 0, 'philadelphia-phillies', 'pittsburgh-pirates'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png', 184, 2, 32, 'St. Louis Cardinals', 'https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', 10, 41, 93, 'Washington Nationals', 'Top 8th', '5', '0', 'Top 8th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/30963.png', 'S. Cishek • 0.0 IP, 0 ER, 0 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/41174.png', 'N. Gorman • 1-2, R, BB, K', 'Top 8th', '0-0', 0, 'st.-louis-cardinals', 'washington-nationals'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png', 32, 27, 27, 'Baltimore Orioles', 'https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png', 196, 20, 34, 'Cincinnati Reds', 'Bot 6th', '0', '1', 'Bottom 6th', 'Runners on 1st & 2nd', 'https://a.espncdn.com/i/headshots/mlb/players/full/36089.png', 'C. Perez • 0.0 IP, 0 ER, H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/32269.png', 'B. Drury • 0-0', 'Bot 6th', '0-0', 1, 'baltimore-orioles', 'cincinnati-reds'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png', 250, 250, 250, 'Cleveland Guardians', 'https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', 250, 250, 250, 'Tampa Bay Rays', 'Bot 6th', '5', '3', 'Bottom 6th', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/nophoto.png', 'K. McCarty • 2.2 IP, ER, 4 H, 2 K, 2 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/31779.png', 'J. Choi • 0-2, 2 RBI, K', 'Bot 6th', '0-0', 2, 'cleveland-guardians', 'tampa-bay-rays'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', 250, 250, 250, 'New York Mets', 'https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png', 250, 250, 250, 'Miami Marlins', 'Top 6th', '7', '1', 'Top 6th', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/mlb/players/full/38898.png', 'J. Fishman • 2.2 IP, ER, 4 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/32788.png', 'T. Naquin • 1-3, 3B, RBI, R', 'Top 6th', '0-0', 1, 'new-york-mets', 'miami-marlins'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', 27, 21, 22, 'Chicago White Sox', 'End 5th', '1', '3', 'End 5th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'End 5th', '0-0', 0, 'oakland-athletics', 'chicago-white-sox'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', 1, 42, 91, 'Seattle Mariners', 'https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png', 250, 250, 250, 'Houston Astros', 'End 5th', '0', '2', 'End 5th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'End 5th', '0-0', 0, 'seattle-mariners', 'houston-astros'], ['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', 250, 250, 250, 'Los Angeles Dodgers', 'https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png', 34, 13, 72, 'Colorado Rockies', 'Bot 2nd', '0', '0', 'Bottom 2nd', 'Runner on 2nd', 'https://a.espncdn.com/i/headshots/mlb/players/full/38958.png', 'T. Gonsolin • 1.1 IP, 0 ER, 2 H, K, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/35440.png', 'C. Joe • 0-0', 'Bot 2nd', '1-2', 1, 'los-angeles-dodgers', 'colorado-rockies'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', 250, 250, 250, 'Texas Rangers', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', '3:07', '45-55', '43-58', '', '+110', '-130', '8.5', 'D. Dunning 1-6 4.38', 'R. Detmers 3-3 3.84'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png', 1, 39, 86, 'Minnesota Twins', 'https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png', 47, 36, 29, 'San Diego Padres', '3:10', '53-47', '56-46', '', '+122', '-144', '8.5', 'D. Bundy 6-4 5.02', 'S. Manaea 5-5 4.33'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', 250, 250, 250, 'Chicago Cubs', 'https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png', 22, 20, 21, 'San Francisco Giants', '6:00', '41-59', '50-51', '', '+152', '-180', '7.5', 'A. Sampson 0-1 3.20', 'C. Rodon 8-6 3.18']], ['golf', 'Rocket Mortgage Classic', 'Round 4 - In Progress', '1. Tony Finau -23 • 2. Taylor Pendrith -21 • 3. Patrick Cantlay -20 • 6. Joohyung Kim -18 • T4. Stephan Jaeger -18 • T4. Cameron Young -18 • 7. Wyndham Clark -16 • T8. Troy Merritt -15 • T8. J.J. Spaun -15 • T8. Russell Henley -15 • T8. Chris Kirk -15 • T8. Taylor Moore -15'], 'HAPPY HOUR EVERYDAY 4-7 PM', '', ['rssFeed', 'ESPN TOP NEWS', "Biggest fantasy football training camp storylines: Aaron Rodgers' new WR1, Michael Thomas' return and backfield battles • Mock draft: 10-team, 1/2 PPR, superflex • Celtics great Russell, 11-time champ, dies at 88"], 'STEAK NIGHT EVERY THURSDAY', 'WWW.MANCAVEDISPLAYS.COM', ['stocks', []]]
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
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
                            print('-------------------------------')
                            print(game[0])
                            print('-------------------------------')
                            if 'mlb logo' in game[0]:
                                print('heerrrrreeeeeeeee')
                                offscreen_canvas.SetImage(teamLogos['MLB'], pos + offset, -10)
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
                                awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + homeTeamStatus + buffer, 12, green, awayOddsString)
                                homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + homeTeamStatus + buffer, 26, green, homeOddsString)
                                overUnderStr = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer+ buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + homeTeam + homeTeamStatus, 12, green, 'O/U')
                                overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer+ homeTeam + homeTeamStatus, 26, green, overUnderString)
                                if awayTeam > homeTeam:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + awayTeam + awayTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer + awayTeam + awayTeamStatus, 26, yellow, homePitcherString)
                                else:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + buffer + buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 26, yellow, homePitcherString)
                            if 'inProgress' in game[0]:
                                print('IN PROGRESSLKSJDFLKSJDFLKSJDFLKJSDLKFJSLKDFJLKSDJFLKSJDF')
                                print(game)
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
                        time.sleep(0.5)
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
                            offset = offset + string + 100
                        time.sleep(0.02)
                        if (pos + offset < 0):
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and 'rssFeed' in arr[0]:
                        blackVs = graphics.DrawText(offscreen_canvas, bFont, -1000, 12, green, arr[1])
                        versus = graphics.DrawText(offscreen_canvas, bFont, (offscreen_canvas.width / 2) - (blackVs / 2), 12, blue, arr[1])
                        length = graphics.DrawText(offscreen_canvas, bFont, pos, 26, green, arr[2])
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif arr == False:
                        running = False
                        pos = offscreen_canvas.width
                    elif arr[0] == 'golf':
                        versus = graphics.DrawText(offscreen_canvas, smallFont, 115, 12, green, arr[1])
                        roundStatus = graphics.DrawText(offscreen_canvas, smallFont, 115 + versus + 20, 12, green, arr[2])
                        length = graphics.DrawText(offscreen_canvas, smallFont, pos, 26, green, arr[3])
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.035)
                    else:
                        running = False
                        pos = offscreen_canvas.width
                        # print('in the else')
                        # length = graphics.DrawText(offscreen_canvas, middleFont, pos, 26, green, arr)
                        # pos -= 1
                        # if (pos + length < 0):
                        #     running = False
                        #     pos = offscreen_canvas.width
                        # time.sleep(0.04)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()