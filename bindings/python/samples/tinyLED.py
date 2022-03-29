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

    def __render_baserunner(self, base, color):
        x = base[0]
        y = base[1]
        size = 6
        half = abs(size/2)
        for offset in range(1, half+1):
            graphics.DrawLine(self.canvas, x + half - offset, y + size - offset, x + half + offset, y + size - offset, yellow)
            graphics.DrawLine(self.canvas, x + half - offset, y + offset, x + half + offset, y + offset, yellow)
    
    def __fill_circle(self, out, color):
        size = out["size"]
        x, y = (out["x"], out["y"])
        for y_offset in range(size):
            graphics.DrawLine(self.canvas, x, y + y_offset, x + size, y + y_offset, color)

    def __render_arrow(self, x, y, size, direction, color):
        for offset in range(size):
            graphics.DrawLine(self.canvas, x - offset, y + (offset * direction), x + offset, y + (offset * direction), color)

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
            responseArr = json.loads(url.text)
            canvas = self.matrix
            bases =  [[54,7],[49,2],[44,7]]
            outs = [[15,26],[19,26],[23,26]]
            for item in responseArr:
                running = True
                len = 1
                print('*****************************************')
                if type(item) is dict and item['league'] != type(None) and item['league'] == 'mlb':
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
                        size = 6
                        half = abs(size/2)
                        for base in bases:
                            graphics.DrawLine(canvas, base[0] + half, base[1], base[0], base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1], base[0] + size, base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1]+ size, base[0], base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1]+ size, base[0] + size, base[1]+ half, yellow)
                        for out in outs:
                            graphics.DrawLine(canvas, base[0] + half, base[1], base[0], base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1], base[0] + size, base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1]+ size, base[0], base[1]+ half, yellow)
                            graphics.DrawLine(canvas, base[0] + half, base[1]+ size, base[0] + size, base[1]+ half, yellow)
                        if item['runners']['onFirst'] == True:
                            __render_baserunner(base[0])
                        elif item['runners']['onSecond'] == True:
                            __render_baserunner(base[1])
                        elif item['runners']['onThird'] == True:
                            __render_baserunner(base[2])
                        if item['situtation']['outs'] == 1:
                            __fill_circle(outs[0])
                        elif item['situtation']['outs'] == 2:
                            __fill_circle(outs[1])
                        elif item['situtation']['outs'] == 3:
                            __fill_circle(outs[2])
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 22, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 22, homeColorSecondary, item['homeTeam']['score'])
                        count = graphics.DrawText(canvas, smallestFont, 43, 22, yellow, '3 - 1')
                        inning = graphics.DrawText(canvas, smallestFont, 0, 29, yellow, item['inning'])
                elif type(item) is dict and item['league'] != type(None) and item['league'] == 'nba':
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
                elif type(item) is dict and item['league'] != type(None) and item['league'] == 'ncaaBasketball':
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
                        finalDetail = graphics.DrawText(canvas, smallFont, 41, 22, yellow, 'F')
                    elif item['inprogress'] == True: 
                        awayTeam = graphics.DrawText(canvas, smallFont, 0, 12, awayColorSecondary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 0, 22, homeColorSecondary, item['homeTeam']['name'])
                        awayTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 12, awayColorSecondary, item['awayTeam']['score'])
                        homeTeamScore = graphics.DrawText(canvas, smallFont, 0 + 18 + 5, 22, homeColorSecondary, item['homeTeam']['score'])
                        quarter = graphics.DrawText(canvas, smallestFont, 43, 22, yellow, item['quarter'])
                        timeRemaining = graphics.DrawText(canvas, smallestFont, 43, 29, yellow, item['timeRemaining'])
                elif type(item) is dict and item['stockSymbol'] != type(None):
                    color = green if item['up'] else red
                    direction = 1 if item['up'] else -1
                    stockLogo = Image.open(requests.get(item['url'], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    canvas.SetImage(stockLogo, 0)
                    stockSymbol = graphics.DrawText(canvas, smallFont, 39, 2, color, item['stockSymbol'])
                    currentPrice = graphics.DrawText(canvas, smallestFont, 39, 25, color, item['currentPrice'])
                    __render_arrow(25, 30, 6, direction, color)
                    percentChange = graphics.DrawText(canvas, smallestFont, 39, 30, color, item['percentChange'])
                elif type(item) is dict and item['condition'] != type(None):
                    locationString = '/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/day/{}.png'.format(item['icon'])
                    weatherImage = Image.open(locationString).convert('RGB').resize((32, 32), Image.ANTIALIAS)
                    canvas.SetImage(weatherImage, 0)
                    weatherConditionText = graphics.DrawText(canvas, smallestFont, 39, 10, blue, item['condition'])
                    currentTemp = graphics.DrawText(canvas, smallFont, 39, 20, blue, item['temp'])
                    highLow = graphics.DrawText(canvas, smallestFont, 39, 30, blue, item['highLow'])
                elif type(item) is list and item[0]['condition'] != type(None):
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
                elif type(item) is dict and item['tourneyName'] != type(None):
                    for page in item['players']
                        for player in page:
                            tourneyName = graphics.DrawText(canvas, smallestFont, 10, 5, blue, item['tourneyName'])
                            tourneyStatus = graphics.DrawText(canvas, smallestFont, 10, 12, blue, item['tourneyStatus'])
                            runningTotal = 18
                            position = graphics.DrawText(canvas, smallestFont, 0, runningTotal, blue, player['position'])
                            name = graphics.DrawText(canvas, smallestFont, 10, runningTotal, blue, player['name'])
                            score = graphics.DrawText(canvas, smallestFont, 30, runningTotal, blue, player['score'])
                            thru = graphics.DrawText(canvas, smallestFont, 45, runningTotal, blue, player['thru'])
                            runningTotal = runningTotal + 8
                        time.sleep(2)
                        canvas.Clear()

                else:
                    return
                time.sleep(2)
                canvas.Clear()









                        # awayCentered = awayTeam / 2 - 5
                        # awayTeamStatus = graphics.DrawText(self.matrix, smallFont, pos + awayLogo.width + buffer + awayCentered, 26, white, awayTeamStatusString)
                        # versus = graphics.DrawText(self.matrix, font, pos + awayLogo.width + buffer + buffer + awayTeam, 24, green, versusString)
                        # self.matrix.SetImage(homeLogo, pos + awayLogo.width + buffer + buffer + awayTeam + versus)
                        # homeTeam = graphics.DrawText(self.matrix, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width, 10, white, homeTeamString)
                        # homeCentered = homeTeam / 2 - 5
                        # homeTeamStatus = graphics.DrawText(self.matrix, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeCentered, 26, white, homeTeamStatusString)
                        # odds = graphics.DrawText(self.matrix, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeTeam + buffer, 15, green, oddsString)
                        # status = graphics.DrawText(self.matrix, smallFont, pos + awayLogo.width + buffer + buffer + awayTeam + versus + buffer + homeLogo.width + homeTeam + buffer, 26, green, statusString)
                    # pos = self.matrix.width
                # self.matrix = self.matrix.SwapOnVSync(self.matrix)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()