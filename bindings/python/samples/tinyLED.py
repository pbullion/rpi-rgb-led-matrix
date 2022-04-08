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
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            responseArr = json.loads(url.text)
            # responseArr = [{'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Red Sox', 'name': 'BOS', 'colors': {'main': [250, 250, 250], 'secondary': [13, 43, 86]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Yankees', 'name': 'NYY', 'colors': {'main': [1, 23, 57], 'secondary': [196, 206, 212]}, 'record': '0-0'}, 'startTime': '1:05 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '58°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'New York Yankees', 'price': -174}, 'away': {'name': 'Boston Red Sox', 'price': 146}}, 'spread': {'home': {'name': 'New York Yankees', 'price': 118, 'point': -1.5}, 'away': {'name': 'Boston Red Sox', 'price': -142, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 8}, 'under': {'name': 'Under', 'price': -108, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'White Sox', 'name': 'CHW', 'colors': {'main': [27, 21, 22], 'secondary': [196, 206, 212]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Tigers', 'name': 'DET', 'colors': {'main': [250, 250, 250], 'secondary': [255, 102, 0]}, 'record': '0-0'}, 'startTime': '1:10 PM EDT', 'weather': {'indoors': False, 'text': 'Cloudy', 'temp': '45°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Detroit Tigers', 'price': 116}, 'away': {'name': 'Chicago White Sox', 'price': -136}}, 'spread': {'home': {'name': 'Detroit Tigers', 'price': -146, 'point': 1.5}, 'away': {'name': 'Chicago White Sox', 'price': 122, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -115, 'point': 7.5}, 'under': {'name': 'Under', 'price': -105, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Brewers', 'name': 'MIL', 'colors': {'main': [5, 12, 51], 'secondary': [241, 242, 243]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Cubs', 'name': 'CHC', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '0-1'}, 'startTime': '2:20 PM EDT', 'weather': {'indoors': False, 'text': 'Cloudy', 'temp': '39°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Chicago Cubs', 'price': 130}, 'away': {'name': 'Milwaukee Brewers', 'price': -154}}, 'spread': {'home': {'name': 'Chicago Cubs', 'price': -137, 'point': 1.5}, 'away': {'name': 'Milwaukee Brewers', 'price': 114, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -128, 'point': 7}, 'under': {'name': 'Under', 'price': 104, 'point': 7}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Athletics', 'name': 'OAK', 'colors': {'main': [1, 67, 38], 'secondary': [239, 178, 30]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Phillies', 'name': 'PHI', 'colors': {'main': [190, 0, 17], 'secondary': [40, 72, 152]}, 'record': '0-0'}, 'startTime': '3:05 PM EDT', 'weather': {'indoors': False, 'text': 'Intermittent clouds', 'temp': '60°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Philadelphia Phillies', 'price': -196}, 'away': {'name': 'Oakland Athletics', 'price': 164}}, 'spread': {'home': {'name': 'Philadelphia Phillies', 'price': 100, 'point': -1.5}, 'away': {'name': 'Oakland Athletics', 'price': -120, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -106, 'point': 8}, 'under': {'name': 'Under', 'price': -114, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Orioles', 'name': 'BAL', 'colors': {'main': [32, 27, 27], 'secondary': [250, 250, 250]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Rays', 'name': 'TB', 'colors': {'main': [250, 250, 250], 'secondary': [143, 188, 230]}, 'record': '0-0'}, 'startTime': '3:10 PM EDT', 'weather': {'indoors': False, 'text': 'Mostly sunny', 'temp': '70°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Tampa Bay Rays', 'price': -188}, 'away': {'name': 'Baltimore Orioles', 'price': 158}}, 'spread': {'home': {'name': 'Tampa Bay Rays', 'price': 112, 'point': -1.5}, 'away': {'name': 'Baltimore Orioles', 'price': -134, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 7.5}, 'under': {'name': 'Under', 'price': -108, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Dodgers', 'name': 'LAD', 'colors': {'main': [250, 250, 250], 'secondary': [162, 170, 173]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Rockies', 'name': 'COL', 'colors': {'main': [34, 13, 72], 'secondary': [34, 13, 72]}, 'record': '0-0'}, 'startTime': '4:10 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '60°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Colorado Rockies', 'price': 176}, 'away': {'name': 'Los Angeles Dodgers', 'price': -210}}, 'spread': {'home': {'name': 'Colorado Rockies', 'price': 118, 'point': 1.5}, 'away': {'name': 'Los Angeles Dodgers', 'price': -142, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 11.5}, 'under': {'name': 'Under', 'price': -110, 'point': 11.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Mariners', 'name': 'SEA', 'colors': {'main': [1, 42, 91], 'secondary': [12, 44, 86]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Twins', 'name': 'MIN', 'colors': {'main': [1, 39, 86], 'secondary': [241, 242, 243]}, 'record': '0-0'}, 'startTime': '4:10 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '42°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Minnesota Twins', 'price': -118}, 'away': {'name': 'Seattle Mariners', 'price': 100}}, 'spread': {'home': {'name': 'Minnesota Twins', 'price': 164, 'point': -1.5}, 'away': {'name': 'Seattle Mariners', 'price': -200, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 8}, 'under': {'name': 'Under', 'price': -108, 'point': 8}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Marlins', 'name': 'MIA', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Giants', 'name': 'SF', 'colors': {'main': [22, 20, 21], 'secondary': [250, 250, 250]}, 'record': '0-0'}, 'startTime': '4:35 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '61°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'San Francisco Giants', 'price': -154}, 'away': {'name': 'Miami Marlins', 'price': 130}}, 'spread': {'home': {'name': 'San Francisco Giants', 'price': 138, 'point': -1.5}, 'away': {'name': 'Miami Marlins', 'price': -166, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -106, 'point': 7.5}, 'under': {'name': 'Under', 'price': -114, 'point': 7.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Mets', 'name': 'NYM', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Nationals', 'name': 'WSH', 'colors': {'main': [10, 41, 93], 'secondary': [241, 242, 243]}, 'record': '1-0'}, 'startTime': '7:05 PM EDT', 'weather': {'indoors': False, 'text': 'Mostly cloudy w/ showers', 'temp': '57°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Washington Nationals', 'price': 140}, 'away': {'name': 'New York Mets', 'price': -168}}, 'spread': {'home': {'name': 'Washington Nationals', 'price': -118, 'point': 1.5}, 'away': {'name': 'New York Mets', 'price': -102, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 8.5}, 'under': {'name': 'Under', 'price': -102, 'point': 8.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Rangers', 'name': 'TEX', 'colors': {'main': [250, 250, 250], 'secondary': [192, 17, 31]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Blue Jays', 'name': 'TOR', 'colors': {'main': [250, 250, 250], 'secondary': [29, 45, 92]}, 'record': '0-0'}, 'startTime': '7:07 PM EDT', 'weather': {'indoors': False, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Toronto Blue Jays', 'price': -166}, 'away': {'name': 'Texas Rangers', 'price': 140}}, 'spread': {'home': {'name': 'Toronto Blue Jays', 'price': 116, 'point': -1.5}, 'away': {'name': 'Texas Rangers', 'price': -140, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 9}, 'under': {'name': 'Under', 'price': -102, 'point': 9}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Reds', 'name': 'CIN', 'colors': {'main': [196, 20, 34], 'secondary': [255, 255, 255]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Braves', 'name': 'ATL', 'colors': {'main': [250, 250, 250], 'secondary': [241, 242, 243]}, 'record': '1-0'}, 'startTime': '7:20 PM EDT', 'weather': {'indoors': False, 'text': 'Partly sunny', 'temp': '50°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Atlanta Braves', 'price': -196}, 'away': {'name': 'Cincinnati Reds', 'price': 164}}, 'spread': {'home': {'name': 'Atlanta Braves', 'price': 104, 'point': -1.5}, 'away': {'name': 'Cincinnati Reds', 'price': -125, 'point': 1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 8.5}, 'under': {'name': 'Under', 'price': -102, 'point': 8.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Astros', 'name': 'HOU', 'colors': {'main': [250, 250, 250], 'secondary': [235, 110, 31]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'Angels', 'name': 'LAA', 'colors': {'main': [165, 0, 23], 'secondary': [134, 38, 51]}, 'record': '1-0'}, 'startTime': '9:38 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '94°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Los Angeles Angels', 'price': -126}, 'away': {'name': 'Houston Astros', 'price': 108}}, 'spread': {'home': {'name': 'Los Angeles Angels', 'price': -200, 'point': 1.5}, 'away': {'name': 'Houston Astros', 'price': 164, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -114, 'point': 9.5}, 'under': {'name': 'Under', 'price': -106, 'point': 9.5}}}}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Padres', 'name': 'SD', 'colors': {'main': [47, 36, 29], 'secondary': [255, 196, 37]}, 'record': '0-0'}, 'homeTeam': {'teamName': 'D-Backs', 'name': 'ARI', 'colors': {'main': [164, 0, 19], 'secondary': [250, 250, 250]}, 'record': '0-1'}, 'startTime': '9:40 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '93°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Arizona Diamondbacks', 'price': 116}, 'away': {'name': 'San Diego Padres', 'price': -136}}, 'spread': {'home': {'name': 'Arizona Diamondbacks', 'price': -137, 'point': 1.5}, 'away': {'name': 'San Diego Padres', 'price': 114, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -120, 'point': 9}, 'under': {'name': 'Under', 'price': -102, 'point': 9}}}}, {'day': 'CURRENT', 'condition': 'Sunny', 'rainPercent': '0%', 'icon': 113, 'temp': '70°', 'highLow': '55°/78°'}, {'day': 'SAT', 'rainPercent': '0%', 'condition': 'Sunny', 'icon': 113, 'highLow': '55°/87°'}, {'day': 'SUN', 'rainPercent': '77%', 'condition': 'Patchy Rain', 'icon': 176, 'highLow': '64°/80°'}, {'stockSymbol': 'TSLA', 'url': 'https://logo.clearbit.com/tesla.com', 'currentPrice': '1041.59', 'up': False, 'percentChange': '1.48%'}, {'stockSymbol': 'OBNK', 'url': 'https://logo.clearbit.com/originbank.com', 'currentPrice': '40.35', 'up': False, 'percentChange': '0.25%'}, {'stockSymbol': 'STEM', 'url': 'https://logo.clearbit.com/stem.com', 'currentPrice': '10.33', 'up': False, 'percentChange': '2.75%'}, {'stockSymbol': 'AAPL', 'url': 'https://logo.clearbit.com/apple.com', 'currentPrice': '171.51', 'up': False, 'percentChange': '0.36%'}, {'stockSymbol': 'AMC', 'url': 'https://logo.clearbit.com/amctheatres.com', 'currentPrice': '18.82', 'up': False, 'percentChange': '4.62%'}, {'stockSymbol': 'AMD', 'url': 'https://logo.clearbit.com/amd.com', 'currentPrice': '102.08', 'up': False, 'percentChange': '1.58%'}, {'stockSymbol': 'HOOD', 'url': 'https://logo.clearbit.com/robinhood.com', 'currentPrice': '11.26', 'up': False, 'percentChange': '6.71%'}, {'stockSymbol': 'BTC', 'url': 'https://logo.clearbit.com/bitcoin.org', 'currentPrice': '43618', 'up': True, 'percentChange': '0.34%'}, {'stockSymbol': 'ETH', 'url': 'https://logo.clearbit.com/ethereum.org', 'currentPrice': '3278.65', 'up': True, 'percentChange': '2.01%'}, {'stockSymbol': 'DOGE', 'url': 'https://logo.clearbit.com/dogecoin.com', 'currentPrice': '0.1476', 'up': True, 'percentChange': '3.36%'}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Bucks', 'name': 'MIL', 'colors': {'main': [250, 250, 250], 'secondary': [240, 235, 210]}, 'record': '27-14'}, 'homeTeam': {'teamName': 'Pistons', 'name': 'DET', 'colors': {'main': [250, 0, 44], 'secondary': [250, 250, 250]}, 'record': '50-30'}, 'startTime': '7:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Detroit Pistons', 'price': 172}, 'away': {'name': 'Milwaukee Bucks', 'price': -205}}, 'spread': {'home': {'name': 'Detroit Pistons', 'price': -110, 'point': 4.5}, 'away': {'name': 'Milwaukee Bucks', 'price': -110, 'point': -4.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 227.5}, 'under': {'name': 'Under', 'price': -110, 'point': 227.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Knicks', 'name': 'NY', 'colors': {'main': [34, 94, 168], 'secondary': [245, 132, 38]}, 'record': '16-24'}, 'homeTeam': {'teamName': 'Wizards', 'name': 'WSH', 'colors': {'main': [14, 55, 100], 'secondary': [227, 24, 55]}, 'record': '35-45'}, 'startTime': '7:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Washington Wizards', 'price': 148}, 'away': {'name': 'New York Knicks', 'price': -176}}, 'spread': {'home': {'name': 'Washington Wizards', 'price': -108, 'point': 4}, 'away': {'name': 'New York Knicks', 'price': -112, 'point': -4}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 222.5}, 'under': {'name': 'Under', 'price': -110, 'point': 222.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Cavaliers', 'name': 'CLE', 'colors': {'main': [6, 22, 66], 'secondary': [253, 187, 48]}, 'record': '24-16'}, 'homeTeam': {'teamName': 'Nets', 'name': 'BKN', 'colors': {'main': [250, 250, 250], 'secondary': [255, 255, 255]}, 'record': '43-37'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Brooklyn Nets', 'price': -350}, 'away': {'name': 'Cleveland Cavaliers', 'price': 280}}, 'spread': {'home': {'name': 'Brooklyn Nets', 'price': -110, 'point': -8.5}, 'away': {'name': 'Cleveland Cavaliers', 'price': -110, 'point': 8.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 232.5}, 'under': {'name': 'Under', 'price': -110, 'point': 232.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Rockets', 'name': 'HOU', 'colors': {'main': [212, 0, 38], 'secondary': [196, 206, 211]}, 'record': '11-29'}, 'homeTeam': {'teamName': 'Raptors', 'name': 'TOR', 'colors': {'main': [206, 15, 65], 'secondary': [6, 25, 34]}, 'record': '20-60'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Toronto Raptors', 'price': -750}, 'away': {'name': 'Houston Rockets', 'price': 530}}, 'spread': {'home': {'name': 'Toronto Raptors', 'price': -110, 'point': -11}, 'away': {'name': 'Houston Rockets', 'price': -110, 'point': 11}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 227.5}, 'under': {'name': 'Under', 'price': -110, 'point': 227.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hawks', 'name': 'ATL', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '27-14'}, 'homeTeam': {'teamName': 'Heat', 'name': 'MIA', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '42-38'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Miami Heat', 'price': 104}, 'away': {'name': 'Atlanta Hawks', 'price': -122}}, 'spread': {'home': {'name': 'Miami Heat', 'price': -110, 'point': 1.5}, 'away': {'name': 'Atlanta Hawks', 'price': -110, 'point': -1.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 230}, 'under': {'name': 'Under', 'price': -110, 'point': 230}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hornets', 'name': 'CHA', 'colors': {'main': [29, 16, 96], 'secondary': [250, 250, 250]}, 'record': '21-19'}, 'homeTeam': {'teamName': 'Bulls', 'name': 'CHI', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '41-39'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Chicago Bulls', 'price': -138}, 'away': {'name': 'Charlotte Hornets', 'price': 118}}, 'spread': {'home': {'name': 'Chicago Bulls', 'price': -110, 'point': -2.5}, 'away': {'name': 'Charlotte Hornets', 'price': -110, 'point': 2.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 234}, 'under': {'name': 'Under', 'price': -110, 'point': 234}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Trail Blazers', 'name': 'POR', 'colors': {'main': [250, 250, 250], 'secondary': [186, 195, 201]}, 'record': '17-23'}, 'homeTeam': {'teamName': 'Mavericks', 'name': 'DAL', 'colors': {'main': [12, 71, 157], 'secondary': [196, 206, 211]}, 'record': '27-53'}, 'startTime': '8:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Dallas Mavericks', 'price': -4000}, 'away': {'name': 'Portland Trail Blazers', 'price': 1500}}, 'spread': {'home': {'name': 'Dallas Mavericks', 'price': -110, 'point': -19.5}, 'away': {'name': 'Portland Trail Blazers', 'price': -110, 'point': 19.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 219.5}, 'under': {'name': 'Under', 'price': -110, 'point': 219.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Suns', 'name': 'PHX', 'colors': {'main': [35, 0, 106], 'secondary': [241, 242, 243]}, 'record': '32-8'}, 'homeTeam': {'teamName': 'Jazz', 'name': 'UTAH', 'colors': {'main': [6, 20, 63], 'secondary': [249, 160, 27]}, 'record': '63-17'}, 'startTime': '9:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Utah Jazz', 'price': -130}, 'away': {'name': 'Phoenix Suns', 'price': 110}}, 'spread': {'home': {'name': 'Utah Jazz', 'price': -110, 'point': -2}, 'away': {'name': 'Phoenix Suns', 'price': -110, 'point': 2}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 228}, 'under': {'name': 'Under', 'price': -110, 'point': 228}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Thunder', 'name': 'OKC', 'colors': {'main': [198, 124, 3], 'secondary': [240, 81, 51]}, 'record': '12-29'}, 'homeTeam': {'teamName': 'Lakers', 'name': 'LAL', 'colors': {'main': [84, 37, 130], 'secondary': [85, 37, 130]}, 'record': '24-56'}, 'startTime': '10:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Los Angeles Lakers', 'price': -220}, 'away': {'name': 'Oklahoma City Thunder', 'price': 184}}, 'spread': {'home': {'name': 'Los Angeles Lakers', 'price': -110, 'point': -5.5}, 'away': {'name': 'Oklahoma City Thunder', 'price': -110, 'point': 5.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 227.5}, 'under': {'name': 'Under', 'price': -110, 'point': 227.5}}}}]
            print(responseArr)
            canvas = self.matrix
            bases =  [[113,5],[108,0],[103,5]]
            outs = [[103,20],[109,20],[115,20]]
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
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset, oddsStartNum - 3, offset, awayColorPrimary)
                        for offset in range(13):
                            graphics.DrawLine(canvas, 0, offset + 13, oddsStartNum - 3, offset + 13, homeColorPrimary)
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
                        # partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        # windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
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
                        gameFinalRunning = True
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
                time.sleep(5)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()