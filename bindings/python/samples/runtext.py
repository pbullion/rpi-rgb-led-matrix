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
            strings.insert(0,'imageeee')
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            # IMAGES FOR WEATHER
            print('********************')
            print('matrix width', self.matrix.width)
            print('matrix height', self.matrix.height)
            partlyCloudyImage = Image.open('./images/weather/icons8-partly-cloudy-day-48.png').convert('RGB')
            thunderstormImage = Image.open('./images/weather/icons8-cloud-lightning-48.png').convert('RGB')
            cloudyImage = Image.open('./images/weather/icons8-clouds-48.png').convert('RGB')
            rainImage = Image.open('./images/weather/icons8-heavy-rain-48.png').convert('RGB')
            stormyImage = Image.open('./images/weather/icons8-stormy-weather-48.png').convert('RGB')
            sunnyImage = Image.open('./images/weather/icons8-summer-48.png').convert('RGB')
            windyImage = Image.open('./images/weather/icons8-wind-48.png').convert('RGB')
            partlyCloudyImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            thunderstormImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            cloudyImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            rainImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            windyImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            stormyImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            sunnyImage.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            print('********************')
            # END IMAGES FOR WEATHER
            for string in strings:
                # set image here
                currentImage = cloudyImage
                img_width, img_height = currentImage.size
                print('|||||||||||||||||||||')
                print('new image width', img_width)
                print('new image height', img_height)
                print('|||||||||||||||||||||')
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
                    if 'imageeee' in string:
                        pos -= 1
                        if (pos + img_width < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(currentImage, pos)
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