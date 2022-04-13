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
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallestFont = graphics.Font()
            smallestFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")
            alilbiggerFont = graphics.Font()
            alilbiggerFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x7.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            # responseArr = json.loads(url.text)
            responseArr = [{'league': 'mlb', 'pregame': False, 'inprogress': True, 'final': False, 'awayTeam': {'teamName': 'Astros', 'name': 'HOU', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '6'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [0, 45, 98], 'secondary': [235, 110, 31]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'D-Backs', 'name': 'ARI', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '5'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [167, 25, 48], 'secondary': [0, 0, 0]}, 'record': '4-1'}, 'inning': 'Bot 9th', 'runners': {'onFirst': True, 'onSecond': False, 'onThird': False}, 'situation': {'balls': 1, 'strikes': 2, 'outs': 2}}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Padres', 'name': 'SD', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '5'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [0, 45, 98], 'secondary': [254, 195, 37]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Giants', 'name': 'SF', 'score': '2', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '4'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [253, 90, 30], 'secondary': [0, 0, 0]}, 'record': '4-3'}, 'winningPitcher': 'L. Webb 1-0', 'losingPitcher': 'S. Manaea 1-1', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': True, 'final': False, 'awayTeam': {'teamName': 'Athletics', 'name': 'OAK', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '0'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [0, 56, 49], 'secondary': [239, 178, 30]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Rays', 'name': 'TB', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '1'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [9, 44, 92], 'secondary': [143, 188, 230]}, 'record': '2-3'}, 'inning': 'Top 2nd', 'runners': {'onFirst': True, 'onSecond': False, 'onThird': False}, 'situation': {'balls': 0, 'strikes': 1, 'outs': 1}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Brewers', 'name': 'MIL', 'colors': {'main': [10, 35, 81], 'secondary': [182, 146, 46]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Orioles', 'name': 'BAL', 'colors': {'main': [223, 70, 1], 'secondary': [0, 0, 0]}, 'record': '2-3'}, 'startTime': '7:05 PM EDT', 'weather': {'indoors': False, 'text': 'Intermittent clouds', 'temp': '79°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Baltimore Orioles', 'price': 154}, 'away': {'name': 'Milwaukee Brewers', 'price': -184}}, 'spread': {'home': {'name': 'Baltimore Orioles', 'price': -108, 'point': 1.5}, 'away': {'name': 'Milwaukee Brewers', 'price': -111, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 8}, 'under': {'name': 'Under', 'price': -110, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Blue Jays', 'name': 'TOR', 'colors': {'main': [19, 74, 142], 'secondary': [29, 45, 92]}, 'record': '2-1'}, 'homeTeam': {'teamName': 'Yankees', 'name': 'NYY', 'colors': {'main': [228, 0, 43], 'secondary': [0, 48, 135]}, 'record': '3-2'}, 'startTime': '7:05 PM EDT', 'weather': {'indoors': False, 'text': 'Intermittent clouds', 'temp': '68°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'New York Yankees', 'price': -174}, 'away': {'name': 'Toronto Blue Jays', 'price': 146}}, 'spread': {'home': {'name': 'New York Yankees', 'price': 120, 'point': -1.5}, 'away': {'name': 'Toronto Blue Jays', 'price': -144, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -115, 'point': 8}, 'under': {'name': 'Under', 'price': -105, 'point': 8}}}}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Mariners', 'name': 'SEA', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '0'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [12, 44, 86], 'secondary': [0, 92, 92]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'White Sox', 'name': 'CHW', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '0'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [0, 0, 0], 'secondary': [196, 206, 212]}, 'record': '2-3'}, 'winningPitcher': '', 'losingPitcher': '', 'finalDetail': 'Top 1st'}, {'day': 'CURRENT', 'condition': 'Partly cloudy', 'rainPercent': '0%', 'icon': 116, 'temp': '78°', 'highLow': '70°/84°'}, {'day': 'THU', 'rainPercent': '89%', 'condition': 'Patchy Rain', 'icon': 176, 'highLow': '64°/86°'}, {'day': 'FRI', 'rainPercent': '87%', 'condition': 'Patchy Rain', 'icon': 176, 'highLow': '69°/88°'}, {'stockSymbol': 'TSLA', 'url': 'https://logo.clearbit.com/tesla.com', 'currentPrice': '1022.37', 'up': True, 'percentChange': '3.59%'}, {'stockSymbol': 'OBNK', 'url': 'https://logo.clearbit.com/originbank.com', 'currentPrice': '41.01', 'up': True, 'percentChange': '1.28%'}, {'stockSymbol': 'STEM', 'url': 'https://logo.clearbit.com/stem.com', 'currentPrice': '10.12', 'up': True, 'percentChange': '3.16%'}, {'stockSymbol': 'AAPL', 'url': 'https://logo.clearbit.com/apple.com', 'currentPrice': '170.40', 'up': True, 'percentChange': '1.63%'}, {'stockSymbol': 'AMC', 'url': 'https://logo.clearbit.com/amctheatres.com', 'currentPrice': '18.53', 'up': True, 'percentChange': '6.37%'}, {'stockSymbol': 'AMD', 'url': 'https://logo.clearbit.com/amd.com', 'currentPrice': '97.74', 'up': True, 'percentChange': '2.78%'}, {'stockSymbol': 'HOOD', 'url': 'https://logo.clearbit.com/robinhood.com', 'currentPrice': '11.89', 'up': True, 'percentChange': '4.02%'}, {'stockSymbol': 'BTC', 'url': 'https://logo.clearbit.com/bitcoin.org', 'currentPrice': '41274', 'up': True, 'percentChange': '3.59%'}, {'stockSymbol': 'ETH', 'url': 'https://logo.clearbit.com/ethereum.org', 'currentPrice': '3119.90', 'up': True, 'percentChange': '3.51%'}, {'stockSymbol': 'DOGE', 'url': 'https://logo.clearbit.com/dogecoin.com', 'currentPrice': '0.1403', 'up': True, 'percentChange': '2.54%'}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hornets', 'name': 'CHA', 'colors': {'main': [32, 23, 71], 'secondary': [0, 119, 139]}, 'record': '22-19'}, 'homeTeam': {'teamName': 'Hawks', 'name': 'ATL', 'colors': {'main': [200, 16, 46], 'secondary': [255, 255, 255]}, 'record': '43-39'}, 'startTime': '7:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Atlanta Hawks', 'price': -225}, 'away': {'name': 'Charlotte Hornets', 'price': 188}}, 'spread': {'home': {'name': 'Atlanta Hawks', 'price': -110, 'point': -5.5}, 'away': {'name': 'Charlotte Hornets', 'price': -110, 'point': 5.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 235.5}, 'under': {'name': 'Under', 'price': -110, 'point': 235.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Spurs', 'name': 'SA', 'colors': {'main': [182, 191, 191], 'secondary': [0, 0, 0]}, 'record': '16-25'}, 'homeTeam': {'teamName': 'Pelicans', 'name': 'NO', 'colors': {'main': [0, 43, 92], 'secondary': [227, 25, 55]}, 'record': '34-48'}, 'startTime': '9:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'New Orleans Pelicans', 'price': -235}, 'away': {'name': 'San Antonio Spurs', 'price': 194}}, 'spread': {'home': {'name': 'New Orleans Pelicans', 'price': -110, 'point': -6}, 'away': {'name': 'San Antonio Spurs', 'price': -110, 'point': 6}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 225}, 'under': {'name': 'Under', 'price': -108, 'point': 225}}}}]
            print(responseArr)
            canvas = self.matrix
            bases =  [[113,5],[108,0],[103,5]]
            outs = [[106,20],[112,20]]
            for item in responseArr:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(item)
                if type(item) is dict and 'league' in item.keys() and item['league'] == 'mlb':
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:
                        awayMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['away']['price']) if int(item['fanDuel']['moneyLine']['away']['price']) > 0 else item['fanDuel']['moneyLine']['away']['price']
                        homeMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['home']['price']) if int(item['fanDuel']['moneyLine']['home']['price']) > 0 else item['fanDuel']['moneyLine']['home']['price']
                        awaySpreadPriceString = item['fanDuel']['spread']['away']['price']
                        homeSpreadPriceString = item['fanDuel']['spread']['home']['price']
                        awaySpreadPointsString = '+{}'.format(item['fanDuel']['spread']['away']['point']) if item['fanDuel']['spread']['away']['point'] > 0 else item['fanDuel']['spread']['away']['point']
                        homeSpreadPointsString = '+{}'.format(item['fanDuel']['spread']['home']['point']) if item['fanDuel']['spread']['home']['point'] > 0 else item['fanDuel']['spread']['home']['point']
                        overTotalPriceString = item['fanDuel']['totals']['over']['price']
                        underTotalPriceString = item['fanDuel']['totals']['under']['price']
                        overTotalPointsString = item['fanDuel']['totals']['over']['point']
                        underTotalPointsString = item['fanDuel']['totals']['under']['point']
                        partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 8, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
                        # awayTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 12 + smallFont.height, awayColorSecondary, item['awayTeam']['record'])
                        # homeTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 22 + smallFont.height, homeColorSecondary, item['homeTeam']['record'])
                        runningCount = oddsStartNum
                        awayMLOdds = graphics.DrawText(canvas, alilbiggerFont, runningCount, 10, green, str(awayMoneyLineString))
                        homeMLOdds = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(homeMoneyLineString))
                        runningCount = runningCount + homeMLOdds + 4
                        awaySpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, str(awaySpreadPointsString))
                        # awaySpreadOddsPrice = graphics.DrawText(canvas, smallestFont, runningCount, 4 + smallestFont.height, green, str(awaySpreadPriceString))
                        homeSpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeSpreadPointsString))
                        # homeSpreadOddsPrice = graphics.DrawText(canvas, smallestFont, runningCount, 19 + smallestFont.height, green, str(homeSpreadPriceString))
                        runningCount = runningCount + awaySpreadOddsPoints + 4
                        overOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, 'O/U')
                        # overOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 9 + alilbiggerFont.height, green, str(overTotalPriceString))
                        underOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(underTotalPointsString))
                        # underOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 19 + alilbiggerFont.height, red, str(underTotalPriceString))
                        runningCount = runningCount + underOddsPoints + 4
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
                        # awayMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['away']['price']) if item['fanDuel']['moneyLine']['away']['price'] > 0 else item['fanDuel']['moneyLine']['away']['price']
                        # homeMoneyLineString = '+{}'.format(item['fanDuel']['moneyLine']['home']['price']) if item['fanDuel']['moneyLine']['home']['price'] > 0 else item['fanDuel']['moneyLine']['home']['price']
                        # awaySpreadPriceString = item['fanDuel']['spread']['away']['price']
                        # homeSpreadPriceString = item['fanDuel']['spread']['home']['price']
                        # awaySpreadPointsString = '+{}'.format(item['fanDuel']['spread']['away']['point']) if item['fanDuel']['spread']['away']['point'] > 0 else item['fanDuel']['spread']['away']['point']
                        # homeSpreadPointsString = '+{}'.format(item['fanDuel']['spread']['home']['point']) if item['fanDuel']['spread']['home']['point'] > 0 else item['fanDuel']['spread']['home']['point']
                        # overTotalPriceString = item['fanDuel']['totals']['over']['price']
                        # underTotalPriceString = item['fanDuel']['totals']['under']['price']
                        # overTotalPointsString = item['fanDuel']['totals']['over']['point']
                        # underTotalPointsString = item['fanDuel']['totals']['under']['point']
                        # partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        # homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        # oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                        # for offset in range(15):
                        #     graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorSecondary)
                        # for offset in range(15):
                        #     graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorSecondary)
                        # awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorPrimary, item['awayTeam']['teamName'])
                        # homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorPrimary, item['homeTeam']['teamName'])
                        # # awayTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 12 + smallFont.height, awayColorSecondary, item['awayTeam']['record'])
                        # # homeTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 22 + smallFont.height, homeColorSecondary, item['homeTeam']['record'])
                        # runningCount = oddsStartNum
                        # awayMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 11, green, str(awayMoneyLineString))
                        # homeMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeMoneyLineString))
                        # runningCount = runningCount + homeMLOdds + 2
                        # awaySpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, str(awaySpreadPointsString))
                        # # awaySpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 4 + smallFont.height, green, str(awaySpreadPriceString))
                        # homeSpreadOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 22, green, str(homeSpreadPointsString))
                        # # homeSpreadOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, green, str(homeSpreadPriceString))
                        # runningCount = runningCount + awaySpreadOddsPoints + 2
                        # overOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 11, green, 'O/U')
                        # # overOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 9 + smallFont.height, green, str(overTotalPriceString))
                        # underOddsPoints = graphics.DrawText(canvas, smallFont, runningCount, 22, red, str(underTotalPointsString))
                        # # underOddsPrice = graphics.DrawText(canvas, smallFont, runningCount, 19 + smallFont.height, red, str(underTotalPriceString))
                        # runningCount = runningCount + underOddsPoints + 2
                        # # if 'Rain' in item['weather']['text'] or 'rain' in item['weather']['text']:
                        # #     canvas.SetImage(rainImage, runningCount, 2)
                        # # elif 'Cloudy' in item['weather']['text'] or 'Overcast' in item['weather']['text'] or 'cloudy' in item['weather']['text'] or 'overcast' in item['weather']['text']:
                        # #     canvas.SetImage(partlyCloudyImage, runningCount, 2)
                        # # elif 'Thunder' in item['weather']['text'] or 'thunder' in item['weather']['text']:
                        # #     canvas.SetImage(thunderstormImage, runningCount, 2)
                        # # elif 'Sun' in item['weather']['text'] or 'sun' in item['weather']['text']:
                        # #     canvas.SetImage(sunnyImage, runningCount, 2)
                        # # weatherTemp = graphics.DrawText(canvas, smallFont, runningCount + 5, 27, yellow, item['weather']['temp'])
                        # startTime = graphics.DrawText(canvas, smallestFont, 80, 30, yellow, item['startTime'])
                    elif item['final'] == True:
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 8, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
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
                        winningPitcher = graphics.DrawText(canvas, smallestFont, 0, 32, green, item['winningPitcher'])
                        losingPitcher = graphics.DrawText(canvas, smallestFont, 4 + winningPitcher, 32, red, item['losingPitcher'])
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
                        
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 8, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
                        runningCount = oddsStartNum
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 10
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['errors']['displayValue'])
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
                        partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
                        # awayTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 12 + smallFont.height, awayColorSecondary, item['awayTeam']['record'])
                        # homeTeamStandings = graphics.DrawText(canvas, smallestFont, 5, 22 + smallFont.height, homeColorSecondary, item['homeTeam']['record'])
                        runningCount = oddsStartNum
                        awayMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, str(awayMoneyLineString))
                        homeMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeMoneyLineString))
                        runningCount = runningCount + homeMLOdds + 4
                        awaySpreadOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 10, green, str(awaySpreadPointsString))
                        # awaySpreadOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 4 + alilbiggerFont.height, green, str(awaySpreadPriceString))
                        homeSpreadOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(homeSpreadPointsString))
                        # homeSpreadOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 19 + alilbiggerFont.height, green, str(homeSpreadPriceString))
                        runningCount = runningCount + awaySpreadOddsPoints + 4
                        overOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, 'O/U')
                        # overOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 9 + alilbiggerFont.height, green, str(overTotalPriceString))
                        underOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(underTotalPointsString))
                        # underOddsPrice = graphics.DrawText(canvas, alilbiggerFont, runningCount, 19 + alilbiggerFont.height, red, str(underTotalPriceString))
                        runningCount = runningCount + underOddsPoints + 4
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
                        awayTeamBlack = graphics.DrawText(canvas, middleFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, middleFont, 1, 23, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(16):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorPrimary)
                        for offset in range(16):
                            graphics.DrawLine(canvas, 0, offset + 16, oddsStartNum - 8, offset + 16, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, middleFont, 1, 13, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, middleFont, 1, 28, homeColorSecondary, item['homeTeam']['teamName'])
                        runningCount = oddsStartNum
                        awayScore = graphics.DrawText(canvas, middleFont, runningCount, 14, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                        homeScore = graphics.DrawText(canvas, middleFont, runningCount, 29, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        finalDetail = graphics.DrawText(canvas, middleFont, 119, 20, yellow, 'F')
                        # finalDetail = graphics.DrawText(canvas, middleFont, 110, 20, yellow, item['finalDetail'])
                    elif item['inprogress'] == True:    
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 25, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 8 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 8
                        for offset in range(16):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 8, offset, awayColorPrimary)
                        for offset in range(16):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 8, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 25, homeColorSecondary, item['homeTeam']['teamName'])
                        runningCount = oddsStartNum
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 12, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 23, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        quarter = graphics.DrawText(canvas, middleFont, runningCount + 7, 5, yellow, item['quarter'])
                        timeRemaining = graphics.DrawText(canvas, middleFont, runningCount + 5, 18, yellow, item['time'])
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
                    currentPrice = graphics.DrawText(canvas, smallFont, stockLogo.width + 2 + stockSymbol + 10, 14, color, '${}'.format(item['currentPrice']))
                    x = stockLogo.width + 2 + stockSymbol
                    y = 25 if item['up'] else 28
                    size = 4
                    for offset in range(size):
                        graphics.DrawLine(canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)
                    percentChange = graphics.DrawText(canvas, middleFont, stockLogo.width + 2 + stockSymbol + 8, 31, color, item['percentChange'])
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
                    # locationString = '/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    # weatherImage = Image.open(locationString).convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
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
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 40, 2, black, item['condition'])
                    centered = 35 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, centered, 2, blue, item['condition'])
                    currentTemp = graphics.DrawText(canvas, middleFont, 32, 13, blue, item['temp'])
                    highLow = graphics.DrawText(canvas, alilbiggerFont, 90, 22, blue, item['highLow'])
                    rainChance = graphics.DrawText(canvas, alilbiggerFont, 90, 30, blue, 'Rain: 80%')
                elif type(item) is dict and 'condition' in item.keys():
                    partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
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
                        # locationString = '/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(day['icon'])
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
                time.sleep(20)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()