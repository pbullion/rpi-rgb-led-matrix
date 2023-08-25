#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)
screen.nodelay(True)


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
        middleFont = graphics.Font()
        middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
        smallFont = graphics.Font()
        smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
        # currentRound = int(input("Current Round: "))
        # currentPick = int(input("Current Pick: "))
        # currentPickIndex = int(input("Current Pick Index: "))
        currentRound = 1
        currentPick = 1
        currentPickIndex = 0
        leagueMembers = [
            "TEDDIE",
            "CALEB",
            "BILL",
            "BRAIN",
            "DUG",
            "JAPAN",
            "DUDDY",
            "DONNY",
            "OSCAR",
            "DENNY",
            "SNAKE",
            "ZANE",
        ]
        seconds = 0
        # get the curses screen window
        curses.curs_set(0)
        screen = curses.initscr()
        # turn off input echoing
        curses.noecho()
        # respond to keys immediately (don't wait for enter)
        curses.cbreak()
        # map arrow keys to special values
        screen.keypad(True)
        try:
            while True:
                offscreen_canvas.Clear()
                timeColor = green
                char = screen.getch()
                if char != 10:
                    curses.napms(1000)
                    seconds += 1
                    nameStr = graphics.DrawText(
                        offscreen_canvas,
                        font,
                        10,
                        26,
                        green,
                        "Caleb",
                    )
                    remainingTime = graphics.DrawText(
                        offscreen_canvas,
                        font,
                        nameStr + 25,
                        26,
                        timeColor,
                        str(seconds),
                    )
                else:
                    nameStr = graphics.DrawText(
                        offscreen_canvas,
                        font,
                        10,
                        26,
                        green,
                        "Caleb",
                    )
                    remainingTime = graphics.DrawText(
                        offscreen_canvas,
                        font,
                        nameStr + 25,
                        26,
                        timeColor,
                        str(seconds),
                    )
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        finally:
            # shut down cleanly
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()
            curses.endwin()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
