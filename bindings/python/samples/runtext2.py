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
            mlbLogos = {
                'New York Yankees': Image.open('https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Washington Nationals': Image.open('https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Texas Rangers': Image.open('https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'New York Mets': Image.open('https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Miami Marlins': Image.open('https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Oakland Athletics': Image.open('https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Kansas City Royals': Image.open('https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Toronto Blue Jays': Image.open('https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Milwaukee Brewers': Image.open('https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Boston Red Sox': Image.open('https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Cleveland Guardians': Image.open('https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Cincinnati Reds': Image.open('https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'San Francisco Giants': Image.open('https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Colorado Rockies': Image.open('https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Minnesota Twins': Image.open('https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Los Angeles Dodgers': Image.open('https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Atlanta Braves': Image.open('https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Seatlle Mariners': Image.open('https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Los Angeles Angels': Image.open('https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Detriot Tigers': Image.open('https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Arizona Diamondbacks': Image.open('https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Philadelphia Phillies': Image.open('https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'San Diego Padres': Image.open('https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Pittsburgh Pirates': Image.open('https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Tampa Bay Rays': Image.open('https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Baltimore Orioles': Image.open('https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Chicago White Sox': Image.open('https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'St. Louis Cardinals': Image.open('https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Chicago Cubs': Image.open('https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
                'Houston Astros': Image.open('https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png').convert('RGB').resize((50, 50), Image.ANTIALIAS),
            }
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/pbullion@gmail.com")
            responseArr = json.loads(url.text)
            # responseArr = [['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png', 22, 20, 21, 'San Francisco Giants', 'https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png', 184, 2, 32, 'St. Louis Cardinals', 'Top 1st', '0', '0', 'Top 1st', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/38680.png', 'D. Hudson • 0.0 IP, 0 ER, 0 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/37798.png', 'L. Wade Jr. • 0-0', 'Top 1st', '0-0', 0, 'san-francisco-giants', 'st.-louis-cardinals'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png', 47, 36, 29, 'San Diego Padres', 'https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', 250, 250, 250, 'Atlanta Braves', 'Sat 4:05 PM EDT on FS1', '21-12', '15-18', '', '+118 * 1.5', '-138 * -1.5', 'O/U 8', 'S. Manaea 2-3 3.75', 'C. Morton 2-3 5.65'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'Sat 4:07 PM EDT ', '22-12', '14-20', '', '+118 * 1.5', '-138 * -1.5', 'O/U 7.5', 'J. Diaz 1-0 0.00', 'P. Blackburn 4-0 1.74'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo.png', 32, 27, 27, 'Baltimore Orioles', 'https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png', 250, 250, 250, 'Detroit Tigers', 'Sat 4:10 PM EDT ', '14-19', '10-23', '', '+104 * 1.5', '-122 * -1.5', 'O/U 8', 'B. Zimmermann 2-1 2.67', 'M. Pineda 1-2 3.43'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png', 5, 12, 51, 'Milwaukee Brewers', 'https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png', 250, 250, 250, 'Miami Marlins', 'Sat 6:10 PM EDT ', '21-12', '14-18', '', '-120 * -1.5', '+102 * 1.5', 'O/U 7', 'E. Lauer 3-0 1.82', 'T. Rogers 1-4 5.00'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png', 250, 250, 250, 'Toronto Blue Jays', 'https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', 250, 250, 250, 'Tampa Bay Rays', 'Sat 6:10 PM EDT ', '17-16', '20-13', '', '+102 * 1.5', '-120 * -1.5', 'O/U 8.5', 'H. Ryu 0-0 13.50', 'R. Yarbrough 0-0 6.14'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png', 196, 20, 34, 'Cincinnati Reds', 'https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png', 17, 17, 17, 'Pittsburgh Pirates', 'Sat 6:35 PM EDT ', '9-24', '13-19', '', '-116 * -1.5', '-102 * 1.5', 'O/U 8', 'L. Castillo 0-0 5.79', 'Z. Thompson 1-3 7.08'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png', 250, 250, 250, 'Boston Red Sox', 'https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', 250, 250, 250, 'Texas Rangers', 'Sat 7:05 PM EDT on ESPN+', '12-20', '13-18', '', '+102 * -1.5', '-120 * 1.5', 'O/U 8', 'R. Hill 0-1 2.86', 'G. Otto 1-0 3.14'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png', 250, 250, 250, 'Houston Astros', 'https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', 10, 41, 93, 'Washington Nationals', 'Sat 7:05 PM EDT ', '22-11', '11-23', '', '-154 * -1.5', '+130 * 1.5', 'O/U 9', 'C. Javier 2-0 0.83', 'E. Fedde 2-2 3.90'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png', 250, 250, 250, 'Cleveland Guardians', 'https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png', 1, 39, 86, 'Minnesota Twins', 'Sat 7:10 PM EDT ', '15-16', '19-10', '', '-132 * -1.5', '+112 * 1.5', 'O/U 8.5', 'S. Bieber 1-2 4.13', 'D. Smeltzer false-false false'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', 1, 23, 57, 'New York Yankees', 'https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', 27, 21, 22, 'Chicago White Sox', 'Sat 7:10 PM EDT ', '24-8', '15-16', '', '-164 * -1.5', '+138 * 1.5', 'O/U 9.5', 'J. Montgomery 0-1 2.90', 'D. Keuchel 2-3 6.86'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', 1, 42, 91, 'Seattle Mariners', 'https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', 250, 250, 250, 'New York Mets', 'Sat 7:10 PM EDT ', '15-18', '22-12', '', '+140 * 1.5', '-166 * -1.5', 'O/U 7', 'G. Kirby 0-0 0.00', 'C. Bassitt 4-2 2.45'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', 250, 250, 250, 'Chicago Cubs', 'https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', 164, 0, 19, 'Arizona Diamondbacks', 'Sat 8:10 PM EDT ', '11-20', '18-15', '', '+140 * 1.5', '-166 * -1.5', 'O/U 8', 'K. Hendricks 2-3 4.38', 'Z. Gallen 2-0 0.95'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png', 250, 250, 250, 'Kansas City Royals', 'https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png', 34, 13, 72, 'Colorado Rockies', 'Sat 8:10 PM EDT ', '11-19', '16-16', '', '+138 * 1.5', '-164 * -1.5', 'O/U 11.5', 'C. Hernandez 0-2 7.15', 'G. Marquez 0-3 6.47'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'Sat 9:40 PM EDT ', '22-12', '14-20', '', '+118 * 1.5', '-138 * -1.5', 'O/U 7.5', 'M. Lorenzen 3-2 4.13', 'A. Oller 0-2 11.17'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', 190, 0, 17, 'Philadelphia Phillies', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', 250, 250, 250, 'Los Angeles Dodgers', 'Sat 10:10 PM EDT ', '16-17', '20-11', '', '+164 * 1.5', '-196 * -1.5', 'O/U 8', 'R. Suarez 3-1 3.68', 'J. Urias 2-2 2.10'], 'AT&T Byron Nelson • Round 3 - In Progress • 1 Sebastián Muñoz -16 • T2 James Hahn -15 • T2 Jordan Spieth -15 • T2 Joaquin Niemann -15 • T2 Ryan Palmer -15 • T6 Justin Thomas -10 • T6 Mito Pereira -10 • T6 K.H. Lee -10 • T6 Charl Schwartzel -10 • T6 David Skinns -10', 'PARTLY CLOUDY 84° Feels Like 84° High 102° Low 74° • SUN: High 106° Low 73° Rain 0% • MON: High 107° Low 75° Rain 0%', "ASTROSNEWS • Astros pounce for 5-run 1st in 11th straight 'W' • Injuries & Moves: Astros acquire Dubón from SF • Dusty's legacy in DC transcends baseball • ESPNMLB • Being Gabe Kapler: Inside the mind of the San Francisco Giants' nonconformist manager • Astros acquire utilityman Dubón from Giants • Source: Bauer's hearing vs. MLB to begin May 23 • ESPNGOLF • Mickelson opts to withdraw from next week's PGA • Palmer shoots 62, joins lead at Byron Nelson • Lee takes 3-shot lead in LPGA's Founders Cup • ESPNTOPSTORIES • 20 injured in pair of shootings near Bucks' arena • Grizzlies' Brooks to Dubs after loss: We're coming • Former All-Pro safety Thomas arrested in Texas", 'HAPPY BIRTHDAY TAYLOR & RYAN']
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            color = green
            print(responseArr)
            for arr in responseArr:
                running = True
                while running:
                    offscreen_canvas.Clear()
                    buffer = 6
                    pos -= 1
                    offset = 0
                    if isinstance(arr, list):
                        for game in arr:
                            bases =  [[2,5],[6,0],[10,5]]
                            outs = [[3,20],[9,20],[15,20]]
                            awayTeamString = game[5]
                            homeTeamString = game[10]
                            awayTeamStatusString = game[12]
                            homeTeamStatusString = game[13]
                            statusString = game[11]
                            oddsString = game[14]
                            if 'pregame' in game[0]: 
                                offscreen_canvas.SetImage(mlbLogos[game[1]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + mlbLogos[game[1]].width, 24, green, 'vs')
                                offscreen_canvas.SetImage(mlbLogos[game[6]], pos + offset + mlbLogos[game[1]].width + buffer + buffer, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer, 12, white, awayTeamString)
                                awayTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + awayTeam, 12, white, awayTeamStatusString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer, 26, white, homeTeamString)
                                homeTeamStatus = graphics.DrawText(offscreen_canvas, smallestFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + homeTeam, 26, white, homeTeamStatusString)
                                if awayTeam > homeTeam:
                                    gameStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + buffer + awayTeam + awayTeamStatus, 26, green, statusString)
                                    oddsStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + buffer+ awayTeam + awayTeamStatus, 12, green, oddsString)
                                else:
                                    gameStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 26, green, statusString)
                                    oddsStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer + buffer + buffer+ homeTeam + homeTeamStatus, 12, green, oddsString)
                            if 'inProgress' in game[0]: 
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
                                offscreen_canvas.SetImage(mlbLogos[game[1]], pos + offset, -10)
                                versus = graphics.DrawText(offscreen_canvas, middleFont, pos + offset + buffer + mlbLogos[game[1]].width, 24, green, 'vs')
                                offscreen_canvas.SetImage(mlbLogos[game[6]], pos + offset + mlbLogos[game[1]].width + buffer + buffer + buffer + buffer + buffer, -10)
                                awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer, 12, awayColor, awayTeamString)
                                homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width + buffer + buffer + buffer, 26, homeColor, homeTeamString)
                                scoreLocation = 0
                                if (homeTeam > awayTeam):
                                    scoreLocation = homeTeam + buffer + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width
                                else:
                                    scoreLocation = awayTeam + buffer + mlbLogos[game[1]].width + versus + mlbLogos[game[6]].width
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
                            if awayTeam > homeTeam:
                                offset = offset + awayTeam + awayTeamStatus + 240
                            else:
                                offset = offset + homeTeam + homeTeamStatus + 240
                    time.sleep(0.008)
                    else:
                        len = graphics.DrawText(offscreen_canvas, font, pos, 24, color, arr)
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.005)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()