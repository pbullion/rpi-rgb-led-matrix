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
            slightlyBiggerFont = graphics.Font()
            slightlyBiggerFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/8x13.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            # responseArr = json.loads(url.text)
            responseArr = [{'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'D-Backs', 'name': 'ARI', 'colors': {'main': [167, 25, 48], 'secondary': [0, 0, 0]}, 'record': '2-4'}, 'homeTeam': {'teamName': 'Nationals', 'name': 'WSH', 'colors': {'main': [171, 0, 3], 'secondary': [17, 34, 91]}, 'record': '3-7'}, 'startTime': '7:05 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '48°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Washington Nationals', 'price': -130}, 'away': {'name': 'Arizona Diamondbacks', 'price': 110}}, 'spread': {'home': {'name': 'Washington Nationals', 'price': 152, 'point': -1.5}, 'away': {'name': 'Arizona Diamondbacks', 'price': -184, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 8.5}, 'under': {'name': 'Under', 'price': -108, 'point': 8.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Blue Jays', 'name': 'TOR', 'colors': {'main': [19, 74, 142], 'secondary': [255, 255, 255]}, 'record': '4-2'}, 'homeTeam': {'teamName': 'Red Sox', 'name': 'BOS', 'colors': {'main': [189, 48, 57], 'secondary': [13, 43, 86]}, 'record': '6-4'}, 'startTime': '7:10 PM EDT', 'weather': {'indoors': False, 'text': 'Showers', 'temp': '49°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Boston Red Sox', 'price': -144}, 'away': {'name': 'Toronto Blue Jays', 'price': 122}}, 'spread': {'home': {'name': 'Boston Red Sox', 'price': 138, 'point': -1.5}, 'away': {'name': 'Toronto Blue Jays', 'price': -166, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -105, 'point': 9.5}, 'under': {'name': 'Under', 'price': -115, 'point': 9.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Pirates', 'name': 'PIT', 'colors': {'main': [253, 184, 39], 'secondary': [0, 0, 0]}, 'record': '4-2'}, 'homeTeam': {'teamName': 'Brewers', 'name': 'MIL', 'colors': {'main': [10, 35, 81], 'secondary': [182, 146, 46]}, 'record': '5-5'}, 'startTime': '7:40 PM EDT', 'weather': {'indoors': False, 'text': 'Mostly cloudy', 'temp': '46°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Milwaukee Brewers', 'price': -270}, 'away': {'name': 'Pittsburgh Pirates', 'price': 220}}, 'spread': {'home': {'name': 'Milwaukee Brewers', 'price': -125, 'point': -1.5}, 'away': {'name': 'Pittsburgh Pirates', 'price': 104, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -124, 'point': 7}, 'under': {'name': 'Under', 'price': 102, 'point': 7}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Giants', 'name': 'SF', 'colors': {'main': [253, 90, 30], 'secondary': [0, 0, 0]}, 'record': '4-2'}, 'homeTeam': {'teamName': 'Mets', 'name': 'NYM', 'colors': {'main': [255, 89, 16], 'secondary': [0, 45, 114]}, 'record': '7-2'}, 'startTime': '7:40 PM EDT', 'weather': {'indoors': False, 'text': 'Showers', 'temp': '48°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'New York Mets', 'price': -600}, 'away': {'name': 'San Francisco Giants', 'price': 380}}, 'spread': {'home': {'price': '0', 'point': 0}, 'away': {'price': '0', 'point': 0}}, 'totals': {'over': {'price': '0', 'point': 0}, 'under': {'price': '0', 'point': 0}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Rays', 'name': 'TB', 'colors': {'main': [9, 44, 92], 'secondary': [143, 188, 230]}, 'record': '4-3'}, 'homeTeam': {'teamName': 'Cubs', 'name': 'CHC', 'colors': {'main': [204, 52, 51], 'secondary': [14, 51, 134]}, 'record': '5-6'}, 'startTime': '7:40 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '45°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Chicago Cubs', 'price': 106}, 'away': {'name': 'Tampa Bay Rays', 'price': -124}}, 'spread': {'home': {'name': 'Chicago Cubs', 'price': -156, 'point': 1.5}, 'away': {'name': 'Tampa Bay Rays', 'price': 130, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 7.5}, 'under': {'name': 'Under', 'price': -102, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Angels', 'name': 'LAA', 'colors': {'main': [186, 0, 33], 'secondary': [0, 50, 99]}, 'record': '3-3'}, 'homeTeam': {'teamName': 'Astros', 'name': 'HOU', 'colors': {'main': [0, 45, 98], 'secondary': [235, 110, 31]}, 'record': '6-5'}, 'startTime': '8:10 PM EDT', 'weather': {'indoors': False, 'text': 'Cloudy', 'temp': '72°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Houston Astros', 'price': -166}, 'away': {'name': 'Los Angeles Angels', 'price': 140}}, 'spread': {'home': {'name': 'Houston Astros', 'price': 128, 'point': -1.5}, 'away': {'name': 'Los Angeles Angels', 'price': -154, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -104, 'point': 8}, 'under': {'name': 'Under', 'price': -118, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Twins', 'name': 'MIN', 'colors': {'main': [0, 43, 92], 'secondary': [211, 17, 69]}, 'record': '2-4'}, 'homeTeam': {'teamName': 'Royals', 'name': 'KC', 'colors': {'main': [0, 70, 135], 'secondary': [192, 154, 91]}, 'record': '4-6'}, 'startTime': '8:10 PM EDT', 'weather': {'indoors': False, 'text': 'Cloudy', 'temp': '53°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Kansas City Royals', 'price': 104}, 'away': {'name': 'Minnesota Twins', 'price': -122}}, 'spread': {'home': {'name': 'Kansas City Royals', 'price': -162, 'point': 1.5}, 'away': {'name': 'Minnesota Twins', 'price': 134, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -118, 'point': 8}, 'under': {'name': 'Under', 'price': -104, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Phillies', 'name': 'PHI', 'colors': {'main': [40, 72, 152], 'secondary': [232, 24, 40]}, 'record': '3-3'}, 'homeTeam': {'teamName': 'Rockies', 'name': 'COL', 'colors': {'main': [51, 51, 102], 'secondary': [255, 255, 255]}, 'record': '4-7'}, 'startTime': '8:40 PM EDT', 'weather': {'indoors': False, 'text': 'Intermittent clouds', 'temp': '72°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Colorado Rockies', 'price': 112}, 'away': {'name': 'Philadelphia Phillies', 'price': -132}}, 'spread': {'home': {'name': 'Colorado Rockies', 'price': -132, 'point': 1.5}, 'away': {'name': 'Philadelphia Phillies', 'price': 110, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -115, 'point': 11.5}, 'under': {'name': 'Under', 'price': -105, 'point': 11.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Orioles', 'name': 'BAL', 'colors': {'main': [223, 70, 1], 'secondary': [0, 0, 0]}, 'record': '3-3'}, 'homeTeam': {'teamName': 'Athletics', 'name': 'OAK', 'colors': {'main': [0, 56, 49], 'secondary': [239, 178, 30]}, 'record': '3-7'}, 'startTime': '9:40 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '63°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Oakland Athletics', 'price': -142}, 'away': {'name': 'Baltimore Orioles', 'price': 120}}, 'spread': {'home': {'name': 'Oakland Athletics', 'price': 134, 'point': -1.5}, 'away': {'name': 'Baltimore Orioles', 'price': -162, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -114, 'point': 8}, 'under': {'name': 'Under', 'price': -106, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Reds', 'name': 'CIN', 'colors': {'main': [198, 1, 31], 'secondary': [0, 0, 0]}, 'record': '0-2'}, 'homeTeam': {'teamName': 'Padres', 'name': 'SD', 'colors': {'main': [0, 45, 98], 'secondary': [254, 195, 37]}, 'record': '2-9'}, 'startTime': '9:40 PM EDT', 'weather': {'indoors': False, 'text': 'Mostly sunny', 'temp': '64°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'San Diego Padres', 'price': -215}, 'away': {'name': 'Cincinnati Reds', 'price': 180}}, 'spread': {'home': {'name': 'San Diego Padres', 'price': -104, 'point': -1.5}, 'away': {'name': 'Cincinnati Reds', 'price': -115, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -104, 'point': 7.5}, 'under': {'name': 'Under', 'price': -118, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Rangers', 'name': 'TEX', 'colors': {'main': [192, 17, 31], 'secondary': [0, 50, 120]}, 'record': '1-5'}, 'homeTeam': {'teamName': 'Mariners', 'name': 'SEA', 'colors': {'main': [0, 92, 92], 'secondary': [12, 44, 86]}, 'record': '2-7'}, 'startTime': '9:40 PM EDT', 'weather': {'indoors': False, 'text': 'Cloudy', 'temp': '52°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Seattle Mariners', 'price': -146}, 'away': {'name': 'Texas Rangers', 'price': 124}}, 'spread': {'home': {'name': 'Seattle Mariners', 'price': 134, 'point': -1.5}, 'away': {'name': 'Texas Rangers', 'price': -162, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 7.5}, 'under': {'name': 'Under', 'price': -102, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Braves', 'name': 'ATL', 'colors': {'main': [206, 17, 65], 'secondary': [19, 39, 79]}, 'record': '3-4'}, 'homeTeam': {'teamName': 'Dodgers', 'name': 'LAD', 'colors': {'main': [239, 62, 66], 'secondary': [0, 90, 156]}, 'record': '5-7'}, 'startTime': '10:10 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '66°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Los Angeles Dodgers', 'price': -152}, 'away': {'name': 'Atlanta Braves', 'price': 128}}, 'spread': {'home': {'name': 'Los Angeles Dodgers', 'price': 142, 'point': -1.5}, 'away': {'name': 'Atlanta Braves', 'price': -172, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -108, 'point': 8}, 'under': {'name': 'Under', 'price': -112, 'point': 8}}}}, {'day': 'CURRENT', 'condition': 'PARTLY CLOUDY', 'rainPercent': '0%', 'icon': 116, 'temp': '74°', 'highLow': '59°/78°'}, {'day': 'WED', 'rainPercent': '90%', 'condition': 'PATCHY RAIN', 'icon': 176, 'highLow': '69°/81°'}, {'day': 'THU', 'rainPercent': '86%', 'condition': 'PATCHY RAIN', 'icon': 176, 'highLow': '70°/92°'}, {'type': 'rssFeed', 'name': 'ESPNMLB', 'feed': "The end of service time manipulation? How Kris Bryant paved the way for the next Kris Bryant • Sources: Rockies, Freeland reach $64.5M deal • Pitch clock shaving 20 minutes off minors games • Padres 1st team to reach uniform ad deal for '23"}, {'type': 'rssFeed', 'name': 'CNN', 'feed': "Russian forces are facing pushback as attacks ramp up, UK intel says, but Russia has seized the city of Kreminna and blasted a civilian shelter in Mariupol • Blind spot: US doesn't know what happens to weapons being sent to Ukraine • The Donbas region: Heart of Russia's war on Ukraine. Here's why it's so important • Multiple sources: US prepping another $800 million weapons package for Ukraine"}, {'stockSymbol': 'TSLA', 'url': 'https://logo.clearbit.com/tesla.com', 'currentPrice': '1028.15', 'up': True, 'percentChange': '2.38%'}, {'stockSymbol': 'OBNK', 'url': 'https://logo.clearbit.com/originbank.com', 'currentPrice': '41.75', 'up': True, 'percentChange': '2.81%'}, {'stockSymbol': 'AAPL', 'url': 'https://logo.clearbit.com/apple.com', 'currentPrice': '167.40', 'up': True, 'percentChange': '1.41%'}, {'stockSymbol': 'TWTR', 'url': 'https://logo.clearbit.com/twitter.com', 'currentPrice': '46.16', 'up': False, 'percentChange': '4.73%'}, {'stockSymbol': 'BTC', 'url': 'https://logo.clearbit.com/bitcoin.org', 'currentPrice': '41423', 'up': True, 'percentChange': '1.51%'}, {'stockSymbol': 'ETH', 'url': 'https://logo.clearbit.com/ethereum.org', 'currentPrice': '3106.70', 'up': True, 'percentChange': '2.26%'}, {'stockSymbol': 'DOGE', 'url': 'https://logo.clearbit.com/dogecoin.com', 'currentPrice': '0.1426', 'up': True, 'percentChange': '2.06%'}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hawks', 'name': 'ATL', 'colors': {'main': [200, 16, 46], 'secondary': [255, 255, 255]}, 'record': '27-14'}, 'homeTeam': {'teamName': 'Heat', 'name': 'MIA', 'colors': {'main': [134, 38, 51], 'secondary': [0, 0, 0]}, 'record': '43-39'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Miami Heat', 'price': -320}, 'away': {'name': 'Atlanta Hawks', 'price': 260}}, 'spread': {'home': {'name': 'Miami Heat', 'price': -110, 'point': -8}, 'away': {'name': 'Atlanta Hawks', 'price': -110, 'point': 8}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 220}, 'under': {'name': 'Under', 'price': -110, 'point': 220}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Timberwolves', 'name': 'MIN', 'colors': {'main': [0, 43, 92], 'secondary': [122, 193, 67]}, 'record': '26-15'}, 'homeTeam': {'teamName': 'Grizzlies', 'name': 'MEM', 'colors': {'main': [35, 55, 91], 'secondary': [97, 137, 185]}, 'record': '46-36'}, 'startTime': '8:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Memphis Grizzlies', 'price': -290}, 'away': {'name': 'Minnesota Timberwolves', 'price': 235}}, 'spread': {'home': {'name': 'Memphis Grizzlies', 'price': -106, 'point': -7}, 'away': {'name': 'Minnesota Timberwolves', 'price': -114, 'point': 7}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 240}, 'under': {'name': 'Under', 'price': -110, 'point': 240}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Pelicans', 'name': 'NO', 'colors': {'main': [0, 43, 92], 'secondary': [227, 25, 55]}, 'record': '19-22'}, 'homeTeam': {'teamName': 'Suns', 'name': 'PHX', 'colors': {'main': [229, 96, 32], 'secondary': [29, 17, 96]}, 'record': '36-46'}, 'startTime': '10:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Phoenix Suns', 'price': -560}, 'away': {'name': 'New Orleans Pelicans', 'price': 420}}, 'spread': {'home': {'name': 'Phoenix Suns', 'price': -114, 'point': -9.5}, 'away': {'name': 'New Orleans Pelicans', 'price': -105, 'point': 9.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 222}, 'under': {'name': 'Under', 'price': -110, 'point': 222}}}}, '']
            print(responseArr)
            canvas = self.matrix
            bases =  [[113,5],[108,0],[103,5]]
            outs = [[107,20],[113,20]]
            for item in responseArr:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(item)
                if type(item) is dict and 'league' in item.keys() and item['league'] == 'mlb':
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:
                        count = 0
                        testing = True
                        while testing:
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
                            oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                            for offset in range(13):
                                graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorPrimary)
                            for offset in range(13):
                                graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorPrimary)
                            awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                            homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
                            runningCount = oddsStartNum
                            awayMLOdds = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 10, green, str(awayMoneyLineString))
                            homeMLOdds = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 24, green, str(homeMoneyLineString))
                            runningCount = runningCount + homeMLOdds + 4
                            awaySpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, str(awaySpreadPointsString))
                            homeSpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeSpreadPointsString))
                            runningCount = runningCount + awaySpreadOddsPoints + 4
                            overOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, 'O/U')
                            underOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(underTotalPointsString))
                            runningCount = runningCount + underOddsPoints + 4
                            startTime = graphics.DrawText(canvas, smallestFont, 100, 32, yellow, item['startTime'])
                            homePitcher = 'J. Verlander 3-1 2.50'
                            awayPitcher = 'K. Something 3-1 5.50'
                            pitchers = [awayPitcher, homePitcher]
                            currentPitcher = graphics.DrawText(canvas, smallestFont, 0, 32, white, pitchers[count])
                            time.sleep(5)
                            canvas.Clear()
                            count = count + 1
                            if count == 3:
                                testing = False
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
                    elif item['postponed'] == True:
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
                        finalDetail = graphics.DrawText(canvas, slightlyBiggerFont, runningCount + 5, 20, yellow, 'Postponed')
                elif type(item) is dict and 'league' in item.keys() and item['league'] == 'nba':
                    print('+++++++++++++')
                    print(item)
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
                        awayTeamBlack = graphics.DrawText(canvas, smallFont, 1, 11, black, item['awayTeam']['teamName'])
                        homeTeamBlack = graphics.DrawText(canvas, smallFont, 1, 22, black, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeamBlack + 3 if awayTeamBlack > homeTeamBlack else homeTeamBlack + 3
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorPrimary)
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 11, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorSecondary, item['homeTeam']['teamName'])
                        runningCount = oddsStartNum
                        awayMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, str(awayMoneyLineString))
                        homeMLOdds = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeMoneyLineString))
                        runningCount = runningCount + homeMLOdds + 4
                        awaySpreadOddsPoints = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 10, green, str(awaySpreadPointsString))
                        homeSpreadOddsPoints = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 22, green, str(homeSpreadPointsString))
                        runningCount = runningCount + awaySpreadOddsPoints + 4
                        overOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, 'O/U')
                        underOddsPoints = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 22, green, str(underTotalPointsString))
                        runningCount = runningCount + underOddsPoints + 4
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
                    runningBuffer = 10
                    runningBlockBuffer = 0
                    for team in item['standings']:
                        print(team)
                        print(runningBuffer)
                        teamColorPrimary = graphics.Color(team['colors']['main'][0],team['colors']['main'][1],team['colors']['main'][2])
                        teamColorSecondary = graphics.Color(team['colors']['secondary'][0],team['colors']['secondary'][1],team['colors']['secondary'][2])
                        teamBlack = graphics.DrawText(canvas, middleFont, 1, 150, black, team['team'])
                        oddsStartNum = 35
                        for offset in range(17):
                            graphics.DrawLine(canvas, 0, offset + runningBlockBuffer, 50, offset + runningBlockBuffer, teamColorPrimary)
                        teamName = graphics.DrawText(canvas, slightlyBiggerFont, 0, runningBuffer, teamColorSecondary, str(team['team']))
                        win = graphics.DrawText(canvas, slightlyBiggerFont, 55, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['win']))
                        loss = graphics.DrawText(canvas, slightlyBiggerFont, 80, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['loss']))
                        gamesBack = graphics.DrawText(canvas, slightlyBiggerFont, 100, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['gamesBack']))
                        runningBuffer = runningBuffer + 11
                        runningBlockBuffer = runningBlockBuffer + 11
                elif type(item) is dict and 'temp' in item.keys():
                    # locationString = '/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    # weatherImage = Image.open(locationString).convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    print(item['condition'])
                    color = blue
                    if 'Rain' in item['condition'] or 'rain' in item['condition']:
                        canvas.SetImage(rainImage, 0, 0)
                        color = blue
                    elif 'CLOUDY' in item['condition'] or 'Overcast' in item['condition'] or 'cloudy' in item['condition'] or 'overcast' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 0)
                        color = yellow
                    elif 'THUNDER' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 0)
                        color = blue
                    elif 'Sun' in item['condition'] or 'SUN' in item['condition']:
                        canvas.SetImage(sunnyImage, 0, 0)
                        color = yellow
                    currentTemp = graphics.DrawText(canvas, font, 32, 31, color, item['temp'])
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 40, 2, black, item['condition'])
                    print(weatherConditionText)
                    centered = 75 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, alilbiggerFont, centered, 8, blue, item['condition'])
                    highLow = graphics.DrawText(canvas, slightlyBiggerFont, 73, 22, green, item['highLow'])
                    rainChance = graphics.DrawText(canvas, alilbiggerFont, 78, 30, blue, 'Rain: {}'.format(item['rainPercent']))
                elif type(item) is dict and 'condition' in item.keys():
                    # locationString = '/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    # weatherImage = Image.open(locationString).convert('RGB').resize((22, 22), Image.ANTIALIAS)
                    partlyCloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    thunderstormImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    cloudyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    rainImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    stormyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    sunnyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    windyImage = Image.open('/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((36, 36), Image.ANTIALIAS)
                    print(item['condition'])
                    color = blue
                    if 'RAIN' in item['condition'] or 'rain' in item['condition']:
                        canvas.SetImage(rainImage, 0, 0)
                        color = blue
                    elif 'CLOUDY' in item['condition'] or 'Overcast' in item['condition'] or 'cloudy' in item['condition'] or 'overcast' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 0)
                        color = yellow
                    elif 'Thunder' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 0)
                        color = blue
                    elif 'Sun' in item['condition'] or 'sun' in item['condition']:
                        canvas.SetImage(sunnyImage, 0, 0)
                        color = yellow
                    dayOfWeek = graphics.DrawText(canvas, middleFont, 36, 24, color, item['day'])
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 40, 2, black, item['condition'])
                    print(weatherConditionText)
                    centered = 75 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, alilbiggerFont, centered, 8, blue, item['condition'])
                    highLow = graphics.DrawText(canvas, slightlyBiggerFont, 73, 22, green, item['highLow'])
                    rainChance = graphics.DrawText(canvas, alilbiggerFont, 78, 30, blue, 'Rain: {}'.format(item['rainPercent']))
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
                    offscreen_canvas = self.matrix.CreateFrameCanvas()
                    pos = offscreen_canvas.width
                    print(item)
                    running = True
                    while running:
                        offscreen_canvas.Clear()
                        tournamentNameBlack = graphics.DrawText(canvas, slightlyBiggerFont, 0, 10, black, item['tourneyName'])
                        tourneyStatusBlack = graphics.DrawText(canvas, smallestFont, 0, 16, black, item['status'])
                        nameCentered = 64 - (tournamentNameBlack / 2)
                        statusCentered = 64 - (tourneyStatusBlack / 2)
                        tournamentName = graphics.DrawText(canvas, slightlyBiggerFont, nameCentered, 10, blue, item['tourneyName'])
                        tourneyStatus = graphics.DrawText(canvas, smallestFont, statusCentered, 16, lightblue, item['status'])
                        pos -= 1
                        topGolfers = graphics.DrawText(offscreen_canvas, middleFont, pos, 28, green, item['topGolfers'])
                        if (pos + topGolfers < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.02)
                        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                elif type(item) is dict and item['type'] == 'rssFeed':
                    print(item)
                    offscreen_canvas = self.matrix.CreateFrameCanvas()
                    pos = offscreen_canvas.width
                    running = True
                    while running:
                        offscreen_canvas.Clear()
                        tournamentNameBlack = graphics.DrawText(canvas, slightlyBiggerFont, 0, 10, black, item['name'])
                        nameCentered = 64 - (tournamentNameBlack / 2)
                        tournamentName = graphics.DrawText(canvas, slightlyBiggerFont, nameCentered, 10, red, item['name'])
                        pos -= 1
                        topGolfers = graphics.DrawText(offscreen_canvas, middleFont, pos, 25, blue, item['feed'])
                        if (pos + topGolfers < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.02)
                        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                else:
                    currentTime = graphics.DrawText(canvas, font, 0, 23, blue, item)
                time.sleep(10)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()