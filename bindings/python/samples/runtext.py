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
            print('++++++++++++++++++++++++++++')
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            print(strings)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            # IMAGES FOR WEATHER
            stockDown = Image.open('./images/stocks/icons8-down-48.png').convert('RGB').resize((8, 8), Image.ANTIALIAS)
            stockUp = Image.open('./images/stocks/icons8-up-48.png').convert('RGB').resize((8, 8), Image.ANTIALIAS)
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
                elif 'BAYLOR' in string:
                    color = green
                elif '#' in string in string:
                    color = green
                elif '-' in string in string:
                    color = red
                elif '+' in string in string:
                    color = green
                else:
                    color = colors[randomNum]
                len = 1
                while running:
                    offscreen_canvas.Clear()
                    if 'RAIN' in string:
                        img_width, img_height = rainImage.size
                        pos -= 1
                        if (pos + img_width < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(rainImage, pos)
                        time.sleep(0.01)
                    elif 'CLOUDY' in string:
                        img_width, img_height = partlyCloudyImage.size
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(partlyCloudyImage, pos)
                        len = graphics.DrawText(offscreen_canvas, font, pos + partlyCloudyImage.width, 24, color, string)
                        time.sleep(0.01)
                    elif '-' in string:
                        img_width, img_height = stockDown.size
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(stockDown, pos,24)
                        len = graphics.DrawText(offscreen_canvas, font, pos + stockDown.width, 24, color, string)
                        time.sleep(0.01)
                    elif '+' in string:
                        img_width, img_height = stockUp.size
                        pos -= 1
                        if (pos + len < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(stockUp, pos, 24)
                        len = graphics.DrawText(offscreen_canvas, font, pos + stockUp.width, 24, color, string)
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


        # if includes 'rain' do the rain image
        # sunny
        # partly cloudy
        # includes 'thunder' do lightning image
        #
        #
        #
        #