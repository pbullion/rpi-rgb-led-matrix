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
            font.LoadFont("../../../fonts/texgyre-27.bdf")
            # print('++++++++++++++++++++++++++++')
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            # print(strings)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            # IMAGES FOR WEATHER
            partlyCloudyImage = Image.open('./images/weather/icons8-partly-cloudy-day-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            thunderstormImage = Image.open('./images/weather/icons8-cloud-lightning-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            cloudyImage = Image.open('./images/weather/icons8-clouds-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            rainImage = Image.open('./images/weather/icons8-heavy-rain-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            stormyImage = Image.open('./images/weather/icons8-stormy-weather-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            sunnyImage = Image.open('./images/weather/icons8-summer-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            windyImage = Image.open('./images/weather/icons8-wind-48.png').convert('RGB').resize((32, 32), Image.ANTIALIAS)
            # END IMAGES FOR WEATHER
            for string in strings:
                running = True
                if 'Poll' in string:
                    color = green
                elif '#' in string:
                    color = green
                else:
                    color = colors[randomNum]
                if isinstance(string, list) and 'game' in string[0]:
                    print(string)
                    awayLogo = Image.open(requests.get(string[1], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    homeLogo = Image.open(requests.get(string[6], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                if isinstance(string, list) and 'http' in string[0]:
                    if '-' in string[3]:
                        color = red
                    elif '+' in string[3]:
                        color = green
                    stockLogo = Image.open(requests.get(string[0], stream=True).raw).convert('RGB').resize((32,32), Image.ANTIALIAS)
                    stockDown = Image.open('./images/stocks/icons8-down-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                    stockUp = Image.open('./images/stocks/icons8-up-48.png').convert('RGB').resize((16,16), Image.ANTIALIAS)
                len = 1
                while running:
                    print('runnnnnnnnnning')
                    offscreen_canvas.Clear()
                    if 'RAIN' in string:
                        color = blue
                        img_width, img_height = rainImage.size
                        pos -= 1
                        if (pos + img_width < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(rainImage, pos)
                        time.sleep(0.01)
                    elif 'CLOUDY' in string or 'OVERCAST' in string:
                        color = blue
                        img_width, img_height = partlyCloudyImage.size
                        pos -= 1
                        if (pos + partlyCloudyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(partlyCloudyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + partlyCloudyImage.width, 24, color, string)
                        time.sleep(0.01)
                    elif 'THUNDER' in string:
                        color = purple
                        img_width, img_height = thunderstormImage.size
                        pos -= 1
                        if (pos + thunderstormImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(thunderstormImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + thunderstormImage.width, 24, color, string)
                        time.sleep(0.01)
                    elif 'SUN' in string:
                        color = yellow
                        img_width, img_height = sunnyImage.size
                        pos -= 1
                        if (pos + sunnyImage.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(sunnyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + sunnyImage.width, 24, color, string)
                        time.sleep(0.01)
                    elif isinstance(string, list) and 'game' in string[0]:
                        print('+++++++++++++++++++++++')
                        print(string)
                        awayColor = graphics.Color(string[2], string[3], string[4])
                        homeColor = graphics.Color(string[7], string[8], string[9])
                        awayTeamString = string[5]
                        homeTeamString = string[10]
                        statusString = string[11]
                        pos -= 1
                        # away team logo
                        offscreen_canvas.SetImage(awayLogo, pos)
                        # away team string
                        awayTeam = graphics.DrawText(offscreen_canvas, font, 15 + pos + 35, 24, awayColor, awayTeamString)
                        # home team logo
                        offscreen_canvas.SetImage(homeLogo, 25 + pos + 35 + awayTeam)
                        # home team string
                        homeTeam = graphics.DrawText(offscreen_canvas, font, 15 + pos + 35 + awayTeam + 35, 24, homeColor, homeTeamString)
                        # game time
                        status = graphics.DrawText(offscreen_canvas, font, 25 + pos + 35 + awayTeam + 35 + homeTeam, 24, blue, statusString)
                        if (60 + pos + 35 + awayTeam + 35 + homeTeam + status < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.01)
                    elif isinstance(string, list):
                        if '-' in string[3]:
                            pos -= 1
                            offscreen_canvas.SetImage(stockLogo, pos)
                            first = graphics.DrawText(offscreen_canvas, font, pos + 35, 24, color, string[1])
                            second = graphics.DrawText(offscreen_canvas, font, pos + first + 35, color, string[2])
                            offscreen_canvas.SetImage(stockDown,  pos + first + 35 + second, 8)
                            third = graphics.DrawText(offscreen_canvas, font,  pos + first + 35 + third, 24, color, string[3])
                            if (pos + 35 + 15 + 20 + 17 + len < 0):
                                running = False
                                pos = offscreen_canvas.width
                            time.sleep(0.01)
                        elif '+' in string[3]:
                            pos -= 1
                            offscreen_canvas.SetImage(stockLogo, pos)
                            first = graphics.DrawText(offscreen_canvas, font, pos + 35, 24, color, string[1])
                            second = graphics.DrawText(offscreen_canvas, font, pos + 35 + first, 24, color, string[2])
                            offscreen_canvas.SetImage(stockUp, pos + 35 + 15 + 20 + first + second, 8)
                            third = graphics.DrawText(offscreen_canvas, font,  pos + first + 35 + second + third, 24, color, string[3])
                            if (pos + 35 + 15 + 20 + 17 + len < 0):
                                running = False
                                pos = offscreen_canvas.width
                            time.sleep(0.01)
                    elif 'AP Poll' in string:
                        color = green
                        basketballLogo = Image.open('./images/logos/basketball.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + basketballLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(basketballLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + basketballLogo.width + 4, 24, color, string)
                        time.sleep(0.01)
                    elif 'ESPN' in string:
                        color = green
                        espnLogo = Image.open('./images/logos/espn.png').convert('RGB').resize((130,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + espnLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(espnLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + espnLogo.width + 4, 24, color, string)
                        time.sleep(0.01)
                    elif 'FOXNEWS' in string:
                        color = blue
                        foxNewsLogo = Image.open('./images/logos/foxnews.png').convert('RGB').resize((32,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + foxNewsLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(foxNewsLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + foxNewsLogo.width + 4, 24, color, string)
                        time.sleep(0.01)
                    elif 'CNN' in string:
                        color = blue
                        cnnLogo = Image.open('./images/logos/cnn.png').convert('RGB').resize((69,32), Image.ANTIALIAS)
                        pos -= 1
                        if (pos + cnnLogo.width + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(cnnLogo, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + cnnLogo.width + 4, 24, color, string)
                        time.sleep(0.01)
                    else:
                        len = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.01)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()