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
            lightblue = graphics.Color(173,216,230)
            teal = graphics.Color(0, 255, 255)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            white = graphics.Color(255, 255, 255)
            black = graphics.Color(0, 0, 0)
            font = graphics.Font()
            font.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallestFont = graphics.Font()
            smallestFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/4x6.bdf")
            alilbiggerFont = graphics.Font()
            alilbiggerFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/5x7.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            # responseArr = json.loads(url.text)
            responseArr = [{'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Phillies', 'name': 'PHI', 'score': '9', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '10'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [190, 0, 17], 'secondary': [40, 72, 152]}, 'record': '8-1'}, 'homeTeam': {'teamName': 'Rays', 'name': 'TB', 'score': '2', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '3'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [143, 188, 230]}, 'record': '10-7'}, 'winningPitcher': 'R. Suarez 1-1', 'losingPitcher': 'L. Patino 1-1', 'finalDetail': 'Final'},{'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Mavericks', 'name': 'DAL', 'colors': {'main': [12, 71, 157], 'secondary': [196, 206, 211]}, 'record': '27-12'}, 'homeTeam': {'teamName': 'Pistons', 'name': 'DET', 'colors': {'main': [250, 0, 44], 'secondary': [250, 250, 250]}, 'record': '49-30'}, 'startTime': '7:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Detroit Pistons', 'price': 310}, 'away': {'name': 'Dallas Mavericks', 'price': -390}}, 'spread': {'home': {'name': 'Detroit Pistons', 'price': -110, 'point': 8.5}, 'away': {'name': 'Dallas Mavericks', 'price': -110, 'point': -8.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 218.5}, 'under': {'name': 'Under', 'price': -110, 'point': 218.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Nets', 'name': 'BKN', 'colors': {'main': [250, 250, 250], 'secondary': [255, 255, 255]}, 'record': '18-21'}, 'homeTeam': {'teamName': 'Knicks', 'name': 'NY', 'colors': {'main': [34, 94, 168], 'secondary': [245, 132, 38]}, 'record': '41-38'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'New York Knicks', 'price': 184}, 'away': {'name': 'Brooklyn Nets', 'price': -220}}, 'spread': {'home': {'name': 'New York Knicks', 'price': -110, 'point': 5}, 'away': {'name': 'Brooklyn Nets', 'price': -110, 'point': -5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 229.5}, 'under': {'name': 'Under', 'price': -110, 'point': 229.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Wizards', 'name': 'WSH', 'colors': {'main': [14, 55, 100], 'secondary': [227, 24, 55]}, 'record': '21-19'}, 'homeTeam': {'teamName': 'Hawks', 'name': 'ATL', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '35-44'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Atlanta Hawks', 'price': -590}, 'away': {'name': 'Washington Wizards', 'price': 410}}, 'spread': {'home': {'name': 'Atlanta Hawks', 'price': -110, 'point': -10.5}, 'away': {'name': 'Washington Wizards', 'price': -110, 'point': 10.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 234}, 'under': {'name': 'Under', 'price': -110, 'point': 234}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Celtics', 'name': 'BOS', 'colors': {'main': [250, 250, 250], 'secondary': [241, 242, 243]}, 'record': '28-13'}, 'homeTeam': {'teamName': 'Bulls', 'name': 'CHI', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '49-30'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Chicago Bulls', 'price': 235}, 'away': {'name': 'Boston Celtics', 'price': -290}}, 'spread': {'home': {'name': 'Chicago Bulls', 'price': -108, 'point': 7}, 'away': {'name': 'Boston Celtics', 'price': -112, 'point': -7}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 224.5}, 'under': {'name': 'Under', 'price': -110, 'point': 224.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Thunder', 'name': 'OKC', 'colors': {'main': [198, 124, 3], 'secondary': [240, 81, 51]}, 'record': '12-29'}, 'homeTeam': {'teamName': 'Jazz', 'name': 'UTAH', 'colors': {'main': [6, 20, 63], 'secondary': [249, 160, 27]}, 'record': '24-55'}, 'startTime': '9:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Utah Jazz', 'price': -1600}, 'away': {'name': 'Oklahoma City Thunder', 'price': 900}}, 'spread': {'home': {'name': 'Utah Jazz', 'price': -108, 'point': -15.5}, 'away': {'name': 'Oklahoma City Thunder', 'price': -112, 'point': 15.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 216}, 'under': {'name': 'Under', 'price': -110, 'point': 216}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Suns', 'name': 'PHX', 'colors': {'main': [35, 0, 106], 'secondary': [241, 242, 243]}, 'record': '32-8'}, 'homeTeam': {'teamName': 'Clippers', 'name': 'LAC', 'colors': {'main': [250, 0, 40], 'secondary': [241, 242, 243]}, 'record': '63-16'}, 'startTime': '10:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'price': ''}, 'away': {'price': ''}}, 'spread': {'home': {'price': ''}, 'away': {'price': ''}}, 'totals': {'over': {'price': ''}, 'under': {'price': ''}}}}]
            print(responseArr)
            canvas = self.matrix
            bases =  [[113,5],[108,0],[103,5]]
            outs = [[103,20],[109,20],[115,20]]
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            for item in responseArr:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(item)
                if type(item) is dict and 'league' in item.keys() and item['league'] == 'mlb':
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:
                        awayMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['away']['price']) if item['fanDuel']['moneyLine']['away']['price'] > 0 else item['fanDuel']['moneyLine']['away']['price']
                        homeMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['home']['price']) if item['fanDuel']['moneyLine']['home']['price'] > 0 else item['fanDuel']['moneyLine']['home']['price']
                        awaySpreadPriceString = item['fanDuel']['spread']['away']['price']
                        homeSpreadPriceString = item['fanDuel']['spread']['home']['price']
                        awaySpreadPointsString = '+{}'.format(item['fanDuel']['spread']['away']['point']) if item['fanDuel']['spread']['away']['point'] > 0 else item['fanDuel']['spread']['away']['point']
                        homeSpreadPointsString = '+{}'.format(item['fanDuel']['spread']['home']['point']) if item['fanDuel']['spread']['home']['point'] > 0 else item['fanDuel']['spread']['home']['point']
                        overTotalPriceString = item['fanDuel']['totals']['over']['price']
                        underTotalPriceString = item['fanDuel']['totals']['under']['price']
                        overTotalPointsString = item['fanDuel']['totals']['over']['point']
                        underTotalPointsString = item['fanDuel']['totals']['under']['point']
                        partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                        for offset in range(15):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorSecondary)
                        for offset in range(15):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorSecondary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorPrimary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorPrimary, item['homeTeam']['teamName'])
                        # awayTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 12 + smallFont.height, awayColorSecondary, item['awayTeam']['record'])
                        # homeTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 22 + smallFont.height, homeColorSecondary, item['homeTeam']['record'])
                        runningCount = oddsStartNum
                        awayMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 11, green, str(awayMoneyLineString))
                        homeMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeMoneyLineString))
                        runningCount = runningCount + homeMLOdds + 2
                        awaySpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, str(awaySpreadPointsString))
                        # awaySpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 4 + smallFont.height, green, str(awaySpreadPriceString))
                        homeSpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 22, green, str(homeSpreadPointsString))
                        # homeSpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, green, str(homeSpreadPriceString))
                        runningCount = runningCount + awaySpreadOddsPoints + 2
                        overOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, 'O/U')
                        # overOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 9 + smallFont.height, green, str(overTotalPriceString))
                        underOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 22, red, str(underTotalPointsString))
                        # underOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, red, str(underTotalPriceString))
                        runningCount = runningCount + underOddsPoints + 2
                        # if 'Rain' in item['weather']['text'] or 'rain' in item['weather']['text']:
                        #     canvas.SetImage(rainImage, runningCount, 2)
                        # elif 'Cloudy' in item['weather']['text'] or 'Overcast' in item['weather']['text'] or 'cloudy' in item['weather']['text'] or 'overcast' in item['weather']['text']:
                        #     canvas.SetImage(partlyCloudyImage, runningCount, 2)
                        # elif 'Thunder' in item['weather']['text'] or 'thunder' in item['weather']['text']:
                        #     canvas.SetImage(thunderstormImage, runningCount, 2)
                        # elif 'Sun' in item['weather']['text'] or 'sun' in item['weather']['text']:
                        #     canvas.SetImage(sunnyImage, runningCount, 2)
                        # weatherTemp = graphics.DrawText(canvas, smallFont, runningCount + 5, 27, yellow, item['weather']['temp'])
                        startTime = graphics.DrawText(canvas, smallestFont, 80, 30, yellow, item['startTime'])
                    elif item['final'] == True:
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorSecondary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 8, offset + 13, homeColorSecondary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorPrimary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorPrimary, item['homeTeam']['teamName'])
                        runningCount = oddsStartNum
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 10
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['errors']['displayValue'])
                        runningCount = runningCount + homeErrorTotal + 10
                        finalDetail = graphics.DrawText(canvas, middleFont, runningCount + 5, 20, yellow, 'F')
                        # winningPitcher = graphics.DrawText(canvas, alilbiggerFont, 0, 32, green, "WP: {}".format(item['winningPitcher']))
                        gameFinalRunning = True
                        while gameFinalRunning:
                            pos -= 1
                            winningPitcher = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos, 32, green, "WP: {}".format(item['winningPitcher']))
                            losingPitcher = graphics.DrawText(offscreen_canvas, alilbiggerFont, pos + 4 + winningPitcher, 32, red, "LP: {}".format(item['losingPitcher']))
                            if (pos + 2 + winningPitcher + losingPitcher < 0):
                                gameFinalRunning = False
                                pos = offscreen_canvas.width
                            time.sleep(0.1)
                            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                    elif item['inprogress'] == True: 
                        situationString = '{}-{}'.format(item['situation']['balls'], item['situation']['strikes'])
                        baseSize = 6
                        outsSize = 4
                        baseHalf = abs(baseSize/2)
                        outsHalf = abs(outsSize/2)
                        for base in bases:
                            graphics.DrawLine(canvas, base[0] + baseHalf, base[1], base[0], base[1]+ baseHalf, yellow)
                            graphics.DrawLine(canvas, base[0] + baseHalf, base[1], base[0] + baseSize, base[1]+ baseHalf, yellow)
                            graphics.DrawLine(canvas, base[0] + baseHalf, base[1]+ baseSize, base[0], base[1]+ baseHalf, yellow)
                            graphics.DrawLine(canvas, base[0] + baseHalf, base[1]+ baseSize, base[0] + baseSize, base[1]+ baseHalf, yellow)
                        for out in outs:
                            graphics.DrawLine(canvas, out[0], out[1], out[0] + outsSize, out[1], red)
                            graphics.DrawLine(canvas, out[0], out[1], out[0], out[1] + outsSize, red)
                            graphics.DrawLine(canvas, out[0] + outsSize, out[1] + outsSize, out[0], out[1] + outsSize, red)
                            graphics.DrawLine(canvas, out[0] + outsSize, out[1] + outsSize, out[0] + outsSize, out[1], red)
                        if item['runners']['onFirst'] == True:
                            x = bases[0][0]
                            y = bases[0][1]
                            half = round(abs(baseSize/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + baseSize - offset, x + half + offset, y + baseSize - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        elif item['runners']['onSecond'] == True:
                            x = bases[1][0]
                            y = bases[1][1]
                            half = round(abs(baseSize/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + baseSize - offset, x + half + offset, y + baseSize - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        elif item['runners']['onThird'] == True:
                            x = bases[2][0]
                            y = bases[2][1]
                            half = round(abs(baseSize/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + baseSize - offset, x + half + offset, y + baseSize - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        if item['situation']['outs'] == 1:
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                        elif item['situation']['outs'] == 2:
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                                graphics.DrawLine(canvas, outs[1][0], outs[1][1] + y_offset, outs[1][0] + outsSize, outs[1][1] + y_offset, red)
                        elif item['situation']['outs'] == 3:
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                                graphics.DrawLine(canvas, outs[1][0], outs[1][1] + y_offset, outs[1][0] + outsSize, outs[1][1] + y_offset, red)
                                graphics.DrawLine(canvas, outs[2][0], outs[2][1] + y_offset, outs[2][0] + outsSize, outs[2][1] + y_offset, red)
                        awayTeam = graphics.DrawText(canvas, smallFont, 2, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 2, 21, homeColorSecondary, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeam + 8  if awayTeam > homeTeam else homeTeam + 8
                        runningCount = oddsStartNum
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 11, green, item['awayTeam']['score'])
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 21, green, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 5
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 21, green, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 5
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 21, green, item['homeTeam']['errors']['displayValue'])
                        runningCount = runningCount + homeErrorTotal + 5
                        count = graphics.DrawText(canvas, smallestFont, 106, 19, yellow, situationString)
                        inning = graphics.DrawText(canvas, smallestFont, 99, 31, yellow, item['inning'])
                elif type(item) is dict and 'league' in item.keys() and item['league'] == 'nba':
                    print('+++++++++++++')
                    print(item)
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:
                        awayMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['away']['price']) if item['fanDuel']['moneyLine']['away']['price'] > 0 else item['fanDuel']['moneyLine']['away']['price']
                        homeMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['home']['price']) if item['fanDuel']['moneyLine']['home']['price'] > 0 else item['fanDuel']['moneyLine']['home']['price']
                        awaySpreadPriceString = item['fanDuel']['spread']['away']['price']
                        homeSpreadPriceString = item['fanDuel']['spread']['home']['price']
                        awaySpreadPointsString = '+{}'.format(item['fanDuel']['spread']['away']['point']) if item['fanDuel']['spread']['away']['point'] > 0 else item['fanDuel']['spread']['away']['point']
                        homeSpreadPointsString = '+{}'.format(item['fanDuel']['spread']['home']['point']) if item['fanDuel']['spread']['home']['point'] > 0 else item['fanDuel']['spread']['home']['point']
                        overTotalPriceString = item['fanDuel']['totals']['over']['price']
                        underTotalPriceString = item['fanDuel']['totals']['under']['price']
                        overTotalPointsString = item['fanDuel']['totals']['over']['point']
                        underTotalPointsString = item['fanDuel']['totals']['under']['point']
                        partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                        for offset in range(12):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorSecondary)
                        for offset in range(12):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorSecondary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorPrimary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorPrimary, item['homeTeam']['teamName'])
                        # awayTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 12 + smallFont.height, awayColorSecondary, item['awayTeam']['record'])
                        # homeTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 22 + smallFont.height, homeColorSecondary, item['homeTeam']['record'])
                        runningCount = oddsStartNum
                        awayMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 11, green, str(awayMoneyLineString))
                        homeMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeMoneyLineString))
                        runningCount = runningCount + homeMLOdds + 2
                        awaySpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, str(awaySpreadPointsString))
                        # awaySpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 4 + smallFont.height, green, str(awaySpreadPriceString))
                        homeSpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 22, green, str(homeSpreadPointsString))
                        # homeSpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, green, str(homeSpreadPriceString))
                        runningCount = runningCount + awaySpreadOddsPoints + 2
                        overOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, 'O/U')
                        # overOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 9 + smallFont.height, green, str(overTotalPriceString))
                        underOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 30, red, str(underTotalPointsString))
                        # underOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, red, str(underTotalPriceString))
                        runningCount = runningCount + underOddsPoints + 2
                        # if 'Rain' in item['weather']['text'] or 'rain' in item['weather']['text']:
                        #     canvas.SetImage(rainImage, runningCount, 2)
                        # elif 'Cloudy' in item['weather']['text'] or 'Overcast' in item['weather']['text'] or 'cloudy' in item['weather']['text'] or 'overcast' in item['weather']['text']:
                        #     canvas.SetImage(partlyCloudyImage, runningCount, 2)
                        # elif 'Thunder' in item['weather']['text'] or 'thunder' in item['weather']['text']:
                        #     canvas.SetImage(thunderstormImage, runningCount, 2)
                        # elif 'Sun' in item['weather']['text'] or 'sun' in item['weather']['text']:
                        #     canvas.SetImage(sunnyImage, runningCount, 2)
                        # weatherTemp = graphics.DrawText(canvas, smallFont, runningCount + 5, 27, yellow, item['weather']['temp'])
                        startTime = graphics.DrawText(canvas, smallestFont, 80, 30, yellow, item['startTime'])
                    if item['final'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 24, homeColorSecondary, item['homeTeam']['score'])
                        finalDetail = graphics.DrawText(canvas, smallFont, 41, 22, yellow, 'F')
                    elif item['inprogress'] == True: 
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 22, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 22, homeColorSecondary, item['homeTeam']['score'])
                        quarter = graphics.DrawText(canvas, smallestFont, 43, 22, yellow, item['quarter'])
                        timeRemaining = graphics.DrawText(canvas, smallestFont, 43, 29, yellow, item['timeRemaining'])
                elif type(item) is dict and 'league' in item.keys() and item['league'] == 'ncaaBasketball':
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
                        startTime = graphics.DrawText(canvas, smallestFont, 43, 22, yellow, item['startTime'])
                        odds = graphics.DrawText(canvas, smallestFont, 43, 29, yellow, item['odds'])
                        tv = graphics.DrawText(canvas, smallestFont, 43, 25, yellow, item['tv'])
                    if item['final'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 24, homeColorSecondary, item['homeTeam']['score'])
                        finalDetail = graphics.DrawText(canvas, middleFont, 43, 20, yellow, 'F')
                    elif item['inprogress'] == True: 
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 22, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 22, homeColorSecondary, item['homeTeam']['score'])
                        quarter = graphics.DrawText(canvas, smallestFont, 43, 22, yellow, item['quarter'])
                        timeRemaining = graphics.DrawText(canvas, smallestFont, 43, 29, yellow, item['timeRemaining'])
                elif type(item) is dict and 'stockSymbol' in item.keys():
                    color = green if item['up'] else red
                    direction = 1 if item['up'] else -1
                    stockLogo = Image.open(requests.get(item['url'], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    canvas.SetImage(stockLogo, 0, 0)
                    stockSymbol = graphics.DrawText(canvas, middleFont, stockLogo.width + 2, 20, color, item['stockSymbol'])
                    currentPrice = graphics.DrawText(canvas, smallFont, stockLogo.width + 2 + stockSymbol + 10, 14, color, item['currentPrice'])
                    x = stockLogo.width + 2 + stockSymbol + 8
                    y = 25 if item['up'] else 28
                    size = 4
                    for offset in range(size):
                        graphics.DrawLine(canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)
                    percentChange = graphics.DrawText(canvas, middleFont, stockLogo.width + 2 + stockSymbol + 15, 31, color, item['percentChange'])
                elif type(item) is dict and 'standings' in item.keys():
                    runningBuffer = 1
                    # team = graphics.DrawText(canvas, smallestFont, 0, 2, green, item['divisionName'])
                    # win = graphics.DrawText(canvas, smallestFont, 30, 2, green, 'W')
                    # loss = graphics.DrawText(canvas, smallestFont, 35, 2, green, 'L')
                    # gamesBack = graphics.DrawText(canvas, smallestFont, 400, 2, green, 'GB')
                    for team in item['standings']:
                        print(team)
                        print(runningBuffer)
                        teamName = graphics.DrawText(canvas, alilbiggerFont, 0, runningBuffer, green, str(team['team']))
                        win = graphics.DrawText(canvas, alilbiggerFont, 25, runningBuffer, green, str(team['win']))
                        loss = graphics.DrawText(canvas, alilbiggerFont, 35, runningBuffer, green, str(team['loss']))
                        gamesBack = graphics.DrawText(canvas, alilbiggerFont, 400, runningBuffer, green, str(team['gamesBack']))
                        runningBuffer = runningBuffer + 8
                elif type(item) is dict and 'temp' in item.keys():
                    # locationString = '/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    # weatherImage = Image.open(locationString).convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    print(item['condition'])
                    color = blue
                    if 'Rain' in item['condition'] or 'rain' in item['condition']:
                        canvas.SetImage(rainImage, 0, 2)
                        color = blue
                    elif 'Cloudy' in item['condition'] or 'Overcast' in item['condition'] or 'cloudy' in item['condition'] or 'overcast' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 2)
                        color = lightblue
                    elif 'Thunder' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 2)
                        color = blue
                    elif 'Sun' in item['condition'] or 'sun' in item['condition']:
                        canvas.SetImage(sunnyImage, 0, 2)
                        color = yellow
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 0, 31, black, item['condition'])
                    centered = 32 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, centered, 31, blue, item['condition'])
                    currentTemp = graphics.DrawText(canvas, middleFont, 32, 13, blue, item['temp'])
                    highLow = graphics.DrawText(canvas, alilbiggerFont, 26, 22, blue, item['highLow'])
                elif type(item) is dict and 'condition' in item.keys():
                    partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    print(item['condition'])
                    color = blue
                    if 'Rain' in item['condition'] or 'rain' in item['condition']:
                        canvas.SetImage(rainImage, 0, 2)
                        color = blue
                    elif 'Cloudy' in item['condition'] or 'Overcast' in item['condition'] or 'cloudy' in item['condition'] or 'overcast' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 2)
                        color = lightblue
                    elif 'Thunder' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 2)
                        color = blue
                    elif 'Sun' in item['condition'] or 'sun' in item['condition']:
                        canvas.SetImage(sunnyImage, 0, 2)
                        color = yellow
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 0, 31, black, item['condition'])
                    centered = 32 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, centered, 31, blue, item['condition'])
                    day = graphics.DrawText(canvas, alilbiggerFont, 32, 8, blue, item['day'])
                    currentTemp = graphics.DrawText(canvas, alilbiggerFont, 32, 19, blue, item['rainPercent'])
                    highLow = graphics.DrawText(canvas, alilbiggerFont, 26, 24, blue, item['highLow'])
                elif isinstance(item, list) and 'condition' in item[0].keys():
                    runningX = 0
                    runningY = 10
                    for day in item:
                        print(day)
                        # locationString = '/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(day['icon'])
                        # weatherImage = Image.open(locationString).convert('RGB').resize((8, 8), Image.ANTIALIAS)
                        # canvas.SetImage(weatherImage, runningX, 15)
                        dayText = graphics.DrawText(canvas, smallFont, 5, 10, green, day['day'])
                        weatherConditionText = graphics.DrawText(canvas, smallestFont, 0, 17, blue, day['condition'])
                        highLow = graphics.DrawText(canvas, alilbiggerFont, 0, 25, blue, day['highLow'])
                        currentTemp = graphics.DrawText(canvas, alilbiggerFont, 0, 32, blue, 'Rain: {}'.format(day['rainPercent']))
                        runningX = runningX + 20
                        time.sleep(3)
                        canvas.Clear()
                elif type(item) is dict and 'tourneyName' in item.keys():
                    for page in item['players']:
                        print(page)
                        for player in page:
                            tourneyName = graphics.DrawText(canvas, smallestFont, 10, 5, blue, item['tourneyName'])
                            tourneyStatus = graphics.DrawText(canvas, smallestFont, 10, 12, blue, item['tourneyStatus'])
                            runningTotal = 18
                            position = graphics.DrawText(canvas, smallestFont, 0, runningTotal, blue, player['position'])
                            name = graphics.DrawText(canvas, smallestFont, 10, runningTotal, blue, player['name'])
                            score = graphics.DrawText(canvas, smallestFont, 30, runningTotal, blue, player['score'])
                            thru = graphics.DrawText(canvas, smallestFont, 45, runningTotal, blue, player['teeTime'])
                            runningTotal = runningTotal + 8
                else:
                    currentTIme = graphics.DrawText(canvas, font, 0, 23, blue, item)
                time.sleep(10)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()