#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t",
            "--text",
            help="The text to scroll on the RGB LED panel",
            default="Hello world!",
        )

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        green = graphics.Color(0, 255, 0)
        red = graphics.Color(255, 0, 0)
        blue = graphics.Color(0, 0, 255)
        teal = graphics.Color(0, 255, 255)
        purple = graphics.Color(102, 0, 204)
        yellow = graphics.Color(255, 255, 0)
        white = graphics.Color(255, 255, 0)
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text
        smallFont = graphics.Font()
        smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
        currentRound = 1
        currentPick = 1
        leagueMembers = [
            "Bill",
            "Dug",
            "Japan",
            "Duddy",
            "Donny",
            "Oscar",
            "Denny",
            "Teddie",
            "Snake",
            "Zane",
            "Brain",
            "Caleb",
        ]
        seconds = 10
        while True:
            offscreen_canvas.Clear()
            round_text = "Rd " + str(currentRound) + " Pk " + str(currentPick)
            time.sleep(1)
            seconds -= 1
            timeColor = green
            if seconds < 60:
                timeColor = yellow
            if seconds < 20:
                timeColor = red
            roundStr = graphics.DrawText(
                offscreen_canvas, font, 1, 26, blue, round_text
            )
            nameStr = graphics.DrawText(
                offscreen_canvas,
                font,
                roundStr + 10,
                26,
                green,
                leagueMembers[currentPick - 1],
            )
            remainingTime = graphics.DrawText(
                offscreen_canvas,
                font,
                roundStr + nameStr + 25,
                26,
                timeColor,
                str(seconds),
            )
            onDeck = graphics.DrawText(
                offscreen_canvas,
                smallFont,
                offscreen_canvas.width - 60,
                14,
                yellow,
                str(currentRound)
                + "."
                + str(currentPick + 1)
                + " "
                + leagueMembers[currentPick],
            )
            inHole = graphics.DrawText(
                offscreen_canvas,
                smallFont,
                offscreen_canvas.width - 60,
                28,
                yellow,
                str(currentRound)
                + "."
                + str(currentPick + 2)
                + " "
                + leagueMembers[currentPick + 1],
            )
            if seconds == 0:
                currentPick += 1
                seconds = 10
                if currentPick > 12:
                    currentRound += 1
                    currentPick = 1
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
