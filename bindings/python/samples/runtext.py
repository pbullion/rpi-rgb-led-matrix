#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    async def run(self):
        print('++++++++++++++++++++++++++++')
        url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/espn")
        text = url.text
        print(text)
        print
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/texgyre-27.bdf")
        green = graphics.Color(0, 255, 0)
        red = graphics.Color(255, 0, 0)
        pos = offscreen_canvas.width
        # my_text = text
        strings = ['Helllllllllllllllllllllo mutha fucka','tits fart turd and twat']

        async def scrollingText(self,color):
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 24, color, string)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width
            time.sleep(0.02)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            return

        while True:
            await for string in strings:
                await scrollingText(green)
                await scrollingText(red)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
