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
            colors = [blue, teal, purple, yellow]
            randomNum = random.randint(0,3)
            # END COLORS
            # FONTS
            font = graphics.Font()
            font.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            # END FONTS
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/tiny-led/all-data/pbullion@gmail.com")
            responseArr = json.loads(url.text)
            canvas = self.matrix

            for item in responseArr:
                running = True
                len = 1
                print('*****************************************')
                if type(item) is dict and item['league'] == 'mlb':
                    print('+++++++++++++')
                    print(item)
                    awayColorPrimary = graphics.Color(item['awayTeam']['colors']['main'][0],item['awayTeam']['colors']['main'][1],item['awayTeam']['colors']['main'][2])
                    awayColorSecondary = graphics.Color(item['awayTeam']['colors']['secondary'][0],item['awayTeam']['colors']['secondary'][1],item['awayTeam']['colors']['secondary'][2])
                    homeColorPrimary = graphics.Color(item['homeTeam']['colors']['main'][0],item['homeTeam']['colors']['main'][1],item['homeTeam']['colors']['main'][2])
                    homeColorSecondary = graphics.Color(item['homeTeam']['colors']['secondary'][0],item['homeTeam']['colors']['secondary'][1],item['homeTeam']['colors']['secondary'][2])
                    if item['pregame'] == False:              
                        awayTeam = graphics.DrawText(canvas, smallFont, 1, 12, awayColorPrimary, item['awayTeam']['name'])
                        homeTeam = graphics.DrawText(canvas, smallFont, 1, 24, homeColorPrimary, item['homeTeam']['name'])
                        print('######################')
                        print(awayTeam)
                        print(homeTeam)
                time.sleep(6)
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