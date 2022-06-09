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
            # COLORS
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            white = graphics.Color(255, 255, 255)
            # END COLORS
            # FONTS
            font = graphics.Font()
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
            alilbiggerFont = graphics.Font()
            alilbiggerFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x7.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            print('getting strings')
            # END FONTS
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            # strings = [['game inProgress mlb', 'https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png', 22, 20, 21, 'San Francisco Giants', 'https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png', 184, 2, 32, 'St. Louis Cardinals', 'Top 1st', '0', '0', 'Top 1st', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/38680.png', 'D. Hudson • 0.0 IP, 0 ER, 0 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/37798.png', 'L. Wade Jr. • 0-0', 'Top 1st', '0-0', 0, 'san-francisco-giants', 'st.-louis-cardinals'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png', 47, 36, 29, 'San Diego Padres', 'https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', 250, 250, 250, 'Atlanta Braves', 'Sat 4:05 PM EDT on FS1', '21-12', '15-18', '', '+118 * 1.5', '-138 * -1.5', 'O/U 8', 'S. Manaea 2-3 3.75', 'C. Morton 2-3 5.65'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'Sat 4:07 PM EDT ', '22-12', '14-20', '', '+118 * 1.5', '-138 * -1.5', 'O/U 7.5', 'J. Diaz 1-0 0.00', 'P. Blackburn 4-0 1.74'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo.png', 32, 27, 27, 'Baltimore Orioles', 'https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png', 250, 250, 250, 'Detroit Tigers', 'Sat 4:10 PM EDT ', '14-19', '10-23', '', '+104 * 1.5', '-122 * -1.5', 'O/U 8', 'B. Zimmermann 2-1 2.67', 'M. Pineda 1-2 3.43'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png', 5, 12, 51, 'Milwaukee Brewers', 'https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png', 250, 250, 250, 'Miami Marlins', 'Sat 6:10 PM EDT ', '21-12', '14-18', '', '-120 * -1.5', '+102 * 1.5', 'O/U 7', 'E. Lauer 3-0 1.82', 'T. Rogers 1-4 5.00'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png', 250, 250, 250, 'Toronto Blue Jays', 'https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', 250, 250, 250, 'Tampa Bay Rays', 'Sat 6:10 PM EDT ', '17-16', '20-13', '', '+102 * 1.5', '-120 * -1.5', 'O/U 8.5', 'H. Ryu 0-0 13.50', 'R. Yarbrough 0-0 6.14'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png', 196, 20, 34, 'Cincinnati Reds', 'https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png', 17, 17, 17, 'Pittsburgh Pirates', 'Sat 6:35 PM EDT ', '9-24', '13-19', '', '-116 * -1.5', '-102 * 1.5', 'O/U 8', 'L. Castillo 0-0 5.79', 'Z. Thompson 1-3 7.08'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png', 250, 250, 250, 'Boston Red Sox', 'https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', 250, 250, 250, 'Texas Rangers', 'Sat 7:05 PM EDT on ESPN+', '12-20', '13-18', '', '+102 * -1.5', '-120 * 1.5', 'O/U 8', 'R. Hill 0-1 2.86', 'G. Otto 1-0 3.14'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png', 250, 250, 250, 'Houston Astros', 'https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', 10, 41, 93, 'Washington Nationals', 'Sat 7:05 PM EDT ', '22-11', '11-23', '', '-154 * -1.5', '+130 * 1.5', 'O/U 9', 'C. Javier 2-0 0.83', 'E. Fedde 2-2 3.90'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png', 250, 250, 250, 'Cleveland Guardians', 'https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png', 1, 39, 86, 'Minnesota Twins', 'Sat 7:10 PM EDT ', '15-16', '19-10', '', '-132 * -1.5', '+112 * 1.5', 'O/U 8.5', 'S. Bieber 1-2 4.13', 'D. Smeltzer false-false false'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', 1, 23, 57, 'New York Yankees', 'https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', 27, 21, 22, 'Chicago White Sox', 'Sat 7:10 PM EDT ', '24-8', '15-16', '', '-164 * -1.5', '+138 * 1.5', 'O/U 9.5', 'J. Montgomery 0-1 2.90', 'D. Keuchel 2-3 6.86'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', 1, 42, 91, 'Seattle Mariners', 'https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', 250, 250, 250, 'New York Mets', 'Sat 7:10 PM EDT ', '15-18', '22-12', '', '+140 * 1.5', '-166 * -1.5', 'O/U 7', 'G. Kirby 0-0 0.00', 'C. Bassitt 4-2 2.45'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', 250, 250, 250, 'Chicago Cubs', 'https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', 164, 0, 19, 'Arizona Diamondbacks', 'Sat 8:10 PM EDT ', '11-20', '18-15', '', '+140 * 1.5', '-166 * -1.5', 'O/U 8', 'K. Hendricks 2-3 4.38', 'Z. Gallen 2-0 0.95'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png', 250, 250, 250, 'Kansas City Royals', 'https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png', 34, 13, 72, 'Colorado Rockies', 'Sat 8:10 PM EDT ', '11-19', '16-16', '', '+138 * 1.5', '-164 * -1.5', 'O/U 11.5', 'C. Hernandez 0-2 7.15', 'G. Marquez 0-3 6.47'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'Sat 9:40 PM EDT ', '22-12', '14-20', '', '+118 * 1.5', '-138 * -1.5', 'O/U 7.5', 'M. Lorenzen 3-2 4.13', 'A. Oller 0-2 11.17'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', 190, 0, 17, 'Philadelphia Phillies', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', 250, 250, 250, 'Los Angeles Dodgers', 'Sat 10:10 PM EDT ', '16-17', '20-11', '', '+164 * 1.5', '-196 * -1.5', 'O/U 8', 'R. Suarez 3-1 3.68', 'J. Urias 2-2 2.10'], 'AT&T Byron Nelson • Round 3 - In Progress • 1 Sebastián Muñoz -16 • T2 James Hahn -15 • T2 Jordan Spieth -15 • T2 Joaquin Niemann -15 • T2 Ryan Palmer -15 • T6 Justin Thomas -10 • T6 Mito Pereira -10 • T6 K.H. Lee -10 • T6 Charl Schwartzel -10 • T6 David Skinns -10', 'PARTLY CLOUDY 84° Feels Like 84° High 102° Low 74° • SUN: High 106° Low 73° Rain 0% • MON: High 107° Low 75° Rain 0%', "ASTROSNEWS • Astros pounce for 5-run 1st in 11th straight 'W' • Injuries & Moves: Astros acquire Dubón from SF • Dusty's legacy in DC transcends baseball • ESPNMLB • Being Gabe Kapler: Inside the mind of the San Francisco Giants' nonconformist manager • Astros acquire utilityman Dubón from Giants • Source: Bauer's hearing vs. MLB to begin May 23 • ESPNGOLF • Mickelson opts to withdraw from next week's PGA • Palmer shoots 62, joins lead at Byron Nelson • Lee takes 3-shot lead in LPGA's Founders Cup • ESPNTOPSTORIES • 20 injured in pair of shootings near Bucks' arena • Grizzlies' Brooks to Dubs after loss: We're coming • Former All-Pro safety Thomas arrested in Texas", 'HAPPY BIRTHDAY TAYLOR & RYAN']
            print(strings)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            # IMAGES FOR WEATHER
            partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            # END IMAGES FOR WEATHER
            print(strings)
            for string in strings:
                running = True
                color = green
                print('=======================')
                print(string)
                if string == None:
                    print('it was NONE')
                elif isinstance(string, list) and 'inProgress mlb' in string[0]:
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                    pitcherHeadshot = string[16]
                    batterHeadshot = string[18]
                    pitcherImage = Image.open(requests.get(pitcherHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    batterImage = Image.open(requests.get(batterHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                elif isinstance(string, list) and 'nba' in string[0]:
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                    pitcherHeadshot = string[16]
                    batterHeadshot = string[18]
                    pitcherImage = Image.open(requests.get(pitcherHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    batterImage = Image.open(requests.get(batterHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                elif isinstance(string, list) and 'game' in string[0]:
                    print(string[1])
                    print(string[6])
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((50,50), Image.ANTIALIAS)
                elif isinstance(string, list) and 'http' in string[0]:
                    if '-' in string[3]:
                        color = red
                    elif '+' in string[3]:
                        color = green
                    stockLogo = Image.open(requests.get(string[0], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    stockDown = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/stocks/icons8-down-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                    stockUp = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/stocks/icons8-up-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                len = 1
                while running:
                    offscreen_canvas.Clear()
                    if 'RAIN' in string:
                        color = blue
                        img_width, img_height = rainImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(rainImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + rainImage.width, 24, color, string)
                        time.sleep(0.005)
                    elif 'CLOUDY' in string or 'OVERCAST' in string:
                        color = blue
                        img_width, img_height = partlyCloudyImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(partlyCloudyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + partlyCloudyImage.width, 24, color, string)
                        time.sleep(0.005)
                    elif 'THUNDER' in string:
                        color = purple
                        img_width, img_height = thunderstormImage.size
                        pos -= 1
                        if (pos + thunderstormImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(thunderstormImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + thunderstormImage.width, 24, color, string)
                        time.sleep(0.005)
                    elif 'SUN' in string:
                        color = yellow
                        img_width, img_height = sunnyImage.size
                        pos -= 1
                        if (pos + sunnyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(sunnyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + sunnyImage.width, 24, color, string)
                        time.sleep(0.005)
                    elif isinstance(string, list) and 'game' in string[0]:
                        # awayColor = graphics.Color(string[2], string[3], string[4])
                        # homeColor = graphics.Color(string[7], string[8], string[9])
                        awayTeamString = string[5]
                        homeTeamString = string[10]
                        awayTeamStatusString = string[12]
                        homeTeamStatusString = string[13]
                        statusString = string[11]
                        oddsString = string[14]
                        versusString = ' at '
                        pos -= 1
                        buffer = 6
                        bases =  [[2,5],[6,0],[10,5]]
                        outs = [[3,20],[9,20],[15,20]]
                        if 'pregame' in string[0]:     
                            offscreen_canvas.SetImage(awayLogo, pos, -10)
                            versus = graphics.DrawText(offscreen_canvas, middleFont, pos + buffer + awayLogo.width, 24, green, versusString)
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer, -10)
                            awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width + buffer, 10, white, awayTeamString)
                            awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + awayTeam, 10, white, awayTeamStatusString)
                            homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width + buffer, 26, white, homeTeamString)
                            homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + homeTeam, 26, white, homeTeamStatusString)
                            odds = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + awayTeam, 10, green, oddsString)
                            status = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + homeTeam, 26, green, statusString)
                            if (pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + status < 0):
                                running = False
                                pos = offscreen_canvas.width
                        elif 'inProgress mlb' in string[0]:
                            runnerSituationString = string[15]
                            pitcherNameString = string[17]
                            batterNameString = string[19]
                            inningString = string[20]
                            countString = string[21]
                            outsString = string[22]
                            if int(awayTeamStatusString) < int(homeTeamStatusString):
                                homeColor = green
                                awayColor = red
                            elif int(awayTeamStatusString) == int(homeTeamStatusString):
                                homeColor = yellow
                                awayColor = yellow
                            else:
                                homeColor = red
                                awayColor = green
                            if 'Bases Loaded' in runnerSituationString:
                                runnersColor = green
                            else:
                                runnersColor = yellow
                            runningTotal = 0
                            offscreen_canvas.SetImage(awayLogo, pos, -10)
                            versus = graphics.DrawText(offscreen_canvas, middleFont, pos + buffer + awayLogo.width, 24, yellow, 'VS')
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + versus, -10)
                            awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer, 12, awayColor, awayTeamString)
                            homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer, 26, homeColor, homeTeamString)
                            scoreLocation = 0
                            if (homeTeam > awayTeam):
                                scoreLocation = homeTeam + buffer
                            else:
                                scoreLocation = awayTeam + buffer
                            awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer + scoreLocation + buffer, 12, awayColor, awayTeamStatusString)
                            homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer + scoreLocation + buffer, 26, homeColor, homeTeamStatusString)
                            runningTotal = awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer + scoreLocation + buffer + buffer + awayTeamStatus + buffer
                            baseSize = 6
                            outsSize = 4
                            baseHalf = abs(baseSize/2)
                            outsHalf = abs(outsSize/2)
                            for base in bases:
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + base[0] + baseHalf, base[1], pos + runningTotal + base[0], base[1]+ baseHalf, yellow)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + base[0] + baseHalf, base[1], pos + runningTotal + base[0] + baseSize, base[1]+ baseHalf, yellow)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + base[0] + baseHalf, base[1]+ baseSize, pos + runningTotal + base[0], base[1]+ baseHalf, yellow)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + base[0] + baseHalf, base[1]+ baseSize, pos + runningTotal + base[0] + baseSize, base[1]+ baseHalf, yellow)
                            for out in outs:
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + out[0], out[1], pos + runningTotal + out[0] + outsSize, out[1], red)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + out[0], out[1], pos + runningTotal + out[0], out[1] + outsSize, red)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + out[0] + outsSize, out[1] + outsSize, pos + runningTotal + out[0], out[1] + outsSize, red)
                                graphics.DrawLine(offscreen_canvas, pos + runningTotal + out[0] + outsSize, out[1] + outsSize, pos + runningTotal + out[0] + outsSize, out[1], red)
                            if '1st' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                x = bases[0][0]
                                y = bases[0][1]
                                size = 6
                                half = round(abs(size/2))
                                for offset in range(1, half + 1):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + size - offset, pos + runningTotal + x + half + offset, y + size - offset, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + offset, pos + runningTotal + x + half + offset, y + offset, yellow)
                            if '2nd' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                x = bases[1][0]
                                y = bases[1][1]
                                size = 6
                                half = round(abs(size/2))
                                for offset in range(1, half + 1):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + size - offset, pos + runningTotal + x + half + offset, y + size - offset, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + offset, pos + runningTotal + x + half + offset, y + offset, yellow)
                            if '3rd' in runnerSituationString or 'Bases Loaded' in runnerSituationString:
                                x = bases[2][0]
                                y = bases[2][1]
                                size = 6
                                half = round(abs(size/2))
                                for offset in range(1, half + 1):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + size - offset, pos + runningTotal + x + half + offset, y + size - offset, yellow)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + x + half - offset, y + offset, pos + runningTotal + x + half + offset, y + offset, yellow)
                            if outsString == 1:
                                for y_offset in range(outsSize):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[0][0], pos + runningTotal + outs[0][1] + y_offset, pos + runningTotal + outs[0][0] + outsSize, pos + runningTotal + outs[0][1] + y_offset, red)
                            elif outsString == 2:
                                for y_offset in range(outsSize):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[0][0], pos + runningTotal + outs[0][1] + y_offset, pos + runningTotal + outs[0][0] + outsSize, pos + runningTotal + outs[0][1] + y_offset, red)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[1][0], pos + runningTotal + outs[1][1] + y_offset, pos + runningTotal + outs[1][0] + outsSize, pos + runningTotal + outs[1][1] + y_offset, red)
                            elif outsString == 3:
                                for y_offset in range(outsSize):
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[0][0], pos + runningTotal + outs[0][1] + y_offset, pos + runningTotal + outs[0][0] + outsSize, pos + runningTotal + outs[0][1] + y_offset, red)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[1][0], pos + runningTotal + outs[1][1] + y_offset, pos + runningTotal + outs[1][0] + outsSize, pos + runningTotal + outs[1][1] + y_offset, red)
                                    graphics.DrawLine(offscreen_canvas, pos + runningTotal + outs[2][0], pos + runningTotal + outs[2][1] + y_offset, pos + runningTotal + outs[2][0] + outsSize, pos + runningTotal + outs[2][1] + y_offset, red)
                            situation = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos + runningTotal + 3, 19, yellow, countString)
                            inning = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos + runningTotal - 5, 31, yellow, inningString)
                            if (pos + runningTotal < 0):
                                running = False
                                pos = offscreen_canvas.width
                        else:
                            if awayTeamStatusString == '':
                                homeColor = yellow
                                awayColor = yellow
                            elif int(awayTeamStatusString) < int(homeTeamStatusString):
                                homeColor = green
                                awayColor = red
                            elif int(awayTeamStatusString) == int(homeTeamStatusString):
                                homeColor = yellow
                                awayColor = yellow
                            else:
                                homeColor = red
                                awayColor = green
                            offscreen_canvas.SetImage(awayLogo, pos, -10)
                            versus = graphics.DrawText(offscreen_canvas, middleFont, pos + buffer + awayLogo.width, 24, yellow, 'VS')
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + versus, -10)
                            awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer, 12, awayColor, awayTeamString)
                            homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer, 26, homeColor, homeTeamString)
                            scoreLocation = 0
                            if (homeTeam > awayTeam):
                                scoreLocation = homeTeam + buffer
                            else:
                                scoreLocation = awayTeam + buffer
                            awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer + scoreLocation + buffer, 12, awayColor, awayTeamStatusString)
                            homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + versus + buffer + homeLogo.width + buffer + scoreLocation + buffer, 26, homeColor, homeTeamStatusString)
                            if 'HALF' in oddsString:
                                quarter = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + versus + homeLogo.width + scoreLocation + homeTeamStatus + buffer + buffer + buffer + buffer + buffer, 12, yellow, oddsString)
                            else:
                                quarter = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + versus + homeLogo.width + scoreLocation + homeTeamStatus + buffer + buffer + buffer + buffer + buffer, 12, yellow, oddsString)
                            status = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + versus + homeLogo.width + scoreLocation + homeTeamStatus + buffer + buffer + buffer + buffer + buffer, 26, yellow, statusString)
                            if (pos + awayLogo.width + buffer + buffer + versus + status + buffer + homeLogo.width + scoreLocation + buffer + quarter < 0):
                                running = False
                                pos = offscreen_canvas.width
                        time.sleep(0.01)
                    elif isinstance(string, list):
                        if '-' in string[4]:
                            pos -= 1
                            offscreen_canvas.SetImage(stockLogo, pos)
                            first = graphics.DrawText(offscreen_canvas, font, pos + 35, 24, red, string[1])
                            second = graphics.DrawText(offscreen_canvas, font, pos + 45 + first, 24, red, string[2])
                            offscreen_canvas.SetImage(stockDown, pos + 60 + first + second, 8)
                            third = graphics.DrawText(offscreen_canvas, font, pos + 70 + first + second + 20, 24, red, string[3])
                            if ( pos + 45 + first + second + 65 + third < 0):
                                running = False
                                pos = offscreen_canvas.width
                            time.sleep(0.005)
                        elif '+' in string[4]:
                            pos -= 1
                            offscreen_canvas.SetImage(stockLogo, pos)
                            first = graphics.DrawText(offscreen_canvas, font, pos + 35, 24, green, string[1])
                            second = graphics.DrawText(offscreen_canvas, font, pos + 45 + first, 24, green, string[2])
                            offscreen_canvas.SetImage(stockUp, pos + 60 + first + second, 8)
                            third = graphics.DrawText(offscreen_canvas, font, pos + 70 + first + second + 20, 24, green, string[3])
                            if ( pos + 45 + first + second + 65 + third < 0):
                                running = False
                                pos = offscreen_canvas.width
                            time.sleep(0.005)
                    elif 'AP Poll' in string:
                        color = green
                        basketballLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + basketballLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(basketballLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + basketballLogo.width + 4, 24, color, string)
                        time.sleep(0.005)
                    elif 'ESPN' in string:
                        color = blue
                        espnLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + espnLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(espnLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + espnLogo.width + 4, 24, color, string)
                        time.sleep(0.005)
                    elif 'FOXNEWS' in string:
                        color = blue
                        foxNewsLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/foxnews.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + foxNewsLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(foxNewsLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + foxNewsLogo.width + 4, 24, color, string)
                        time.sleep(0.005)
                    elif 'CNN' in string:
                        color = blue
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        len = graphics.DrawText(offscreen_canvas, font, pos + 4, 24, color, string)
                        time.sleep(0.005)
                    else:
                        len = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
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

        # elif isinstance(string, list) and 'game' in string[0]:
                    #     if 'BAYLOR' in string[5]:
                    #         awayColor = green
                    #     else:
                    #         awayColor = graphics.Color(string[2], string[3], string[4])
                    #     if 'BAYLOR' in string[10]:
                    #         homeColor = green
                    #     else:
                    #         homeColor = graphics.Color(string[7], string[8], string[9])
                    #     awayTeamString = string[5]
                    #     homeTeamString = string[10]
                    #     awayTeamStatusString = string[12]
                    #     homeTeamStatusString = string[13]
                    #     statusString = string[11]
                    #     oddsString = string[14]
                    #     versusString = ' at '
                    #     pos -= 1
                    #     buffer = 6
                    #     if 'pregame' in string[0]:                            
                    #         offscreen_canvas.SetImage(awayLogo, pos)
                    #         awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer, 10, awayColor, awayTeamString)
                    #         awayCentered = awayTeam / 2 - 5
                    #         awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + awayCentered, 26, awayColor, awayTeamStatusString)
                    #         versus = graphics.DrawText(offscreen_canvas, middleFont, pos + buffer + awayLogo.width + awayTeam, 24, green, versusString)
                    #         offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + awayTeam + versus)
                    #         homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width, 10, homeColor, homeTeamString)
                    #         homeCentered = homeTeam / 2 - 5
                    #         homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeCentered, 26, homeColor, homeTeamStatusString)
                    #         odds = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeTeam + buffer, 15, green, oddsString)
                    #         status = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeTeam + buffer, 26, green, statusString)
                    #         if (pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + status < 0):
                    #             running = False
                    #             pos = offscreen_canvas.width
                    #     else:
                    #         offscreen_canvas.SetImage(awayLogo, pos)
                    #         awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer, 10, awayColor, awayTeamString)
                    #         awayCentered = awayTeam / 3
                    #         awayTeamStatus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + awayCentered, 31, awayColor, awayTeamStatusString)
                    #         if 'HALF' in oddsString:
                    #             quarter = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + awayTeam, 12, green, oddsString)
                    #         else:
                    #             quarter = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + awayTeam + 4, 12, green, oddsString)
                    #         status = graphics.DrawText(offscreen_canvas, middleFont, pos + awayLogo.width + buffer + buffer + awayTeam, 26, green, statusString)
                    #         offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + awayTeam + quarter + buffer + buffer + buffer)
                    #         homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + buffer + buffer + buffer + homeLogo.width, 10, homeColor, homeTeamString)
                    #         homeCentered = homeTeam / 2
                    #         homeTeamStatus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + homeLogo.width + homeCentered, 31, homeColor, homeTeamStatusString)
                    #         if (pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + quarter < 0):
                    #             running = False
                    #             pos = offscreen_canvas.width
                    #     time.sleep(0.01)
                    # elif isinstance(string, list) and 'game' in string[0]:
                    #     awayColor = graphics.Color(string[2], string[3], string[4])
                    #     homeColor = graphics.Color(string[7], string[8], string[9])
                    #     awayTeamString = string[5]
                    #     homeTeamString = string[10]
                    #     statusString = string[11]
                    #     versusString = ' vs '
                    #     pos -= 1
                    #     # away team logo
                    #     offscreen_canvas.SetImage(awayLogo, pos)
                    #     # away team string
                    #     awayTeam = graphics.DrawText(offscreen_canvas, font, 15 + pos + 35, 24, awayColor, awayTeamString)
                    #     # versus
                    #     versus = graphics.DrawText(offscreen_canvas, middleFont, 25 + pos + 35 + awayTeam, 24, green, versusString)
                    #     # home team logo
                    #     offscreen_canvas.SetImage(homeLogo, 30 + pos + 35 + awayTeam + versus)
                    #     # home team string
                    #     homeTeam = graphics.DrawText(offscreen_canvas, font, 35 + pos + 35 + awayTeam + 35 + versus, 24, homeColor, homeTeamString)
                    #     # game time
                    #     status = graphics.DrawText(offscreen_canvas, font, 80 + pos + 45 + awayTeam + 35 + homeTeam, 24, blue, statusString)
                    #     if (60 + pos + 45 + awayTeam + 35 + homeTeam + status + versus < 0):
                    #         running = False
                    #         pos = offscreen_canvas.width
                    #     time.sleep(0.01)