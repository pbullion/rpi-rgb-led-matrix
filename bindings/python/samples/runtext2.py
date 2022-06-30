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
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/pbullion@gmail.com")
            responseArr = json.loads(url.text)
            # responseArr = [[['mlb logo'],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png",250,250,250,"New York Mets","https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png",250,250,250,"Miami Marlins","","2","3","Final","","","","","","","","","","","","","new-york-mets","miami-marlins","Fortes solo HR with 2 outs in bottom of 9th, Miami tops Mets"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png",250,250,250,"Houston Astros","https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png",1,23,57,"New York Yankees","","3","6","Final/10","","","","","","","","","","","","","houston-astros","new-york-yankees","Yankees' Judge walks off Astros for 2nd time in 4 days"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png",250,250,250,"Boston Red Sox","https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png",250,250,250,"Cleveland Guardians","","8","3","Final","","","","","","","","","","","","","boston-red-sox","cleveland-guardians","Red Sox beat Guardians 8-3 for sweep, winning streak at 7"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png",17,17,17,"Pittsburgh Pirates","https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png",250,250,250,"Tampa Bay Rays","","2","4","Final","","","","","","","","","","","","","pittsburgh-pirates","tampa-bay-rays",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png",32,27,27,"Baltimore Orioles","https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png",27,21,22,"Chicago White Sox","","3","4","Final","","","","","","","","","","","","","baltimore-orioles","chicago-white-sox","Cease strikes out 13, White Sox hold off Orioles 4-3"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png",34,13,72,"Colorado Rockies","https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png",1,39,86,"Minnesota Twins","","3","6","Final","","","","","","","","","","","","","colorado-rockies","minnesota-twins",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png",1,67,38,"Oakland Athletics","https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png",250,250,250,"Kansas City Royals","","5","3","Final","","","","","","","","","","","","","oakland-athletics","kansas-city-royals","Brown, Allen boost A's in 5-3 win over Royals"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png",250,250,250,"Toronto Blue Jays","https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png",5,12,51,"Milwaukee Brewers","","3","10","Final","","","","","","","","","","","","","toronto-blue-jays","milwaukee-brewers",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png",250,250,250,"Chicago Cubs","https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png",184,2,32,"St. Louis Cardinals","","6","5","Final/10","","","","","","","","","","","","","chicago-cubs","st.-louis-cardinals","Cubs overcome 5-run deficit to beat Cards 6-5, Flaherty hurt"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png",10,41,93,"Washington Nationals","https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png",250,250,250,"Texas Rangers","","6","4","Final","","","","","","","","","","","","","washington-nationals","texas-rangers",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png",196,20,34,"Cincinnati Reds","https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png",22,20,21,"San Francisco Giants","","10","3","Final","","","","","","","","","","","","","cincinnati-reds","san-francisco-giants","Mahle ends long drought, Reds thump Giants 10-3"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png",1,42,91,"Seattle Mariners","https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png",165,0,23,"Los Angeles Angels","","1","2","Final","","","","","","","","","","","","","seattle-mariners","los-angeles-angels","Melee mayhem: Big brawl, 8 ejected, Angels top Mariners 2-1"],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png",250,250,250,"Detroit Tigers","https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png",164,0,19,"Arizona Diamondbacks","","7","11","Final","","","","","","","","","","","","","detroit-tigers","arizona-diamondbacks",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png",190,0,17,"Philadelphia Phillies","https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png",47,36,29,"San Diego Padres","","8","5","Final","","","","","","","","","","","","","philadelphia-phillies","san-diego-padres",""],["game final mlb","https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png",250,250,250,"Los Angeles Dodgers","https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png",250,250,250,"Atlanta Braves","","5","3","Final/11","","","","","","","","","","","","","los-angeles-dodgers","atlanta-braves","Taylor drives in go-ahead run, Dodgers top Braves 5-3 in 11"]],[["game final nhl","https://loodibee.com/wp-content/uploads/nhl-colorado-avalanche-logo.png",134,0,56,"Colorado Avalanche","https://loodibee.com/wp-content/uploads/nhl-tampa-bay-lightning-logo.png",250,250,250,"Tampa Bay Lightning","","2","1","Final","","","","","","","","","","","","","colorado-avalanche","tampa-bay-lightning","Avalanche dethrone Lightning to win Stanley Cup for 3rd time"]],"",""]
            # responseArr = [[['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', 27, 21, 22, 'Chicago White Sox', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'Bot 2nd', '0', '0', 'Bottom 2nd', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/mlb/players/full/32697.png', 'L. Giolito • 1.1 IP, 0 ER, 2 H, K, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/30429.png', 'M. Stassi • 0-0', 'Bot 2nd', '0-1', 1, 'chicago-white-sox', 'los-angeles-angels'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png', 32, 27, 27, 'Baltimore Orioles', 'https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', 1, 42, 91, 'Seattle Mariners', '10:10 PM EDT', '34-40', '34-40', '', '+130', '-154', 'O/U 7.5', 'T. Wells 5-4 3.34', 'G. Kirby 2-2 3.12']], '', '', '']
            # responseArr = [['golf', 'John Deere Classic', 'Round 1 - In Progress', '1 J.T. Poston -9 • 2 Vaughn Taylor -6 • T3 Ricky Barnes -5 • T3 Denny McCarthy -5 • T3 Chris Naegel -5 • T6 Taylor Moore -4 • T6 Scott Stallings -4 • T6 Chesson Hadley -4 • T6 Mark Hubbard -4 • T6 Adam Svensson -4'], ['rssFeed', 'ESPNGOLF', "How to watch the PGA Tour's John Deere Classic on ESPN+ • Fox claims 1-shot lead after Day 1 at Irish Open • U.S. captain doubts LIV golfers' Ryder Cup hopes"], ['rssFeed', 'CNN', "The Court handcuffed the Environmental Protection Agency's ability to regulate emissions from power plants, just as scientists warn the world is running out of time to address the climate crisis • 'Devastating': See ex-EPA administrator's reaction to Supreme Court's ruling • Supreme Court tells lower courts to reconsider disputes on abortion and guns after blockbuster decisions "]]
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            color = green
            print(responseArr)
            for arr in responseArr:
                running = True
                print('-------------------------------')
                print(arr)
                print(arr[0])
                print('-------------------------------')
                while running:
                    offscreen_canvas.Clear()
                    buffer = 6
                    pos -= 1
                    offset = 0
                    if isinstance(arr, list) and 'mlb' in arr[0][0]:
                        for game in arr:
                            if 'mlb logo' in game[0]:
                                offscreen_canvas.SetImage(teamLogos['MLB'], pos + offset, -10)
                            elif 'nhl logo' in game[0]:
                                offscreen_canvas.SetImage(teamLogos['NHL'], pos + offset, -10)
                            
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if 'pregame' in game[0]:
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
                                awayOddsString = game[15]
                                homeOddsverUnderString = String = game[16]
                                overUnderString = verUnderString = game[17]
                                offscreen_canvas.SetImage(teamLogos[game[5]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + teamLogos[game[5]].width, 24, green, statusString)
                                offscreen_canvas.SetImage(teamLogos[game[10]], pos + offset + teamLogos[game[5]].width + buffer + buffer + versus, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 12, white, awayTeamString)
                                awayTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer + awayTeam, 12, white, awayTeamStatusString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer, 26, white, homeTeamString)
                                homeTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + homeTeam, 26, white, homeTeamStatusString)
                                awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ + buffer + buffer + homeTeam + homeTeamStatus, 12, green, awayOddsString)
                                homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ + buffer + buffer + homeTeam + homeTeamStatus, 26, green, homeOddsString)
                                overUnderString = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ + buffer + buffer+ buffer + buffer + homeTeam + homeTeamStatus, 12, green, 'O/U')
                                overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ + buffer + buffer+ buffer + buffer + homeTeam + homeTeamStatus, 26, green, overUnderString)
                                if awayTeam > homeTeam:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + awayTeam + awayTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer + awayTeam + awayTeamStatus, 26, yellow, homePitcherString)
                                else:
                                    awayPitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 12, yellow, awayPitcherString)
                                    homePitcher = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + homeOdds + teamLogos[game[10]].width + buffer + buffer+ buffer + buffer+ buffer + buffer + buffer + buffer + + buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 26, yellow, homePitcherString)
                            if 'inProgress' in game[0]:
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
                                outsHalf = abs(outsSize/2)
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
                                if outsString == 1:
                                    for y_offset in range(outsSize):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[0][0], pos + offset + runningTotal + outs[0][1] + y_offset, pos + offset + runningTotal + outs[0][0] + outsSize, pos + offset + runningTotal + outs[0][1] + y_offset, red)
                                elif outsString == 2:
                                    for y_offset in range(outsSize):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[0][0], pos + offset + runningTotal + outs[0][1] + y_offset, pos + offset + runningTotal + outs[0][0] + outsSize, pos + offset + runningTotal + outs[0][1] + y_offset, red)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[1][0], pos + offset + runningTotal + outs[1][1] + y_offset, pos + offset + runningTotal + outs[1][0] + outsSize, pos + offset + runningTotal + outs[1][1] + y_offset, red)
                                elif outsString == 3:
                                    for y_offset in range(outsSize):
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[0][0], pos + offset + runningTotal + outs[0][1] + y_offset, pos + offset + runningTotal + outs[0][0] + outsSize, pos + offset + runningTotal + outs[0][1] + y_offset, red)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[1][0], pos + offset + runningTotal + outs[1][1] + y_offset, pos + offset + runningTotal + outs[1][0] + outsSize, pos + offset + runningTotal + outs[1][1] + y_offset, red)
                                        graphics.DrawLine(offscreen_canvas, pos + offset + runningTotal + outs[2][0], pos + offset + runningTotal + outs[2][1] + y_offset, pos + offset + runningTotal + outs[2][0] + outsSize, pos + offset + runningTotal + outs[2][1] + y_offset, red)
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
                    elif isinstance(arr, list) and 'rssFeed' in arr[0]:
                        versus = graphics.DrawText(offscreen_canvas, smallFont, 200, 12, green, arr[1])
                        length = graphics.DrawText(offscreen_canvas, smallFont, pos, 26, green, arr[2])
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.01)
                    elif arr[0] == 'golf':
                        versus = graphics.DrawText(offscreen_canvas, smallFont, 115, 12, green, arr[1])
                        roundStatus = graphics.DrawText(offscreen_canvas, smallFont, 115 + versus + 20, 12, green, arr[2])
                        length = graphics.DrawText(offscreen_canvas, smallFont, pos, 26, green, arr[3])
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.01)
                    else:
                        time.sleep(0.01)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()