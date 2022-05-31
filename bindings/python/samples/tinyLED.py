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
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            responseArr = json.loads(url.text)
            # responseArr = [{'stockSymbol': 'TSLA', 'url': 'https://logo.clearbit.com/tesla.com', 'currentPrice': '999.58', 'up': False, 'percentChange': '2.78%'}, {'stockSymbol': 'OBNK', 'url': 'https://logo.clearbit.com/originbank.com', 'currentPrice': '42.40', 'up': True, 'percentChange': '1.56%'}, {'stockSymbol': 'AAPL', 'url': 'https://logo.clearbit.com/apple.com', 'currentPrice': '167.95', 'up': True, 'percentChange': '0.33%'}, {'stockSymbol': 'TWTR', 'url': 'https://logo.clearbit.com/twitter.com', 'currentPrice': '45.70', 'up': False, 'percentChange': '0.99%'}, {'stockSymbol': 'BTC', 'url': 'https://logo.clearbit.com/bitcoin.org', 'currentPrice': '41637', 'up': True, 'percentChange': '0.19%'}, {'stockSymbol': 'ETH', 'url': 'https://logo.clearbit.com/ethereum.org', 'currentPrice': '3103.48', 'up': False, 'percentChange': '0.32%'}, {'stockSymbol': 'DOGE', 'url': 'https://logo.clearbit.com/dogecoin.com', 'currentPrice': '0.1426', 'up': True, 'percentChange': '0.55%'}, {'league': 'nba', 'pregame': False, 'inProgress': False, 'final': True, 'awayTeam': {'teamName': 'Hawks', 'name': 'ATL', 'score': '105', 'colors': {'main': [200, 16, 46], 'secondary': [255, 255, 255]}, 'record': '27-14'}, 'homeTeam': {'teamName': 'Heat', 'name': 'MIA', 'score': '115', 'colors': {'main': [134, 38, 51], 'secondary': [0, 0, 0]}, 'record': '43-39'}, 'winningPitcher': '', 'losingPitcher': '', 'finalDetail': 'Final'}, {'league': 'nba', 'pregame': False, 'inProgress': False, 'final': True, 'awayTeam': {'teamName': 'Timberwolves', 'name': 'MIN', 'score': '96', 'colors': {'main': [0, 43, 92], 'secondary': [122, 193, 67]}, 'record': '26-15'}, 'homeTeam': {'teamName': 'Grizzlies', 'name': 'MEM', 'score': '124', 'colors': {'main': [35, 55, 91], 'secondary': [97, 137, 185]}, 'record': '46-36'}, 'winningPitcher': '', 'losingPitcher': '', 'finalDetail': 'Final'}, {'league': 'nba', 'pregame': False, 'inProgress': False, 'final': True, 'awayTeam': {'teamName': 'Pelicans', 'name': 'NO', 'score': '125', 'colors': {'main': [0, 43, 92], 'secondary': [227, 25, 55]}, 'record': '19-22'}, 'homeTeam': {'teamName': 'Suns', 'name': 'PHX', 'score': '114', 'colors': {'main': [229, 96, 32], 'secondary': [29, 17, 96]}, 'record': '36-46'}, 'winningPitcher': '', 'losingPitcher': '', 'finalDetail': 'Final'}, '']
            print(responseArr)
            canvas = self.matrix
            bases =  [[115,5],[110,0],[105,5]]
            outs = [[108,20],[114,20]]
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
                        pregameCycle = True
                        pitchers = [item['awayTeam']['starter'], item['homeTeam']['starter']]
                        while pregameCycle:
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
                            awayMLOdds = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 10, green, str(awayMoneyLineString))
                            homeMLOdds = graphics.DrawText(canvas, slightlyBiggerFont, runningCount, 24, green, str(homeMoneyLineString))
                            runningCount = runningCount + homeMLOdds + 4
                            awaySpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, str(awaySpreadPointsString))
                            homeSpreadOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 22, green, str(homeSpreadPointsString))
                            runningCount = runningCount + awaySpreadOddsPoints + 4
                            overOddsPoints = graphics.DrawText(canvas, smallestFont, runningCount, 10, green, 'O/U')
                            underOddsPoints = graphics.DrawText(canvas, alilbiggerFont, runningCount, 22, green, str(underTotalPointsString))
                            runningCount = runningCount + underOddsPoints + 4
                            startTime = graphics.DrawText(canvas, alilbiggerFont, 103, 32, yellow, item['startTime'])
                            currentPitcher = graphics.DrawText(canvas, smallestFont, 0, 32, white, pitchers[count])
                            time.sleep(5)
                            count = count + 1
                            if count == 2:
                                pregameCycle = False
                            canvas.Clear()
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
                        awayScore = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                        homeScore = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                        runningCount = runningCount + homeScore + 10
                        homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['hits']['displayValue'])
                        awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['hits']['displayValue'])
                        runningCount = runningCount + homeHitTotal + 10
                        homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['errors']['displayValue'])
                        awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['errors']['displayValue'])
                        runningCount = runningCount + homeErrorTotal + 10
                        finalDetail = graphics.DrawText(canvas, middleFont, runningCount + 5, 20, yellow, 'F')
                        winningPitcher = graphics.DrawText(canvas, smallestFont, 0, 32, green, item['winningPitcher'])
                        losingPitcher = graphics.DrawText(canvas, smallestFont, 4 + winningPitcher, 32, red, item['losingPitcher'])                    
                        time.sleep(5)
                    elif item['inProgress'] == True: 
                        runningCount = 0
                        pregameCycle = True
                        players = [item['players']['currentPitcher'], item['players']['currentBatter']]
                        while pregameCycle:
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
                            awayScore = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['score'])
                            homeScore = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['score'])
                            runningCount = runningCount + homeScore + 10
                            homeHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['hits']['displayValue'])
                            awayHitTotal = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['hits']['displayValue'])
                            runningCount = runningCount + homeHitTotal + 10
                            homeErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 11, green if int(item['awayTeam']['score']) > int(item['homeTeam']['score']) else red, item['awayTeam']['errors']['displayValue'])
                            awayErrorTotal = graphics.DrawText(canvas, smallFont, runningCount, 24, green if int(item['homeTeam']['score']) > int(item['awayTeam']['score']) else red, item['homeTeam']['errors']['displayValue'])
                            count = count + homeErrorTotal + 5
                            count = graphics.DrawText(canvas, smallestFont, 108, 19, yellow, situationString)
                            inning = graphics.DrawText(canvas, smallestFont, 100, 31, yellow, item['inning'])
                            currentPlayers = graphics.DrawText(canvas, smallestFont, 0, 32, white, players[runningCount])
                            time.sleep(10)
                            runningCount = runningCount + 1
                            if runningCount == 2:
                                pregameCycle = False
                            canvas.Clear()
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
                        finalDetail = graphics.DrawText(canvas, alilbiggerFont, runningCount + 5, 20, yellow, 'Postponed')
                        time.sleep(5)
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
                    elif item['inProgress'] == True:    
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
                    time.sleep(15)
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
                    elif item['inProgress'] == True: 
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
                    currentPriceBlack = graphics.DrawText(canvas, smallFont, 150, 14, black, '${}'.format(item['currentPrice']))
                    currentPrice = graphics.DrawText(canvas, smallFont, 127 - currentPriceBlack, 14, color, '${}'.format(item['currentPrice']))
                    percentChangeBlack = graphics.DrawText(canvas, middleFont,150, 31, black, item['percentChange'])
                    x = 127 - percentChangeBlack - 8
                    y = 25 if item['up'] else 28
                    size = 4
                    for offset in range(size):
                        graphics.DrawLine(canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)
                    percentChange = graphics.DrawText(canvas, middleFont, 127 - percentChangeBlack, 31, color, item['percentChange'])
                    time.sleep(5)
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
                            graphics.DrawLine(canvas, 0, offset + runningBlockBuffer, 30, offset + runningBlockBuffer, teamColorPrimary)
                        teamName = graphics.DrawText(canvas, alilbiggerFont if team['team'] == 'Mariners' else  slightlyBiggerFont, 0, runningBuffer, teamColorSecondary, str(team['team']))
                        win = graphics.DrawText(canvas, slightlyBiggerFont, 35, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['win']))
                        loss = graphics.DrawText(canvas, slightlyBiggerFont, 60, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['loss']))
                        gamesBack = graphics.DrawText(canvas, slightlyBiggerFont, 80, runningBuffer, green if team['gamesBack'] == 0 else red, str(team['gamesBack']))
                        last10 = graphics.DrawText(canvas, smallestFont, 110, runningBuffer - 2, green if team['gamesBack'] == 0 else red, str(team['last10']))
                        runningBuffer = runningBuffer + 11
                        runningBlockBuffer = runningBlockBuffer + 11
                    time.sleep(5)
                elif type(item) is dict and 'temp' in item.keys():
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
                    elif 'CLOUDY' in item['condition'] or 'cloudy' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 0)
                        color = yellow
                    elif 'OVERCAST' in item['condition']:
                        canvas.SetImage(cloudyImage, 0, 0)
                        color = yellow
                    elif 'THUNDER' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 0)
                        color = blue
                    elif 'SUNNY' in item['condition']:
                        canvas.SetImage(sunnyImage, 0, 0)
                        color = yellow
                    currentTemp = graphics.DrawText(canvas, font, 32, 31, color, item['temp'])
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 40, 2, black, item['condition'])
                    print(weatherConditionText)
                    centered = 75 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, alilbiggerFont, centered, 8, blue, item['condition'])
                    highLow = graphics.DrawText(canvas, slightlyBiggerFont, 73, 22, green, item['highLow'])
                    rainChance = graphics.DrawText(canvas, alilbiggerFont, 78, 30, blue, 'Rain: {}'.format(item['rainPercent']))
                    time.sleep(5)
                elif type(item) is dict and 'condition' in item.keys():
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
                    elif 'CLOUDY' in item['condition']:
                        canvas.SetImage(partlyCloudyImage, 0, 0)
                        color = yellow
                    elif 'OVERCAST' in item['condition']:
                        canvas.SetImage(cloudyImage, 0, 0)
                        color = yellow
                    elif 'THUNDER' in item['condition'] or 'thunder' in item['condition']:
                        canvas.SetImage(thunderstormImage, 0, 0)
                        color = blue
                    elif 'SUNNY' in item['condition'] or item['condition'] == 'SUNNY':
                        canvas.SetImage(sunnyImage, 0, 0)
                        color = yellow
                    dayOfWeek = graphics.DrawText(canvas, middleFont, 36, 24, color, item['day'])
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 40, 2, black, item['condition'])
                    print(weatherConditionText)
                    centered = 75 - (weatherConditionText / 2)
                    weatherConditionText = graphics.DrawText(canvas, alilbiggerFont, centered, 8, blue, item['condition'])
                    highLow = graphics.DrawText(canvas, slightlyBiggerFont, 73, 22, green, item['highLow'])
                    rainChance = graphics.DrawText(canvas, alilbiggerFont, 78, 30, blue, 'Rain: {}'.format(item['rainPercent']))
                    time.sleep(5)
                elif type(item) is dict and 'tourneyName' in item.keys():
                    offscreen_canvas = self.matrix.CreateFrameCanvas()
                    pos = offscreen_canvas.width
                    print(item)
                    running = True
                    while running:
                        offscreen_canvas.Clear()
                        tournamentNameBlack = graphics.DrawText(canvas, alilbiggerFont, 0, 10, black, item['tourneyName'])
                        tourneyStatusBlack = graphics.DrawText(canvas, smallestFont, 0, 16, black, item['status'])
                        nameCentered = 64 - (tournamentNameBlack / 2)
                        statusCentered = 64 - (tourneyStatusBlack / 2)
                        tournamentName = graphics.DrawText(canvas, alilbiggerFont, nameCentered, 10, blue, item['tourneyName'])
                        tourneyStatus = graphics.DrawText(canvas, smallestFont, statusCentered, 16, lightblue, item['status'])
                        pos -= 1
                        topGolfers = graphics.DrawText(offscreen_canvas, slightlyBiggerFont, pos, 28, green, item['topGolfers'])
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
                        tournamentNameBlack = graphics.DrawText(canvas, middleFont, 0, 10, black, item['name'])
                        nameCentered = 64 - (tournamentNameBlack / 2)
                        tournamentName = graphics.DrawText(canvas, middleFont, nameCentered, 10, red, item['name'])
                        pos -= 1
                        topGolfers = graphics.DrawText(offscreen_canvas, slightlyBiggerFont, pos, 25, blue, item['feed'])
                        if (pos + topGolfers < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.015)
                        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                elif type(item) is dict and item['type'] == 'time':
                    currentDayBlack = graphics.DrawText(canvas, slightlyBiggerFont, 150, 5, black, item['day'])
                    currentMonthBlack = graphics.DrawText(canvas, slightlyBiggerFont, 150, 23, black, item['month'])
                    currentDateBlack = graphics.DrawText(canvas, slightlyBiggerFont, 150, 23, black, item['date'])
                    currentTime = graphics.DrawText(canvas, font, 0, 20, purple, item['time'])
                    currentTimeAmPm = graphics.DrawText(canvas, middleFont, currentTime + 4, 20, purple, item['amPM'])
                    currentDay = graphics.DrawText(canvas, slightlyBiggerFont, 64 - (currentDayBlack / 2), 30, green, item['day'])
                    currentMonth = graphics.DrawText(canvas, slightlyBiggerFont, 127 - currentMonthBlack, 9, yellow, item['month'])
                    currentDate = graphics.DrawText(canvas, slightlyBiggerFont, 127 - currentDateBlack, 21, yellow, item['date'])
                    time.sleep(5)
                else:
                    time.sleep(0)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()