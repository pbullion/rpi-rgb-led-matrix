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
        middleFont = graphics.Font()
        middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
        smallFont = graphics.Font()
        smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
        currentRound = int(input("Current Round: "))
        currentPick = int(input("Current Pick: "))
        currentPickIndex = int(input("Current Pick Index: "))
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
        seconds = 10
        randomSayings = [
            "HURRY THE FUCK UP!",
            "YOU'RE A CHICKEN BITCH",
        ]
        while True:
            if currentRound % 2 == 0:
                if currentPickIndex > 1:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex - 1]
                    inHolesPicksName = leagueMembers[currentPickIndex - 2]
                if currentPickIndex == 1:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex - 1]
                    inHolesPicksName = leagueMembers[currentPickIndex - 1]
                if currentPickIndex == 0:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex]
                    inHolesPicksName = leagueMembers[currentPickIndex - 1]
            if currentRound % 2 != 0:
                if currentPickIndex < 10:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex + 1]
                    inHolesPicksName = leagueMembers[currentPickIndex + 2]
                if currentPickIndex == 10:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex + 1]
                    inHolesPicksName = leagueMembers[currentPickIndex + 1]
                if currentPickIndex == 11:
                    currentPicksName = leagueMembers[currentPickIndex]
                    nextUpPicksName = leagueMembers[currentPickIndex]
                    inHolesPicksName = leagueMembers[currentPickIndex - 1]
            offscreen_canvas.Clear()
            round_text = "Rd " + str(currentRound) + "." + str(currentPick)
            time.sleep(1)
            seconds -= 1
            timeColor = green
            if seconds < 60:
                timeColor = yellow
            if seconds < 20:
                timeColor = red
            if seconds == 60 or seconds == 59:
                blackHurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    -1000,
                    26,
                    green,
                    nextUpPicksName + " GET YOUR FINGER OUT YO ASS",
                )
                hurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    ((offscreen_canvas.width / 2) - (blackHurryUpText / 2)),
                    26,
                    green,
                    nextUpPicksName + " GET YOUR FINGER OUT YO ASS",
                )
            elif seconds == 58 or seconds == 57:
                blackHurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    font,
                    -1000,
                    26,
                    green,
                    "YOU'RE UP NEXT!",
                )
                hurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    font,
                    ((offscreen_canvas.width / 2) - (blackHurryUpText / 2)),
                    26,
                    green,
                    "YOU'RE UP NEXT!",
                )
            elif seconds == 20 or seconds == 19:
                blackHurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    -1000,
                    18,
                    red,
                    "HURRY THE FUCK UP " + currentPicksName + "!",
                )
                hurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    ((offscreen_canvas.width / 2) - (blackHurryUpText / 2)),
                    18,
                    red,
                    "HURRY THE FUCK UP " + currentPicksName + "!",
                )
            elif seconds == 0:
                blackHurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    -1000,
                    18,
                    red,
                    "TAKE A SHOT " + currentPicksName + "!",
                )
                hurryUpText = graphics.DrawText(
                    offscreen_canvas,
                    middleFont,
                    ((offscreen_canvas.width / 2) - (blackHurryUpText / 2)),
                    18,
                    red,
                    "TAKE A SHOT " + currentPicksName + "!",
                )
            else:
                roundStr = graphics.DrawText(
                    offscreen_canvas, font, 1, 26, blue, round_text
                )
                nameStr = graphics.DrawText(
                    offscreen_canvas,
                    font,
                    roundStr + 10,
                    26,
                    green,
                    currentPicksName,
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
                    offscreen_canvas.width - 65,
                    14,
                    yellow,
                    str(currentRound)
                    + "."
                    + str(currentPick + 1)
                    + " "
                    + nextUpPicksName,
                )
                inHole = graphics.DrawText(
                    offscreen_canvas,
                    smallFont,
                    offscreen_canvas.width - 65,
                    28,
                    yellow,
                    str(currentRound)
                    + "."
                    + str(currentPick + 2)
                    + " "
                    + inHolesPicksName,
                )
            if seconds == -1:
                input("Press Enter to continue...")
                seconds = 10
                currentRound += 1
                currentPick += 1
                if currentRound % 2 == 0:
                    currentPickIndex = 11
                if currentRound % 2 != 0:
                    currentPickIndex = 0
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
