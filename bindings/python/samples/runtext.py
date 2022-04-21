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
            # END FONTS
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            # strings = json.loads(url.text)
            strings = [['game inprogress mlb', 'https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png', 250, 250, 250, 'Boston Red Sox', 'https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png', 1, 23, 57, 'New York Yankees', 'Bot 8th', '4', '3', 'Bottom 8th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/39674.png', 'G. Whitlock • 2.1 IP, 0 ER, H, 4 K, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/30765.png', 'D. LeMahieu • 0-2, BB', 'Bot 8th', '1-2', 1, 'boston-red-sox', 'new-york-yankees'], ['game inprogress mlb', 'https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png', 27, 21, 22, 'Chicago White Sox', 'https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png', 250, 250, 250, 'Detroit Tigers', 'Bot 8th', '3', '1', 'Bottom 8th', 'Bases Empty', 'https://a.espncdn.com/i/headshots/mlb/players/full/36131.png', 'A. Bummer • 0.0 IP, 0 ER, 0 H, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/33452.png', 'E. Haase • 0-0', 'Bot 8th', '0-0', 0, 'chicago-white-sox', 'detroit-tigers'], ['game postponed mlb', 'https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png', 5, 12, 51, 'Milwaukee Brewers', 'https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png', 250, 250, 250, 'Chicago Cubs', '', '', '', 'Postponed'], ['game inprogress mlb', 'https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png', 1, 67, 38, 'Oakland Athletics', 'https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png', 190, 0, 17, 'Philadelphia Phillies', 'Top 3rd', '0', '1', 'Top 3rd', 'Runner on 1st', 'https://a.espncdn.com/i/headshots/mlb/players/full/33709.png', 'A. Nola • 2.2 IP, 0 ER, 0 H, K, 0 BB', 'https://a.espncdn.com/i/headshots/mlb/players/full/34083.png', 'T. Kemp • 0-1', 'Top 3rd', '2-2', 2, 'oakland-athletics', 'philadelphia-phillies'], ['game inprogress mlb', 'https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png', 32, 27, 27, 'Baltimore Orioles', 'https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png', 250, 250, 250, 'Tampa Bay Rays', 'End 2nd', '0', '0', 'End 2nd', 'Bases Empty', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'https://a.espncdn.com/i/headshots/nophoto.png', 'undefined • undefined', 'End 2nd', '0-0', 0, 'baltimore-orioles', 'tampa-bay-rays'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png', 250, 250, 250, 'Los Angeles Dodgers', 'https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png', 34, 13, 72, 'Colorado Rockies', 'Fri 4:10 PM EDT ', '0-0', '0-0', '', '-210 * -1.5', '+176 * 1.5', 'O/U 11.5'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png', 1, 42, 91, 'Seattle Mariners', 'https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png', 1, 39, 86, 'Minnesota Twins', 'Fri 4:10 PM EDT ', '0-0', '0-0', '', '+100 * -1.5', '-118 * 1.5', 'O/U 8'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png', 250, 250, 250, 'Miami Marlins', 'https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png', 22, 20, 21, 'San Francisco Giants', 'Fri 4:35 PM EDT ', '0-0', '0-0', '', '+130 * 1.5', '-154 * -1.5', 'O/U 7.5'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png', 250, 250, 250, 'New York Mets', 'https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png', 10, 41, 93, 'Washington Nationals', 'Fri 7:05 PM EDT on Apple TV+', '1-0', '0-1', '', '-168 * -1.5', '+140 * 1.5', 'O/U 8.5'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png', 250, 250, 250, 'Texas Rangers', 'https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png', 250, 250, 250, 'Toronto Blue Jays', 'Fri 7:07 PM EDT ', '0-0', '0-0', '', '+140 * 1.5', '-166 * -1.5', 'O/U 9'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png', 196, 20, 34, 'Cincinnati Reds', 'https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png', 250, 250, 250, 'Atlanta Braves', 'Fri 7:20 PM EDT ', '1-0', '0-1', '', '+164 * 1.5', '-196 * -1.5', 'O/U 8.5'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png', 250, 250, 250, 'Houston Astros', 'https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png', 165, 0, 23, 'Los Angeles Angels', 'Fri 9:38 PM EDT on Apple TV+', '1-0', '0-1', '', '+108 * 1.5', '-126 * -1.5', 'O/U 9.5'], ['game pregame mlb', 'https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png', 47, 36, 29, 'San Diego Padres', 'https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png', 164, 0, 19, 'Arizona Diamondbacks', 'Fri 9:40 PM EDT ', '0-1', '1-0', '', '-136 * -1.5', '+116 * 1.5', 'O/U 9'], 'Masters Tournament • Round 2 - In Progress • T1 Charl Schwartzel -3 • T1 Sungjae Im -3 • T1 Danny Willett -3 • T4 Harold Varner III -2 • T4 Dustin Johnson -2 • T4 Talor Gooch -2 • T4 Cameron Smith -2 • T4 Joaquin Niemann -2 • T4 Hideki Matsuyama -2 • T4 Scottie Scheffler -2', ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-milwaukee-bucks-logo.png', 250, 250, 250, 'Milwaukee Bucks', 'https://loodibee.com/wp-content/uploads/nba-detroit-pistons-logo.png', 250, 0, 44, 'Detroit Pistons', 'Fri 7:00 PM EDT on NBA TV', '50-30', '23-57', '', '-235 * -5.5', '+194 * 5.5', 'O/U 228.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-new-york-knicks-logo.png', 34, 94, 168, 'New York Knicks', 'https://loodibee.com/wp-content/uploads/nba-washington-wizards-logo.png', 14, 55, 100, 'Washington Wizards', 'Fri 7:00 PM EDT ', '35-45', '35-45', '', '-162 * -3.5', '+136 * 3.5', 'O/U 224'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-cleveland-cavaliers-logo.png', 6, 22, 66, 'Cleveland Cavaliers', 'https://loodibee.com/wp-content/uploads/nba-brooklyn-nets-logo.png', 250, 250, 250, 'Brooklyn Nets', 'Fri 7:30 PM EDT ', '43-37', '42-38', '', '+280 * 8.5', '-350 * -8.5', 'O/U 232.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-houston-rockets-logo.png', 212, 0, 38, 'Houston Rockets', 'https://loodibee.com/wp-content/uploads/nba-toronto-raptors-logo.png', 206, 15, 65, 'Toronto Raptors', 'Fri 7:30 PM EDT ', '20-60', '47-33', '', '+540 * 12', '-770 * -12', 'O/U 227.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-atlanta-hawks-logo.png', 250, 250, 250, 'Atlanta Hawks', 'https://loodibee.com/wp-content/uploads/nba-miami-heat-logo.png', 250, 250, 250, 'Miami Heat', 'Fri 8:00 PM EDT ', '42-38', '52-28', '', '-130 * -2', '+110 * 2', 'O/U 230.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-charlotte-hornets-logo.png', 29, 16, 96, 'Charlotte Hornets', 'https://loodibee.com/wp-content/uploads/nba-chicago-bulls-logo.png', 250, 250, 250, 'Chicago Bulls', 'Fri 8:00 PM EDT ', '41-39', '45-35', '', '+120 * 2.5', '-142 * -2.5', 'O/U 235.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-portland-trail-blazers-logo.png', 250, 250, 250, 'Portland Trail Blazers', 'https://loodibee.com/wp-content/uploads/nba-dallas-mavericks-logo.png', 12, 71, 157, 'Dallas Mavericks', 'Fri 8:30 PM EDT ', '27-53', '50-30', '', '+1500 * 19.5', '-4000 * -19.5', 'O/U 220.5'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-phoenix-suns-logo.png', 35, 0, 106, 'Phoenix Suns', 'https://loodibee.com/wp-content/uploads/nba-utah-jazz-logo.png', 6, 20, 63, 'Utah Jazz', 'Fri 9:30 PM EDT on NBA TV', '63-17', '48-32', '', '+118 * 2.5', '-138 * -2.5', 'O/U 228'], ['game pregame nba', 'https://loodibee.com/wp-content/uploads/nba-oklahoma-city-thunder-logo.png', 198, 124, 3, 'Oklahoma City Thunder', 'https://loodibee.com/wp-content/uploads/nba-los-angeles-lakers-logo.png', 84, 37, 130, 'Los Angeles Lakers', 'Fri 10:30 PM EDT ', '24-56', '31-49', '', '+184 * 5', '-220 * -5', 'O/U 225.5'], ['https://logo.clearbit.com/tesla.com', 'TSLA', '1026.13', '-2.94%', 'TSLA 1026.13 -2.94%'], ['https://logo.clearbit.com/originbank.com', 'OBNK', '40.19', '-0.64%', 'OBNK 40.19 -0.64%'], ['https://logo.clearbit.com/stem.com', 'STEM', '10.20', '-4.00%', 'STEM 10.20 -4.00%'], ['https://logo.clearbit.com/apple.com', 'AAPL', '170.12', '-1.18%', 'AAPL 170.12 -1.18%'], ['', 'AMC', '18.18', '-7.83%', 'AMC 18.18 -7.83%'], ['', 'AMD', '100.91', '-2.71%', 'AMD 100.91 -2.71%'], ['', 'HOOD', '11.26', '-6.74%', 'HOOD 11.26 -6.74%'], 'SUNNY 74° Feels Like 73° High 78° Low 55° • SAT: High 87° Low 55° Rain 0% • SUN: High 80° Low 64° Rain 77%', '', 'HELLLLLLLLOOOOO']
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
                elif isinstance(string, list) and 'inprogress mlb' in string[0]:
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
                    pitcherHeadshot = string[16]
                    batterHeadshot = string[18]
                    pitcherImage = Image.open(requests.get(pitcherHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    batterImage = Image.open(requests.get(batterHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                elif isinstance(string, list) and 'nba' in string[0]:
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
                    pitcherHeadshot = string[16]
                    batterHeadshot = string[18]
                    pitcherImage = Image.open(requests.get(pitcherHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    batterImage = Image.open(requests.get(batterHeadshot, stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                elif isinstance(string, list) and 'game' in string[0]:
                    print(string[1])
                    print(string[6])
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((64,64), Image.ANTIALIAS)
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
                        time.sleep(0.008)
                    elif 'CLOUDY' in string or 'OVERCAST' in string:
                        color = blue
                        img_width, img_height = partlyCloudyImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(partlyCloudyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + partlyCloudyImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif 'THUNDER' in string:
                        color = purple
                        img_width, img_height = thunderstormImage.size
                        pos -= 1
                        if (pos + thunderstormImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(thunderstormImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + thunderstormImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif 'SUN' in string:
                        color = yellow
                        img_width, img_height = sunnyImage.size
                        pos -= 1
                        if (pos + sunnyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(sunnyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + sunnyImage.width, 24, color, string)
                        time.sleep(0.008)
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
                            offscreen_canvas.SetImage(awayLogo, pos, -20)
                            versus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer, 24, green, versusString)
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + versus + buffer, -20)
                            awayTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width + buffer, 10, white, awayTeamString)
                            awayTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + awayTeam, 10, white, awayTeamStatusString)
                            homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width + buffer, 26, white, homeTeamString)
                            homeTeamStatus = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + homeTeam, 26, white, homeTeamStatusString)
                            odds = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + awayTeam, 10, green, oddsString)
                            status = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + versus + buffer + homeLogo.width+ buffer + homeTeam, 26, green, statusString)
                            if (pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + status < 0):
                                running = False
                                pos = offscreen_canvas.width
                        elif 'inprogress mlb' in string[0]:
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
                            offscreen_canvas.SetImage(awayLogo, pos, -20)
                            versus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + buffer, 24, yellow, 'VS')
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + buffer + versus, -20)
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
                            runningTotal = runningTotal + inning + 5 + buffer        
                            pitcherTitle = graphics.DrawText(offscreen_canvas, smallFont, pos + runningTotal, 12, white, 'Pitcher: {}'.format(pitcherNameString))
                            batterTitle = graphics.DrawText(offscreen_canvas, smallFont, pos + runningTotal, 26, white, 'Batter: {}'.format(batterNameString))
                            runningTotal = runningTotal + pitcherTitle
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
                            offscreen_canvas.SetImage(awayLogo, pos, -20)
                            versus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + buffer, 24, yellow, 'VS')
                            offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + buffer + versus, -20)
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
                        time.sleep(0.008)
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
                    #         versus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + buffer + awayTeam, 24, green, versusString)
                    #         offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + awayTeam + versus)
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
                    #         offscreen_canvas.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + buffer + buffer)
                    #         homeTeam = graphics.DrawText(offscreen_canvas, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + buffer + buffer + buffer + homeLogo.width, 10, homeColor, homeTeamString)
                    #         homeCentered = homeTeam / 2
                    #         homeTeamStatus = graphics.DrawText(offscreen_canvas, font, pos + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + homeLogo.width + homeCentered, 31, homeColor, homeTeamStatusString)
                    #         if (pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + quarter < 0):
                    #             running = False
                    #             pos = offscreen_canvas.width
                    #     time.sleep(0.008)
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
                    #     versus = graphics.DrawText(offscreen_canvas, font, 25 + pos + 35 + awayTeam, 24, green, versusString)
                    #     # home team logo
                    #     offscreen_canvas.SetImage(homeLogo, 30 + pos + 35 + awayTeam + versus)
                    #     # home team string
                    #     homeTeam = graphics.DrawText(offscreen_canvas, font, 35 + pos + 35 + awayTeam + 35 + versus, 24, homeColor, homeTeamString)
                    #     # game time
                    #     status = graphics.DrawText(offscreen_canvas, font, 80 + pos + 45 + awayTeam + 35 + homeTeam, 24, blue, statusString)
                    #     if (60 + pos + 45 + awayTeam + 35 + homeTeam + status + versus < 0):
                    #         running = False
                    #         pos = offscreen_canvas.width
                    #     time.sleep(0.008)
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
                            time.sleep(0.008)
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
                            time.sleep(0.008)
                    elif 'AP Poll' in string:
                        color = green
                        basketballLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + basketballLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(basketballLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + basketballLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'ESPN' in string:
                        color = blue
                        espnLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + espnLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(espnLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + espnLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'FOXNEWS' in string:
                        color = blue
                        foxNewsLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/foxnews.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + foxNewsLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(foxNewsLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + foxNewsLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'CNN' in string:
                        color = blue
                        cnnLogo = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/cnn.png').convert('RGB').resize((69,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + cnnLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(cnnLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + cnnLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    else:
                        len = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.008)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()