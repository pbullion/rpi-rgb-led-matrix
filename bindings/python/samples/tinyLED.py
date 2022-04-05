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
            colors = [blue, teal, purple, yellow]
            randomNum = random.randint(0,3)
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
            # responseArr = json.loads(url.text)
            responseArr = [{'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Cardinals', 'name': 'STL', 'score': '7', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '13'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [184, 2, 32], 'secondary': [255, 255, 255]}, 'record': '5-2'}, 'homeTeam': {'teamName': 'Marlins', 'name': 'MIA', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '2'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '9-5'}, 'winningPitcher': 'S. Matz 1-1', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Pirates', 'name': 'PIT', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '5'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [17, 17, 17], 'secondary': [250, 250, 250]}, 'record': '4-2'}, 'homeTeam': {'teamName': 'Phillies', 'name': 'PHI', 'score': '5', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [190, 0, 17], 'secondary': [40, 72, 152]}, 'record': '7-7'}, 'winningPitcher': 'Z. Eflin 2-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Mets', 'name': 'NYM', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '3'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '5-3'}, 'homeTeam': {'teamName': 'Nationals', 'name': 'WSH', 'score': '14', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '20'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [10, 41, 93], 'secondary': [241, 242, 243]}, 'record': '7-7'}, 'winningPitcher': 'E. Fedde 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Rays', 'name': 'TB', 'score': '0', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '1'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [143, 188, 230]}, 'record': '4-4'}, 'homeTeam': {'teamName': 'Braves', 'name': 'ATL', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [250, 250, 250], 'secondary': [241, 242, 243]}, 'record': '6-10'}, 'winningPitcher': 'S. Newcomb 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Twins', 'name': 'MIN', 'score': '6', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [1, 39, 86], 'secondary': [241, 242, 243]}, 'record': '7-2'}, 'homeTeam': {'teamName': 'Red Sox', 'name': 'BOS', 'score': '10', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '11'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [13, 43, 86]}, 'record': '9-10'}, 'winningPitcher': 'H. Robles 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Tigers', 'name': 'DET', 'score': '5', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '11'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [255, 102, 0]}, 'record': '3-4'}, 'homeTeam': {'teamName': 'Yankees', 'name': 'NYY', 'score': '3', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '10'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [1, 23, 57], 'secondary': [196, 206, 212]}, 'record': '7-9'}, 'winningPitcher': 'M. Manning 1-1', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Orioles', 'name': 'BAL', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '6'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [32, 27, 27], 'secondary': [250, 250, 250]}, 'record': '6-2'}, 'homeTeam': {'teamName': 'Blue Jays', 'name': 'TOR', 'score': '2', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '5'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [250, 250, 250], 'secondary': [29, 45, 92]}, 'record': '8-8'}, 'winningPitcher': 'A. Cimber 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Mariners', 'name': 'SEA', 'score': '9', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '11'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [1, 42, 91], 'secondary': [12, 44, 86]}, 'record': '6-2'}, 'homeTeam': {'teamName': 'Reds', 'name': 'CIN', 'score': '12', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '12'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [196, 20, 34], 'secondary': [255, 255, 255]}, 'record': '9-7'}, 'winningPitcher': 'A. Diaz 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Cubs', 'name': 'CHC', 'score': '5', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '6'}, 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '8-2'}, 'homeTeam': {'teamName': 'Rangers', 'name': 'TEX', 'score': '11', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '10'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [250, 250, 250], 'secondary': [192, 17, 31]}, 'record': '11-7'}, 'winningPitcher': 'T. Hearn 3-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Royals', 'name': 'KC', 'score': '4', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '4'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [250, 250, 250], 'secondary': [122, 178, 221]}, 'record': '4-4'}, 'homeTeam': {'teamName': 'Brewers', 'name': 'MIL', 'score': '5', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [5, 12, 51], 'secondary': [241, 242, 243]}, 'record': '8-8'}, 'winningPitcher': 'S. Cruz 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'White Sox', 'name': 'CHW', 'score': '9', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '12'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '3'}, 'colors': {'main': [27, 21, 22], 'secondary': [196, 206, 212]}, 'record': '3-6'}, 'homeTeam': {'teamName': 'Padres', 'name': 'SD', 'score': '6', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [47, 36, 29], 'secondary': [255, 196, 37]}, 'record': '9-10'}, 'winningPitcher': 'T. Banks 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Guardians', 'name': 'CLE', 'score': '1', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '6'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '5-4'}, 'homeTeam': {'teamName': 'Diamondbacks', 'name': 'ARI', 'score': '3', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '4'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [164, 0, 19], 'secondary': [250, 250, 250]}, 'record': '7-11'}, 'winningPitcher': 'C. Booser 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': False, 'inprogress': True, 'final': False, 'awayTeam': {'teamName': 'Athletics', 'name': 'OAK', 'score': '7', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '12'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '0'}, 'colors': {'main': [1, 67, 38], 'secondary': [239, 178, 30]}, 'record': '4-4'}, 'homeTeam': {'teamName': 'Giants', 'name': 'SF', 'score': '4', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '9'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '2'}, 'colors': {'main': [22, 20, 21], 'secondary': [250, 250, 250]}, 'record': '5-10'}, 'inning': 'Top 9th', 'runners': {'onFirst': True, 'onSecond': False, 'onThird': False}, 'situation': {'balls': 0, 'strikes': 0, 'outs': 2}}, {'league': 'mlb', 'pregame': False, 'inprogress': False, 'final': True, 'awayTeam': {'teamName': 'Guardians', 'name': 'CLE', 'score': '3', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '8'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '5-4'}, 'homeTeam': {'teamName': 'Rockies', 'name': 'COL', 'score': '10', 'hits': {'name': 'hits', 'abbreviation': 'H', 'displayValue': '15'}, 'errors': {'name': 'errors', 'abbreviation': 'E', 'displayValue': '1'}, 'colors': {'main': [34, 13, 72], 'secondary': [34, 13, 72]}, 'record': '7-12'}, 'winningPitcher': 'A. Gomber 1-0', 'finalDetail': 'Final'}, {'league': 'mlb', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Angels', 'name': 'LAA', 'colors': {'main': [165, 0, 23], 'secondary': [134, 38, 51]}, 'record': '6-2'}, 'homeTeam': {'teamName': 'Dodgers', 'name': 'LAD', 'colors': {'main': [250, 250, 250], 'secondary': [162, 170, 173]}, 'record': '11-5'}, 'startTime': '9:10 PM EDT', 'weather': {'indoors': False, 'text': 'Sunny', 'temp': '75°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Los Angeles Dodgers', 'price': -168}, 'away': {'name': 'Los Angeles Angels', 'price': 142}}, 'spread': {'home': 'none', 'away': 'none'}, 'totals': {'over': 'none', 'under': 'none'}}}, {'day': 'CURRENT', 'condition': 'Sunny', 'rainPercent': '0%', 'icon': 113, 'temp': '91°', 'highLow': '68°/95°'}, {'day': 'WED', 'rainPercent': '0%', 'condition': 'Sunny', 'icon': 113, 'highLow': '66°/87°'}, {'day': 'THU', 'rainPercent': '0%', 'condition': 'Sunny', 'icon': 113, 'highLow': '58°/80°'}, {'stockSymbol': 'TSLA', 'url': 'https://logo.clearbit.com/tesla.com', 'currentPrice': '1091.26', 'up': False, 'percentChange': '4.73%'}, {'stockSymbol': 'OBNK', 'url': 'https://logo.clearbit.com/originbank.com', 'currentPrice': '41.31', 'up': False, 'percentChange': '0.91%'}, {'stockSymbol': 'STEM', 'url': 'https://logo.clearbit.com/stem.com', 'currentPrice': '11.72', 'up': False, 'percentChange': '3.54%'}, {'stockSymbol': 'AAPL', 'url': 'https://logo.clearbit.com/apple.com', 'currentPrice': '175.06', 'up': False, 'percentChange': '1.89%'}, {'stockSymbol': 'AMC', 'url': 'https://logo.clearbit.com/amctheatres.com', 'currentPrice': '21.21', 'up': False, 'percentChange': '9.01%'}, {'stockSymbol': 'AMD', 'url': 'https://logo.clearbit.com/amd.com', 'currentPrice': '106.82', 'up': False, 'percentChange': '3.36%'}, {'stockSymbol': 'HOOD', 'url': 'https://logo.clearbit.com/robinhood.com', 'currentPrice': '13.03', 'up': False, 'percentChange': '5.78%'}, {'stockSymbol': 'BTC', 'url': 'https://logo.clearbit.com/bitcoin.org', 'currentPrice': '45879', 'up': False, 'percentChange': '1.68%'}, {'stockSymbol': 'ETH', 'url': 'https://logo.clearbit.com/ethereum.org', 'currentPrice': '3446.71', 'up': False, 'percentChange': '2.27%'}, {'stockSymbol': 'DOGE', 'url': 'https://logo.clearbit.com/dogecoin.com', 'currentPrice': '0.1715', 'up': True, 'percentChange': '14.88%'}, [], ['game inprogress nba', 'https://loodibee.com/wp-content/uploads/nba-philadelphia-76ers-logo.png', 250, 250, 250, 'Philadelphia 76ers', 'https://loodibee.com/wp-content/uploads/nba-indiana-pacers-logo.png', 6, 22, 66, 'Indiana Pacers', '6:18 ', '17', '17', '1st'], ['game inprogress nba', 'https://loodibee.com/wp-content/uploads/nba-cleveland-cavaliers-logo.png', 6, 22, 66, 'Cleveland Cavaliers', 'https://loodibee.com/wp-content/uploads/nba-orlando-magic-logo.png', 8, 96, 168, 'Orlando Magic', '4:54 ', '19', '18', '1st'], {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Rockets', 'name': 'HOU', 'colors': {'main': [212, 0, 38], 'secondary': [196, 206, 211]}, 'record': '11-29'}, 'homeTeam': {'teamName': 'Nets', 'name': 'BKN', 'colors': {'main': [250, 250, 250], 'secondary': [255, 255, 255]}, 'record': '20-59'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Brooklyn Nets', 'price': -2200}, 'away': {'name': 'Houston Rockets', 'price': 1100}}, 'spread': {'home': {'name': 'Brooklyn Nets', 'price': -110, 'point': -17}, 'away': {'name': 'Houston Rockets', 'price': -110, 'point': 17}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 244}, 'under': {'name': 'Under', 'price': -110, 'point': 244}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hornets', 'name': 'CHA', 'colors': {'main': [29, 16, 96], 'secondary': [250, 250, 250]}, 'record': '20-19'}, 'homeTeam': {'teamName': 'Heat', 'name': 'MIA', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '40-38'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Miami Heat', 'price': -196}, 'away': {'name': 'Charlotte Hornets', 'price': 164}}, 'spread': {'home': {'name': 'Miami Heat', 'price': -110, 'point': -4.5}, 'away': {'name': 'Charlotte Hornets', 'price': -110, 'point': 4.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 225}, 'under': {'name': 'Under', 'price': -110, 'point': 225}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Hawks', 'name': 'ATL', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '26-14'}, 'homeTeam': {'teamName': 'Raptors', 'name': 'TOR', 'colors': {'main': [206, 15, 65], 'secondary': [6, 25, 34]}, 'record': '41-37'}, 'startTime': '7:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Toronto Raptors', 'price': -166}, 'away': {'name': 'Atlanta Hawks', 'price': 140}}, 'spread': {'home': {'name': 'Toronto Raptors', 'price': -110, 'point': -4}, 'away': {'name': 'Atlanta Hawks', 'price': -110, 'point': 4}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 226}, 'under': {'name': 'Under', 'price': -110, 'point': 226}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Bucks', 'name': 'MIL', 'colors': {'main': [250, 250, 250], 'secondary': [240, 235, 210]}, 'record': '26-14'}, 'homeTeam': {'teamName': 'Bulls', 'name': 'CHI', 'colors': {'main': [250, 250, 250], 'secondary': [250, 250, 250]}, 'record': '48-30'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Chicago Bulls', 'price': 235}, 'away': {'name': 'Milwaukee Bucks', 'price': -290}}, 'spread': {'home': {'name': 'Chicago Bulls', 'price': -114, 'point': 7}, 'away': {'name': 'Milwaukee Bucks', 'price': -106, 'point': -7}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 231}, 'under': {'name': 'Under', 'price': -110, 'point': 231}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Wizards', 'name': 'WSH', 'colors': {'main': [14, 55, 100], 'secondary': [227, 24, 55]}, 'record': '21-19'}, 'homeTeam': {'teamName': 'Timberwolves', 'name': 'MIN', 'colors': {'main': [14, 55, 100], 'secondary': [196, 206, 211]}, 'record': '34-44'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Minnesota Timberwolves', 'price': -770}, 'away': {'name': 'Washington Wizards', 'price': 540}}, 'spread': {'home': {'name': 'Minnesota Timberwolves', 'price': -110, 'point': -11.5}, 'away': {'name': 'Washington Wizards', 'price': -110, 'point': 11.5}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 239.5}, 'under': {'name': 'Under', 'price': -108, 'point': 239.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Trail Blazers', 'name': 'POR', 'colors': {'main': [250, 250, 250], 'secondary': [186, 195, 201]}, 'record': '17-23'}, 'homeTeam': {'teamName': 'Thunder', 'name': 'OKC', 'colors': {'main': [198, 124, 3], 'secondary': [240, 81, 51]}, 'record': '27-51'}, 'startTime': '8:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Oklahoma City Thunder', 'price': -174}, 'away': {'name': 'Portland Trail Blazers', 'price': 146}}, 'spread': {'home': {'name': 'Oklahoma City Thunder', 'price': -110, 'point': -4}, 'away': {'name': 'Portland Trail Blazers', 'price': -110, 'point': 4}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 221.5}, 'under': {'name': 'Under', 'price': -110, 'point': 221.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Spurs', 'name': 'SA', 'colors': {'main': [250, 250, 250], 'secondary': [6, 25, 34]}, 'record': '16-24'}, 'homeTeam': {'teamName': 'Nuggets', 'name': 'DEN', 'colors': {'main': [8, 96, 168], 'secondary': [253, 185, 39]}, 'record': '33-45'}, 'startTime': '9:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Denver Nuggets', 'price': -390}, 'away': {'name': 'San Antonio Spurs', 'price': 310}}, 'spread': {'home': {'name': 'Denver Nuggets', 'price': -110, 'point': -9}, 'away': {'name': 'San Antonio Spurs', 'price': -110, 'point': 9}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 234}, 'under': {'name': 'Under', 'price': -110, 'point': 234}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Grizzlies', 'name': 'MEM', 'colors': {'main': [93, 118, 168], 'secondary': [115, 153, 198]}, 'record': '29-10'}, 'homeTeam': {'teamName': 'Jazz', 'name': 'UTAH', 'colors': {'main': [6, 20, 63], 'secondary': [249, 160, 27]}, 'record': '55-23'}, 'startTime': '9:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Utah Jazz', 'price': -240}, 'away': {'name': 'Memphis Grizzlies', 'price': 198}}, 'spread': {'home': {'name': 'Utah Jazz', 'price': -108, 'point': -6}, 'away': {'name': 'Memphis Grizzlies', 'price': -112, 'point': 6}}, 'totals': {'over': {'name': 'Over', 'price': -112, 'point': 225.5}, 'under': {'name': 'Under', 'price': -108, 'point': 225.5}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Pelicans', 'name': 'NO', 'colors': {'main': [250, 250, 250], 'secondary': [180, 151, 90]}, 'record': '18-21'}, 'homeTeam': {'teamName': 'Kings', 'name': 'SAC', 'colors': {'main': [57, 57, 150], 'secondary': [142, 144, 144]}, 'record': '34-44'}, 'startTime': '10:00 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Sacramento Kings', 'price': 295}, 'away': {'name': 'New Orleans Pelicans', 'price': -370}}, 'spread': {'home': {'name': 'Sacramento Kings', 'price': -108, 'point': 8}, 'away': {'name': 'New Orleans Pelicans', 'price': -112, 'point': -8}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 224}, 'under': {'name': 'Under', 'price': -110, 'point': 224}}}}, {'league': 'nba', 'pregame': True, 'inprogress': False, 'final': False, 'awayTeam': {'teamName': 'Lakers', 'name': 'LAL', 'colors': {'main': [84, 37, 130], 'secondary': [85, 37, 130]}, 'record': '20-20'}, 'homeTeam': {'teamName': 'Suns', 'name': 'PHX', 'colors': {'main': [35, 0, 106], 'secondary': [241, 242, 243]}, 'record': '31-47'}, 'startTime': '10:30 PM EDT', 'weather': {'indoors': True, 'temp': 'undefined°'}, 'fanDuel': {'moneyLine': {'home': {'name': 'Phoenix Suns', 'price': -1000}, 'away': {'name': 'Los Angeles Lakers', 'price': 660}}, 'spread': {'home': {'name': 'Phoenix Suns', 'price': -108, 'point': -13.5}, 'away': {'name': 'Los Angeles Lakers', 'price': -114, 'point': 13.5}}, 'totals': {'over': {'name': 'Over', 'price': -110, 'point': 234.5}, 'under': {'name': 'Under', 'price': -110, 'point': 234.5}}}}]
            canvas = self.matrix
            bases =  [[93,5],[88,0],[83,5]]
            outs = [[83,20],[89,20],[95,20]]
            print('here')
            print(responseArr)
            for item in responseArr:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(item)
                running = True
                if type(item) is dict and 'league' in item.keys() and item['league'] == 'mlb':
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:
                        partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((22, 22), Image.ANTIALIAS)
                        awayTeam = graphics.DrawText(canvas, smallFont, 2, 7, awayColorSecondary, item['awayTeam']['teamName'])
                        awayTeamStandings = graphics.DrawText(canvas, smallestFont, 8 + awayTeam, 4, awayColorSecondary, item['awayTeam']['record'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 2, 22, homeColorSecondary, item['homeTeam']['teamName'])
                        homeTeamStandings = graphics.DrawText(canvas, smallestFont, 8 + homeTeam, 4, homeColorSecondary, item['homeTeam']['record'])
                        oddsStartNum = awayTeam + 8 + awayTeamStandings if awayTeam > homeTeam else homeTeam + 8 + homeTeamStandings
                        runningCount = oddsStartNum
                        homeMLOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['moneyLine']['home']['price'])
                        awayMLOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['moneyLine']['away']['price'])
                        runningCount = runningCount + homeMLOdds + 5
                        homeSpreadOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['spread']['home']['price'])
                        awaySpreadOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['spread']['away']['price'])
                        runningCount = runningCount + homeSpreadOdds + 5
                        homeTotalsOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['totals']['home']['price'])
                        awayTotalsOdds = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['fanDuel']['totals']['away']['price'])
                        runningCount = runningCount + homeTotalsOdds + 5
                        if 'Rain' in item['weather']['text'] or 'rain' in item['weather']['text']:
                            canvas.SetImage(rainImage, runningCount, 2)
                        elif 'Cloudy' in item['weather']['text'] or 'Overcast' in item['weather']['text'] or 'cloudy' in item['weather']['text'] or 'overcast' in item['weather']['text']:
                            canvas.SetImage(partlyCloudyImage, runningCount, 2)
                        elif 'Thunder' in item['weather']['text'] or 'thunder' in item['weather']['text']:
                            canvas.SetImage(thunderstormImage, runningCount, 2)
                        elif 'Sun' in item['weather']['text'] or 'sun' in item['weather']['text']:
                            canvas.SetImage(sunnyImage, runningCount, 2)
                        weatherTemp = graphics.DrawText(canvas, smallFont, runningCount + 5, 24, yellow, item['weather']['temp'])
                        startTime = graphics.DrawText(canvas, smallFont, runningCount, 304, yellow, item['startTime'])
                    if item['final'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 2, 7, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 2, 22, homeColorSecondary, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeam + 8 if awayTeam > homeTeam else homeTeam + 8
                        runningCount = oddsStartNum
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 7, green, item['awayTeam']['score'])
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 7, green, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 10
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 7, green, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['errors']['displayValue'])
                        runningCount = runningCount + homeErrorTotal + 10
                        winningPitcher = graphics.DrawText(canvas, alilbiggerFont, 0, 30, green, "WP: {}".format(item['winningPitcher']))
                        finalDetail = graphics.DrawText(canvas, middleFont, runningCount + 5, 20, yellow, 'F')
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
                        awayTeam = graphics.DrawText(canvas, smallFont, 2, 7, awayColorSecondary, item['awayTeam']['teamName'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 2, 22, homeColorSecondary, item['homeTeam']['teamName'])
                        oddsStartNum = awayTeam + 8 + awayTeamStandings if awayTeam > homeTeam else homeTeam + 8 + homeTeamStandings
                        runningCount = oddsStartNum
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['awayTeam']['score'])
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 5
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 5
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 4, green, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 22, green, item['homeTeam']['errors']['displayValue'])
                        runningCount = runningCount + homeErrorTotal + 5
                        count = graphics.DrawText(canvas, smallestFont, 83, 19, yellow, situationString)
                        inning = graphics.DrawText(canvas, smallestFont, 81, 31, yellow, item['inning'])
                elif type(item) is dict and 'league' in item.keys() and item['league'] == 'nba':
                    print('+++++++++++++')
                    print(item)
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
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
                    stockLogo = Image.open(requests.get(item['url'], stream=True).raw).convert('RGB').resize((20,20), Image.ANTIALIAS)
                    canvas.SetImage(stockLogo, 2, 3)
                    stockSymbol = graphics.DrawText(canvas, middleFont, 25 if len(item['stockSymbol']) > 3 else 28, 12, color, item['stockSymbol'])
                    currentPrice = graphics.DrawText(canvas, alilbiggerFont, 29, 20, color, item['currentPrice'])
                    x = 22
                    y = 25 if item['up'] else 28
                    size = 4
                    for offset in range(size):
                        graphics.DrawLine(canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)
                    percentChange = graphics.DrawText(canvas, smallFont, 29, 31, color, item['percentChange'])
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
                time.sleep(4)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()