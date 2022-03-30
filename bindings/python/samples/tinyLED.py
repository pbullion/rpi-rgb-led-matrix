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
            colors = [blue, teal, purple, yellow]
            randomNum = random.randint(0,3)
            font = graphics.Font()
            font.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallestFont = graphics.Font()
            smallestFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/4x6.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            # responseArr = json.loads(url.text)
            responseArr = [
                {
                    "stockSymbol": "TSLA",
                    "url": "https://logo.clearbit.com/tesla.com",
                    "currentPrice": "1099.57",
                    "up": True,
                    "percentChange": "0.71%"
                },
                {
                    "stockSymbol": "OBNK",
                    "url": "https://logo.clearbit.com/originbank.com",
                    "currentPrice": "43.88",
                    "up": True,
                    "percentChange": "0.69%"
                },
                {
                    "stockSymbol": "STEM",
                    "url": "https://logo.clearbit.com/stem.com",
                    "currentPrice": "11.58",
                    "up": True,
                    "percentChange": "6.14%"
                },
                {
                    "stockSymbol": "AAPL",
                    "url": "https://logo.clearbit.com/apple.com",
                    "currentPrice": "178.96",
                    "up": True,
                    "percentChange": "1.91%"
                },
                {
                    "stockSymbol": "AMC",
                    "url": "https://logo.clearbit.com/amctheatres.com",
                    "currentPrice": "29.44",
                    "up": True,
                    "percentChange": "0.38%"
                },
                {
                    "stockSymbol": "AMD",
                    "url": "https://logo.clearbit.com/amd.com",
                    "currentPrice": "123.23",
                    "up": True,
                    "percentChange": "2.49%"
                },
                {
                    "stockSymbol": "HOOD",
                    "url": "https://logo.clearbit.com/robinhood.com",
                    "currentPrice": "15.91",
                    "up": True,
                    "percentChange": "24.20%"
                },
                {
                    "stockSymbol": "BTC",
                    "url": "https://logo.clearbit.com/bitcoin.org",
                    "currentPrice": "47061",
                    "up": False,
                    "percentChange": "0.87%"
                },
                {
                    "stockSymbol": "ETH",
                    "url": "https://logo.clearbit.com/ethereum.org",
                    "currentPrice": "3362.86",
                    "up": False,
                    "percentChange": "0.44%"
                },
                {
                    "stockSymbol": "DOGE",
                    "url": "https://logo.clearbit.com/dogecoin.com",
                    "currentPrice": "0.1415",
                    "up": False,
                    "percentChange": "2.61%"
                },
                "",
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "WSH",
                    "score": "1",
                    "colors": {
                        "main": [
                        10,
                        41,
                        93
                        ],
                        "secondary": [
                        241,
                        242,
                        243
                        ]
                    },
                    "record": "0-5"
                    },
                    "homeTeam": {
                    "name": "HOU",
                    "score": "3",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        235,
                        110,
                        31
                        ]
                    },
                    "record": "1-9"
                    },
                    "winningPitcher": "J. Verlander 2-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "BOS",
                    "score": "2",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        13,
                        43,
                        86
                        ]
                    },
                    "record": "5-1"
                    },
                    "homeTeam": {
                    "name": "PIT",
                    "score": "6",
                    "colors": {
                        "main": [
                        17,
                        17,
                        17
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "7-5"
                    },
                    "winningPitcher": "M. Keller 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "MIN",
                    "score": "2",
                    "colors": {
                        "main": [
                        1,
                        39,
                        86
                        ],
                        "secondary": [
                        241,
                        242,
                        243
                        ]
                    },
                    "record": "3-2"
                    },
                    "homeTeam": {
                    "name": "TB",
                    "score": "4",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        143,
                        188,
                        230
                        ]
                    },
                    "record": "4-8"
                    },
                    "winningPitcher": "J.P. Feyereisen 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "PHI",
                    "score": "2",
                    "colors": {
                        "main": [
                        190,
                        0,
                        17
                        ],
                        "secondary": [
                        40,
                        72,
                        152
                        ]
                    },
                    "record": "5-0"
                    },
                    "homeTeam": {
                    "name": "NYY",
                    "score": "14",
                    "colors": {
                        "main": [
                        1,
                        23,
                        57
                        ],
                        "secondary": [
                        196,
                        206,
                        212
                        ]
                    },
                    "record": "6-4"
                    },
                    "winningPitcher": "C. Schmidt 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "ARI",
                    "score": "2",
                    "colors": {
                        "main": [
                        164,
                        0,
                        19
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "3-2"
                    },
                    "homeTeam": {
                    "name": "CHC",
                    "score": "3",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "5-7"
                    },
                    "winningPitcher": "J. Steele 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "MIL",
                    "score": "3",
                    "colors": {
                        "main": [
                        5,
                        12,
                        51
                        ],
                        "secondary": [
                        241,
                        242,
                        243
                        ]
                    },
                    "record": "2-2"
                    },
                    "homeTeam": {
                    "name": "CLE",
                    "score": "10",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "4-5"
                    },
                    "winningPitcher": "B. Shaw 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "SD",
                    "score": "6",
                    "colors": {
                        "main": [
                        47,
                        36,
                        29
                        ],
                        "secondary": [
                        255,
                        196,
                        37
                        ]
                    },
                    "record": "3-1"
                    },
                    "homeTeam": {
                    "name": "SF",
                    "score": "11",
                    "colors": {
                        "main": [
                        22,
                        20,
                        21
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "4-5"
                    },
                    "winningPitcher": "C. Rodon 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "CIN",
                    "score": "7",
                    "colors": {
                        "main": [
                        196,
                        20,
                        34
                        ],
                        "secondary": [
                        255,
                        255,
                        255
                        ]
                    },
                    "record": "3-1"
                    },
                    "homeTeam": {
                    "name": "TEX",
                    "score": "1",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        192,
                        17,
                        31
                        ]
                    },
                    "record": "6-4"
                    },
                    "winningPitcher": "R. Sanmartin 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "LAA",
                    "score": "8",
                    "colors": {
                        "main": [
                        165,
                        0,
                        23
                        ],
                        "secondary": [
                        134,
                        38,
                        51
                        ]
                    },
                    "record": "4-2"
                    },
                    "homeTeam": {
                    "name": "COL",
                    "score": "2",
                    "colors": {
                        "main": [
                        34,
                        13,
                        72
                        ],
                        "secondary": [
                        34,
                        13,
                        72
                        ]
                    },
                    "record": "7-4"
                    },
                    "winningPitcher": "J. Suarez 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": False,
                    "final": True,
                    "awayTeam": {
                    "name": "KC",
                    "score": "11",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        122,
                        178,
                        221
                        ]
                    },
                    "record": "4-2"
                    },
                    "homeTeam": {
                    "name": "SEA",
                    "score": "4",
                    "colors": {
                        "main": [
                        1,
                        42,
                        91
                        ],
                        "secondary": [
                        12,
                        44,
                        86
                        ]
                    },
                    "record": "6-3"
                    },
                    "winningPitcher": "D. Lynch 1-0",
                    "finalDetail": "Final"
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": True,
                    "final": False,
                    "awayTeam": {
                    "name": "NYM",
                    "score": "10",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "4-1"
                    },
                    "homeTeam": {
                    "name": "MIA",
                    "score": "0",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        250,
                        250,
                        250
                        ]
                    },
                    "record": "5-3"
                    },
                    "inning": "End 7th",
                    "runners": {
                    "onFirst": False,
                    "onSecond": False,
                    "onThird": False
                    },
                    "situation": {
                    "balls": 0,
                    "strikes": 0,
                    "outs": 0
                    }
                },
                {
                    "league": "mlb",
                    "pregame": False,
                    "inprogress": True,
                    "final": False,
                    "awayTeam": {
                    "name": "OAK",
                    "score": "1",
                    "colors": {
                        "main": [
                        1,
                        67,
                        38
                        ],
                        "secondary": [
                        239,
                        178,
                        30
                        ]
                    },
                    "record": "2-2"
                    },
                    "homeTeam": {
                    "name": "LAD",
                    "score": "0",
                    "colors": {
                        "main": [
                        250,
                        250,
                        250
                        ],
                        "secondary": [
                        162,
                        170,
                        173
                        ]
                    },
                    "record": "2-7"
                    },
                    "inning": "End 2nd",
                    "runners": {
                    "onFirst": False,
                    "onSecond": False,
                    "onThird": False
                    },
                    "situation": {
                    "balls": 0,
                    "strikes": 0,
                    "outs": 0
                    }
                },
                {
                    "condition": "Overcast",
                    "icon": 122,
                    "temp": "74°",
                    "highLow": "68°/82°"
                },
                [
                    {
                    "day": "WED",
                    "rainPercent": "92%",
                    "condition": "Overcast",
                    "icon": 302,
                    "highLow": "67°/86°"
                    },
                    {
                    "day": "THU",
                    "rainPercent": "0%",
                    "condition": "Overcast",
                    "icon": 113,
                    "highLow": "58°/87°"
                    }
                ],
                "",
                "HELLLLLLLLOOOOO"
            ]
            canvas = self.matrix
            bases =  [[54,7],[49,2],[44,7]]
            outs = [[44,25],[50,25],[56,25]]
            print('here')
            print(responseArr)
            for item in responseArr:
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print(item)
                running = True
                len = 1
                if type(item) is dict and 'league' in item.keys() and item['league'] == 'mlb':
                    print('+++++++++++++')
                    print(item)
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
                        finalDetail = graphics.DrawText(canvas, smallFont, 25, 20, yellow, item['startTime'])
                        winningPitcher = graphics.DrawText(canvas, smallFont, 25, 31, green, item['odds'])
                    if item['final'] == True:    
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 24, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 24, homeColorSecondary, item['homeTeam']['score'])
                        finalDetail = graphics.DrawText(canvas, middleFont, 45, 20, yellow, 'F')
                        winningPitcher = graphics.DrawText(canvas, smallestFont, 0, 31, green, item['winningPitcher'])
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
                            size = 6
                            half = round(abs(size/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + size - offset, x + half + offset, y + size - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        elif item['runners']['onSecond'] == True:
                            x = bases[1][0]
                            y = bases[1][1]
                            size = 6
                            half = round(abs(size/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + size - offset, x + half + offset, y + size - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        elif item['runners']['onThird'] == True:
                            x = bases[2][0]
                            y = bases[2][1]
                            size = 6
                            half = round(abs(size/2))
                            for offset in range(1, half + 1):
                                graphics.DrawLine(canvas, x + half - offset, y + size - offset, x + half + offset, y + size - offset, yellow)
                                graphics.DrawLine(canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
                        if item['situation']['outs'] == 1:
                            outsSize = 3
                            x = outs[0][0]
                            y = outs[0][1]
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                        elif item['situation']['outs'] == 2:
                            outsSize = 3
                            x = outs[1][0]
                            y = outs[1][1]
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                        elif item['situation']['outs'] == 3:
                            outsSize = 3
                            x = outs[2][0]
                            y = outs[2][1]
                            for y_offset in range(outsSize):
                                graphics.DrawLine(canvas, outs[0][0], outs[0][1] + y_offset, outs[0][0] + outsSize, outs[0][1] + y_offset, red)
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 22, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 22, homeColorSecondary, item['homeTeam']['score'])
                        count = graphics.DrawText(canvas, smallestFont, 47, 22, yellow, situationString)
                        inning = graphics.DrawText(canvas, smallestFont, 0, 29, yellow, item['inning'])
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
                elif type(item) is dict and 'stockSymbol' in item.keys() :
                    color = green if item['up'] else red
                    direction = 1 if item['up'] else -1
                    stockLogo = Image.open(requests.get(item['url'], stream=True).raw).convert('RGB').resize((20,20), Image.ANTIALIAS)
                    canvas.SetImage(stockLogo, 2, 3)
                    stockSymbol = graphics.DrawText(canvas, middleFont, 25, 12, color, item['stockSymbol'])
                    currentPrice = graphics.DrawText(canvas, smallestFont, 30, 19, color, item['currentPrice'])
                    x = 27
                    y = 30 if item['up'] else 26
                    size = 4
                    for offset in range(size):
                        graphics.DrawLine(canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)
                    percentChange = graphics.DrawText(canvas, smallFont, 32, 29, color, item['percentChange'])
                elif type(item) is dict and 'condition' in item.keys() :
                    locationString = '/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    weatherImage = Image.open(locationString).convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    canvas.SetImage(weatherImage, 0)
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 39, 10, blue, item['condition'])
                    currentTemp = graphics.DrawText(canvas, smallFont, 39, 20, blue, item['temp'])
                    highLow = graphics.DrawText(canvas, smallestFont, 42, 40, blue, item['highLow'])
                elif type(item) is list and 'condition' in item[0].values():
                    runningX = 0
                    runningY = 10
                    for day in item:
                        locationString = '/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(day['icon'])
                        weatherImage = Image.open(locationString).convert('RGB').resize((8, 8), Image.ANTIALIAS)
                        dayText = graphics.DrawText(canvas, smallestFont, runningX, 10, blue, day['day'])
                        canvas.SetImage(weatherImage, runningX, 15)
                        weatherConditionText = graphics.DrawText(canvas, smallestFont, runningX, 30, blue, day['condition'])
                        currentTemp = graphics.DrawText(canvas, smallFont, runningX, 36, blue, day['temp'])
                        highLow = graphics.DrawText(canvas, smallestFont, runningX, 40, blue, day['highLow'])
                        runningX = runningX + 20
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
                        time.sleep(7)
                        canvas.Clear()
                else:
                    print('there was nothing')
                time.sleep(4)
                canvas.Clear()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()