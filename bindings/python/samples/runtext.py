#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        while True:
            print('++++++++++++++++++++++++++++')
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/espn")
            strings = json.loads(url.text)
            print(strings)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("../../../fonts/texgyre-27.bdf")
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
            pos = offscreen_canvas.width
            for string in strings:
                running = True
                if 'CURRENT WEATHER' in string:
                    color = teal
                elif 'MARKETWATCH' in string:
                    color = teal
                elif 'ESPNNBA' in string:
                    color = teal
                elif 'ESPNNFL' in string:
                    color = teal
                elif 'ESPNMLB' in string:
                    color = teal
                elif 'ESPNTOPSTORIES' in string:
                    color = teal
                elif 'ESPNCOLLEGEFOOTBALL' in string:
                    color = teal
                elif 'ESPNCOLLEGEBASKETBALL' in string:
                    color = teal
                elif 'ESPNBIG12' in string:
                    color = teal
                elif 'ESPNSEC' in string:
                    color = teal
                elif 'CNN' in string:
                    color = teal
                elif 'NYTIMES' in string:
                    color = teal
                elif 'FOXNEWS' in string:
                    color = teal
                elif 'USATODAY' in string:
                    color = teal
                elif 'NPR' in string:
                    color = teal
                elif 'ABCHOUSTON' in string:
                    color = teal
                elif 'INVESTINGDOTCOM' in string:
                    color = teal
                elif '-' in string in string:
                    color = red
                elif '+' in string in string:
                    color = green
                else:
                    color = blue
                while running:
                    offscreen_canvas.Clear()
                    length = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
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
