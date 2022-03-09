#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
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
        self.parser.add_argument("-i", "--image", help="The image to display", default="./tesla.png")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

        while True:
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            colors = [blue, teal, purple, yellow]
            randomNum = random.randint(0,3)
            font = graphics.Font()
            font.LoadFont("../../../fonts/texgyre-27.bdf")
            print('++++++++++++++++++++++++++++')
            url = requests.get("https://sheline-art-website-api.herokuapp.com/patrick/all-data/pbullion@gmail.com")
            strings = json.loads(url.text)
            print(strings)
            strings.append('imageeee')
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            img_width, img_height = self.image.size
            for string in strings:
                running = True
                if 'Poll' in string:
                    color = green
                elif 'BAYLOR' in string:
                    color = green
                elif 'CURRENT WEATHER' in string:
                    color = colors[randomNum]
                elif '#' in string in string:
                    color = green
                elif '-' in string in string:
                    color = red
                elif '+' in string in string:
                    color = green
                else:
                    color = blue
                len = 1
                while running:
                    offscreen_canvas.Clear()
                    if 'imageeee' in string:
                        pos -= 1
                        if (pos + img_width < 0):
                            running = False
                            pos = offscreen_canvas.width
                        offscreen_canvas.SetImage(self.image, pos)
                        offscreen_canvas.SetImage(self.image, pos + img_width)
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