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
            colors = [blue, teal, purple, yellow]
            randomNum = random.randint(0,3)
            # END COLORS
            font = graphics.Font()
            font.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/6x13.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/new/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            # IMAGES FOR WEATHER
            partlyCloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            thunderstormImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            cloudyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-clouds-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            rainImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            stormyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            sunnyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-summer-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            windyImage = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/weather/icons8-wind-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            # END IMAGES FOR WEATHER
            # print(strings)
            for string in strings:
                running = True
                if 'Poll' in string:
                    color = green
                elif '#' in string:
                    color = green
                else:
                    color = green
                if isinstance(string, list) and 'http' in string[0]:
                    if '-' in string[3]:
                        color = red
                    elif '+' in string[3]:
                        color = green
                    stockLogo = Image.open(requests.get(string[0], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    stockDown = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/stocks/icons8-down-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                    stockUp = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/stocks/icons8-up-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                length = 1
                while running:
                    offscreen_canvas.Clear()
                    if 'RAIN' in string:
                        color = blue
                        img_width, img_height = rainImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(rainImage, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + rainImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif 'CLOUDY' in string or 'OVERCAST' in string:
                        color = blue
                        img_width, img_height = partlyCloudyImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(partlyCloudyImage, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + partlyCloudyImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif 'THUNDER' in string:
                        color = purple
                        img_width, img_height = thunderstormImage.size
                        pos -= 1
                        if (pos + thunderstormImage.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(thunderstormImage, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + thunderstormImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif 'SUN' in string:
                        color = yellow
                        img_width, img_height = sunnyImage.size
                        pos -= 1
                        if (pos + sunnyImage.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(sunnyImage, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + sunnyImage.width, 24, color, string)
                        time.sleep(0.008)
                    elif isinstance(string, list) and 'game' in string[0]:
                        string.pop(0)
                        gamesRunning = True
                        games = string
                        runningCount = 0
                        var_holder = {}
                        for i in range(len(games)):
                            var_holder['awayLogo' + str(i)] = Image.open(requests.get(games[i][1], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                            var_holder['homeLogo' + str(i)] = Image.open(requests.get(games[i][6], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                            var_holder['awayTeamString' + str(i)] = games[i][5]
                            var_holder['homeTeamString' + str(i)] = games[i][10]
                            var_holder['awayTeamStatusString' + str(i)] = games[i][12]
                            var_holder['homeTeamStatusString' + str(i)] = games[i][13]
                            var_holder['statusString' + str(i)] = games[i][11]
                            var_holder['oddsString' + str(i)] = games[i][14]
                            var_holder['versusString' + str(i)] = ' at '
                            var_holder['awayTeam' + str(i)] = graphics.DrawText(offscreen_canvas, smallFont, pos + runningCount + awayLogo.width + buffer, 10, awayColor, awayTeamString)
                            var_holder['awayCentered' + str(i)] = awayTeam / 3
                            var_holder['awayTeamStatus' + str(i)] = graphics.DrawText(offscreen_canvas, font, pos + runningCount + awayLogo.width + buffer + awayCentered, 31, awayColor, awayTeamStatusString)
                            var_holder['quarter' + str(i)] = graphics.DrawText(offscreen_canvas, middleFont, pos + runningCount + awayLogo.width + buffer + buffer + awayTeam + 4, 12, green, oddsString)
                            var_holder['status' + str(i)] = graphics.DrawText(offscreen_canvas, middleFont, pos + runningCount + awayLogo.width + buffer + buffer + awayTeam, 26, green, statusString)
                            var_holder['homeTeam' + str(i)] = graphics.DrawText(offscreen_canvas, smallFont, pos + runningCount + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + buffer + buffer + buffer + homeLogo.width, 10, homeColor, homeTeamString)
                            var_holder['homeCentered' + str(i)] = homeTeam / 2
                            var_holder['homeTeamStatus' + str(i)] = graphics.DrawText(offscreen_canvas, font, pos + runningCount + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + homeLogo.width + homeCentered, 31, homeColor, homeTeamStatusString)
                        print(var_holder)
                        while gamesRunning:
                            buffer = 6
                            pos -= 1
                            for game in string:
                                offscreen_canvas.SetImage(Image.open(requests.get(game[1], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS), pos)
                                offscreen_canvas.SetImage(homeLogo, pos + runningCount + awayLogo.width + buffer + buffer + awayTeam + quarter + buffer + buffer + buffer)
                                runningCount = runningCount + pos + awayLogo.width + buffer + buffer + awayTeam + status + buffer + homeLogo.width + homeTeam + buffer + quarter 
                            if (pos < 0):
                                gamesRunning = False
                                running = False
                                pos = offscreen_canvas.width
                            time.sleep(0.1)
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
                        basketballLogo = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + basketballLogo.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(basketballLogo, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + basketballLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'ESPN' in string:
                        color = blue
                        espnLogo = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + espnLogo.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(espnLogo, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + espnLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'FOXNEWS' in string:
                        color = blue
                        foxNewsLogo = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/logos/foxnews.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + foxNewsLogo.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(foxNewsLogo, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + foxNewsLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    elif 'CNN' in string:
                        color = blue
                        cnnLogo = Image.open('/home/pi/new/rpi-rgb-led-matrix/bindings/python/samples/images/logos/cnn.png').convert('RGB').resize((69,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + cnnLogo.width + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(cnnLogo, pos)
                        length = graphics.DrawText(offscreen_canvas, font, pos + cnnLogo.width + 4, 24, color, string)
                        time.sleep(0.008)
                    else:
                        length = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
                        pos -= 1
                        if (pos + length < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.008)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()