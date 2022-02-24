#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import asyncio

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    async def run(self):
        print('++++++++++++++++++++++++++++')
        url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/espn")
        text = url.text
        # print(text)
        print
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/texgyre-27.bdf")
        green = graphics.Color(0, 255, 0)
        red = graphics.Color(255, 0, 0)
        pos = offscreen_canvas.width
        # my_text = text
        strings = ['Helllllllllllllllllllllo mutha fucka','tits fart turd and twat']

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 24, red, strings[0])
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
            time.sleep(0.02)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            await asyncio.sleep(5)
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 24, green, strings[1])
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
            time.sleep(0.02)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = asyncio.RunText()
    if (not run_text.process()):
        run_text.print_help()
