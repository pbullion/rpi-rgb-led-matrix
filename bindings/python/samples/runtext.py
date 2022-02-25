#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json
from threading import Timer
import asyncio

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    async def run(self):
        print('++++++++++++++++++++++++++++')
        scrolling = False
        strings = []
        async def getData():
            print('getting data')
            url = await requests.get("https://sheline-art-website-api.herokuapp.com/patrick/espn")
            strings = await json.loads(url.text)
            scrolling = True
        print
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/texgyre-27.bdf")
        green = graphics.Color(0, 255, 0)
        red = graphics.Color(255, 0, 0)
        blue = graphics.Color(0, 0, 255)
        teal = graphics.Color(0, 255, 255)
        pos = offscreen_canvas.width
        print(scrolling)
        print(strings)

        while scrolling:
            for string in strings:
                running = True
                if 'CURRENT WEATHER' in string:
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
                        if (string == strings[stringLen]):
                            scrolling = False
                        running = False
                        pos = offscreen_canvas.width
                    time.sleep(0.02)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        
        while not scrolling:
            getData()




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
