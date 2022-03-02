#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json
import random

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        while True:
            print('++++++++++++++++++++++++++++')
            # url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            url = requests.get("localhost:3001/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            print(strings)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("../../../fonts/texgyre-27.bdf")
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            colors = [blue, teal, purple, yellow]
            pos = offscreen_canvas.width
            randomNum = random.randint(0,3)
            for string in strings:
                running = True
                if 'POLL' in string:
                    color = green
                elif 'BAYLOR' in string:
                    color = green
                elif 'CURRENT WEATHER' in string:
                    color = colors[randomNum]
                elif 'MARKETWATCH' in string:
                    color = colors[randomNum]
                elif 'ESPNNBA' in string:
                    color = colors[randomNum]
                elif 'ESPNNFL' in string:
                    color = colors[randomNum]
                elif 'ESPNMLB' in string:
                    color = colors[randomNum]
                elif 'ESPNTOPSTORIES' in string:
                    color = colors[randomNum]
                elif 'ESPNCOLLEGEFOOTBALL' in string:
                    color = colors[randomNum]
                elif 'ESPNCOLLEGEBASKETBALL' in string:
                    color = colors[randomNum]
                elif 'ESPNBIG12' in string:
                    color = colors[randomNum]
                elif 'ESPNSEC' in string:
                    color = colors[randomNum]
                elif 'CNN' in string:
                    color = colors[randomNum]
                elif 'NYTIMES' in string:
                    color = colors[randomNum]
                elif 'FOXNEWS' in string:
                    color = colors[randomNum]
                elif 'USATODAY' in string:
                    color = colors[randomNum]
                elif 'NPR' in string:
                    color = colors[randomNum]
                elif 'ABCHOUSTON' in string:
                    color = colors[randomNum]
                elif 'INVESTINGDOTCOM' in string:
                    color = colors[randomNum]
                elif '-' in string in string:
                    color = red
                elif '+' in string in string:
                    color = green
                else:
                    color = blue
                while running:
                    gameLength = len(string)
                    print(gameLength)
                    offscreen_canvas.Clear()
                    line1 = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string[0])
                    line2 = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string[1])
                    # length = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
                    pos -= 1
                    if (pos + length < 0):
                        running = False
                        pos = offscreen_canvas.width
                    time.sleep(0.01)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
