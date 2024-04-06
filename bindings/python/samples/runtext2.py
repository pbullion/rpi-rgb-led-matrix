#!/usr/bin/env python
# Display a runtext with double-buffering.
from ast import If
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json
from PIL import Image
import re

userFile = open("/home/pi/rpi-rgb-led-matrix/user.json")


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(self)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t",
            "--text",
            help="The text to scroll on the RGB LED panel",
            default="Hello world!",
        )

    def run(self):
        userJSON = json.load(userFile)
        houstonOpenLogo2 = (
            Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/houstonopen2.png",
            )
            .convert("RGB")
            .resize((35, 35), Image.ANTIALIAS)
        )
        mmaLogos = {
            "UFC Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ufclogo.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "0000000000": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/defaultperson2.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4916974": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4916974 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5127984": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5127984 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5032015": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5032015 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5144068": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5144068 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4815973": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4815973 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5149439": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5149439 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4085155": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4085155 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4816066": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4816066 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3154389": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3154389 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4293183": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4293183 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2552777": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2552777 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4418784": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4418784 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2504639": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2504639 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3088232": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3088232 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4786358": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4786358 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5048900": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5048900 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4710386": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4710386 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            # "5147389": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5147389 Background Removed.png"
            # )
            # .convert("RGB")
            # .resize((45, 45), Image.ANTIALIAS),
            "3089069": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3089069 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4038116": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4038116 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4040926": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4040926 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4324622": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4324622 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3099187": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3099187 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4018757": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4018757 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2984770": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2984770 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4025699": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4025699 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5077789": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5077789 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4687434": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4687434 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4697476": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4697476 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4420893": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4420893 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5060398": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5060398 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4684240": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4684240 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4875513": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4875513 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4686735": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4686735 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5044438": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5044438 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3089633": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3089633 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4227122": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4227122 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4289516": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4289516 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4700617": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4700617 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3821549": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3821549 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3915502": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3915502 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2959422": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2959422 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4078243": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4078243 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4076472": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4076472 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4408436": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4408436 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4422103": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4422103 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5060467": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5060467 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2553993": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2553993 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4333158": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4333158 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3045887": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3045887 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4024714": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4024714 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4350796": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4350796 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4608674": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4608674 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2312150": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2312150 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5060505": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5060505 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5145496": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5145496 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5157669": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5157669 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            # "4894780": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4894780 Background Removed.png"
            # )
            # .convert("RGB")
            # .resize((45, 45), Image.ANTIALIAS),
            "5093484": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5093484 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4426305": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4426305 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5093447": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5093447 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            # "4402367": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4402367 Background Removed.png"
            # )
            # .convert("RGB")
            # .resize((45, 45), Image.ANTIALIAS),
            "4686723": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4686723 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2591306": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2591306 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4010864": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4010864 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3571515": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3571515 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3955577": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3955577 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3019246": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3019246 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4294378": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4294378 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4239738": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4239738 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5144312": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5144312 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3900088": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3900088 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4351319": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4351319 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5077399": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5077399 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5144008": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/5144008 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4354318": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4354318 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4374436": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4374436 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4566145": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4566145 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4915907": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4915907 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3032973": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3032973 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4221863": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4221863 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4816062": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4816062 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4878592": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4878592 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4565671": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4565671 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4901883": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4901883 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4616087": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4616087 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4702589": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4702589 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3955778": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3955778 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4816283": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4816283 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3896934": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3896934 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4424224": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4424224 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4319785": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4319785 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4801267": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4801267 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4339145": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4339145 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4702563": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4702563 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2553261": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2553261 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3111927": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3111927 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3104720": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3104720 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4334306": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4334306 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4875511": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4875511 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4918083": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4918083 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2500735": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2500735 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4245094": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4245094 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4815998": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4815998 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4875506": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4875506 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3093559": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3093559 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3722422": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3722422 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3028064": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3028064 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3281606": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3281606 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4294926": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4294926 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4396359": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4396359 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4276994": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4276994 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4012999": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4012999 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4418962": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4418962 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2959588": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2959588 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3994033": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3994033 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3045734": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3045734 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4237015": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4237015 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2335687": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2335687 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3068125": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3068125 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4026490": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4026490 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4246307": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4246307 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3922557": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3922557 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4873640": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4873640 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3151289": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3151289 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4293517": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4293517 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3090197": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3090197 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4828707": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4828707 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3022067": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3022067 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3943695": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3943695 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2506549": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/2506549 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4895362": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4895362 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3155424": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/3155424 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4205093": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/4205093 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
        }
        teamLogosNCAA = {
            "0000000000": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/defaultperson2.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "47": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/47 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "258": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/258 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "147": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/147 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "68": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/68 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "344": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/344 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "252": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/252 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "156": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/156 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "12": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/12 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "153": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/153 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "356": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/356 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2579": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2579 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2168": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2168 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "251": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/251 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "96": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/96 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2250": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2250 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "66": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/66 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2633": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2633 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2641": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2641 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2305": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2305 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "265": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/265 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2226": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2226 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "239": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/239 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "21": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/21 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "269": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/269 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "41": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/41 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "228": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/228 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "57": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/57 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "158": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/158 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "150": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/150 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2509": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2509 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "333": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/333 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "248": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/248 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "275": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/275 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "328": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/328 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2608": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2608 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "99": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/99.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2507": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2507 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "61": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/61 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "194": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/194 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2116": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2116 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "259": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/259 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2086": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2086 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2294": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2294.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "254": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/254 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2550": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2550 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "282": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/282 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "71": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/71 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "163": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/163 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "154": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/154 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2132": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2132.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "222": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/222 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2032": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2032 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "28": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/28 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2547": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2547 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2458": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2458 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "149": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/149 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2217": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2217 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2514": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2514 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2272": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2272 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2627": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2627 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "357": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/357 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "189": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/189 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2046": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2046 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2681": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2681 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "36": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/36 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2755": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2755 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "38": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/38 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "127": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/127 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2184": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2184 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2006": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2006 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "299": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/299 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2413": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2413 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2483": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2483 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2440": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2440 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2473": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2473 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2377": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2377 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2571": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2571 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2612": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2612 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "152": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/152 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2535": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2535 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2181": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2181 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "77": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/77 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2142": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2142 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/5 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "98": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/98 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "56": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/56 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "167": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/167 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "43": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/43 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "245": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/245 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "261": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/261 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "232": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/232 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2344": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2344 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "256": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/256 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2628": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2628 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2253": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2253 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "249": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/249 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "103": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/103 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2752": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2752 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "172": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/172 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "58": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/58 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "257": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/257 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "135": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/135 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2306": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2306 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "300": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/300.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2603": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2603 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2567": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2567 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2350": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2350 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2439": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2439 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2026": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2026 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2539": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2539 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2670": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2670 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2065": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2065 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2130": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2130 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2169": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2169 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "325": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/325 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2506": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2506 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2031": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2031 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "339": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/339 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2640": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2640 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2000": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2000 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2870": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2870 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2010": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaa/2010 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
        }
        teamLogosMLB = {
            "MLB": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "29": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/29 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "15": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/15 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "1": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/1 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "2": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/2 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "16": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/16 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/4 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "17": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/17 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "5": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/5 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "27": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/27 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "6": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/6 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "18": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/18 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "7": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/7 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "3": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/3 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "19": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/19 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "28": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/28 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "8": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/8 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "9": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/9 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "21": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/21 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "10": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/10 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "11": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/11 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "22": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/22 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "23": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/23 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "25": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/25 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "26": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/26 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "12": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/12 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "24": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/24 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "30": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/30 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "13": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/13 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "14": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/14 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "20": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlb/20 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
        }
        teamLogos = {
            # "MLB": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_ Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            "NFL": Image.open(
                requests.get(
                    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/National_Football_League_logo.svg/1200px-National_Football_League_logo.svg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            # "New York Yankees": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-new-york-yankees- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Washington Nationals": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-Washington-Nationals- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Texas Rangers": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcvkAI8sinNSRfodR342oUFAo6JXPJUW9M8vM3yC5f3g&s",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "New York Mets": Image.open(
            #     requests.get(
            #         "https://www.mlbstatic.com/team-logos/share/121.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Miami Marlins": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO_zP8e4N4bDCCuMrkp1eGA7rIc8akKKqFmg&usqp=CAU",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Oakland Athletics": Image.open(
            #     requests.get(
            #         "https://1000logos.net/wp-content/uploads/2018/05/Oakland-Athletics-Logo-Color.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Kansas City Royals": Image.open(
            #     requests.get(
            #         "https://img.mlbstatic.com/mlb-images/image/private/t_1x1/t_w1024/mlb/y4j3k0mxap2tx6ozuac6.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Toronto Blue Jays": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Milwaukee Brewers": Image.open(
            #     requests.get(
            #         "https://purepng.com/public/uploads/large/milwaukee-brewers-logo-9xg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Boston Red Sox": Image.open(
            #     requests.get(
            #         "https://www.freepnglogos.com/uploads/boston-red-sox-logo-png/boston-red-sox-circle-hd-picture-download-11.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Cleveland Guardians": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Cincinnati Reds": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cincinnati_Reds_Logo.svg/1200px-Cincinnati_Reds_Logo.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "San Francisco Giants": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/bI0AAOSwqo1gMvNf/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Colorado Rockies": Image.open(
            #     requests.get(
            #         "https://cdn.cdnlogo.com/logos/c/19/colorado-rockies.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Minnesota Twins": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW5d4zuFojuvYldGSmfFDf_L4YDpkGNNr1kP-gAUg&s",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Los Angeles Dodgers": Image.open(
            #     requests.get(
            #         "https://cdn.shopify.com/s/files/1/1949/1233/products/183165943449-0.jpg?v=1575428281",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Atlanta Braves": Image.open(
            #     requests.get(
            #         "https://images.fineartamerica.com/images/artworkimages/medium/1/atlanta-braves-logo-jeromi-cesk-transparent.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Seattle Mariners": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Seattle_Mariners_logo_%28low_res%29.svg/1200px-Seattle_Mariners_logo_%28low_res%29.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # # https://loodibee.com/wp-content/uploads/Seattle-Mariners-Logo-1977-1980-300x300.png
            # .convert("RGB").resize((45,45), Image.ANTIALIAS),
            # "Los Angeles Angels": Image.open(
            #     requests.get(
            #         "https://media-s3-us-east-1.ceros.com/mlb/images/2022/05/31/20ba2e8b96bd79f5c4c3fe0367fed23f/patch.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Detroit Tigers": Image.open(
            #     requests.get(
            #         "https://1000logos.net/wp-content/uploads/2017/08/Detroit-Tigers-Logo-1994.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Arizona Diamondbacks": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Philadelphia Phillies": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-Philadelphia-Phillies- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "San Diego Padres": Image.open(
            #     requests.get(
            #         "https://s.yimg.com/it/api/res/1.2/3.wJ5Gj6m_PwuYk8zbM0.g--~A/YXBwaWQ9eW5ld3M7dz0xMjAwO2g9NjMwO3E9MTAw/https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Pittsburgh Pirates": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Tampa Bay Rays": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/ctwAAOSwYshgyTRa/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Baltimore Orioles": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/Baltimore-Orioles-Logo-1989-1991-300x300.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Chicago White Sox": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/ducAAOSwXGxgQuJM/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "St. Louis Cardinals": Image.open(
            #     requests.get(
            #         "https://i.pinimg.com/originals/34/2c/0b/342c0baa25c6344e9cb9e3dddaec3f25.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Chicago Cubs": Image.open(
            #     requests.get(
            #         "https://i.etsystatic.com/16901505/r/il/638115/1932889911/il_fullxfull.1932889911_4max.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Houston Astros": Image.open(
            #     requests.get(
            #         "https://images.ctfassets.net/iiozhi00a8lc/t117_favicon117_qgouernt_ehw9pj78_png/700d0ebafa92b5499f3dc09bf465fc98/t117_favicon.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Arizona Cardinals": Image.open(
            #     requests.get(
            #         "https://seeklogo.com/images/A/arizona-cardinals-logo-60AFACA5B9-seeklogo.com.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Atlanta Falcons": Image.open(
            #     requests.get(
            #         "https://cdn.freebiesupply.com/images/large/2x/atlanta-falcons-logo-on-black.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Baltimore Ravens": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b09.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Buffalo Bills": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/03/Buffalo_Bills_logo_blue-700x502.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Carolina Panthers": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/02/Carolina_Panthers_logo_blue-700x380.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Chicago Bears": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b16.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Cincinnati Bengals": Image.open(
            #     requests.get(
            #         "https://cdn.freebiesupply.com/images/thumbs/1x/cincinnati-bengals- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Cleveland Browns": Image.open(
            #     requests.get(
            #         "https://i.redd.it/1rsnuls0llu71.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Jacksonville Jaguars": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b2f.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Las Vegas Raiders": Image.open(
            #     requests.get(
            #         "https://content.sportslogos.net/logos/7/6708/full/8521_las_vegas_raiders-primary-20201.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Dallas Cowboys": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/1076px-Dallas_Cowboys.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Denver Broncos": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b21.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Detroit Lions": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-detroit-lions-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Green Bay Packers": Image.open(
            #     requests.get(
            #         "https://seeklogo.com/images/G/green-bay-packers-logo-2A5FB2D033-seeklogo.com.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Houston Texans": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b29.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Indianapolis Colts": Image.open(
            #     requests.get(
            #         "https://s.yimg.com/it/api/res/1.2/1U2AxCGOmhypKITxE2PNMw--~A/YXBwaWQ9eW5ld3M7dz0xMjAwO2g9NjMwO3E9MTAw/https://s.yimg.com/cv/apiv2/default/nfl/20190724/500x500/2019_IND_wbg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Los Angeles Chargers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-los-angeles-chargers-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Los Angeles Rams": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/los-angeles-rams-2020- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Miami Dolphins": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/02/Miami_Dolphins_logo_bright-609x700.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Minnesota Vikings": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-minnesota-vikings-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            "Kansas City Chiefs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-kansas-city-chiefs-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            # "New England Patriots": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-england-patriots-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "New Orleans Saints": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-orleans-saints-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "New York Giants": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-york-giants-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "New York Jets": Image.open(
            #     requests.get(
            #         "https://www.liblogo.com/img-logo/max/ne809n810-new-york-jets-logo-new-york-jets-logos-history-amp-images-logos-lists-brands.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Philadelphia Eagles": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-philadelphia-eagles-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Pittsburgh Steelers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-pittsburgh-steelers-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            "San Francisco 49ers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            # "Seattle Seahawks": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-seattle-seahawks-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Tampa Bay Buccaneers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/tampa-bay-buccaneers-2020- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Tennessee Titans": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-tennessee-titans-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            # "Washington Commanders": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/washington-commanders- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((45,45), Image.ANTIALIAS),
            "Atlanta Hawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hawks.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Boston Celtics": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/celtics.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Brooklyn Nets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nets.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Charlotte Hornets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hornets.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Chicago Bulls": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bulls.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Cleveland Cavaliers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/cavs.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Dallas Mavericks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mavs.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Denver Nuggets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nuggets.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Detroit Pistons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pistons.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Golden State Warriors": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/warriors.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Houston Rockets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/rockets.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Indiana Pacers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pacers.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Los Angeles Clippers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/clippers.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Los Angeles Lakers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lakers.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Memphis Grizzlies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/grizzlies.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Miami Heat": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/heat.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Milwaukee Bucks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bucks.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Minnesota Timberwolves": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/twolves.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "New Orleans Pelicans": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pelicans.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "New York Knicks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/knicks.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Oklahoma City Thunder": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/thunder.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Orlando Magic": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/magic.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Philadelphia 76ers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/76ers.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Phoenix Suns": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/suns.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Portland Trail Blazers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blazers.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Sacramento Kings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kings.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "San Antonio Spurs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/spurs.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Toronto Raptors": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/raptors.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Utah Jazz": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/jazz.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Washington Wizards": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wizards.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Ducks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ducks Background Removed.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Coyotes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coyotes Background Removed.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Blue Jackets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bluejackets Background Removed.png",
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Anaheim Ducks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ducks Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Arizona Coyotes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coyotes Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Boston Bruins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bruins Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Buffalo Sabres": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sabres Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Calgary Flames": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/flames Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Carolina Hurricanes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hurricanes Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Chicago Blackhawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blackhawks Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Colorado Avalanche": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/avalanche Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Columbus Blue Jackets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bluejackets Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Dallas Stars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/stars Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Detroit Red Wings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/redwings Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Edmonton Oilers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oilers Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Florida Panthers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/panthers Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Los Angeles Kings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lakings Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Minnesota Wild": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wild Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Montreal Canadiens": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/canadiens Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Nashville Predators": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/predators Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "New Jersey Devils": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/devils Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "New York Islanders": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/islanders Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "New York Rangers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nyrangers Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Ottawa Senators": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/senators Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Philadelphia Flyers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/flyers Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Pittsburgh Penguins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/penguins Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "San Jose Sharks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sharks Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Seattle Kraken": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kraken Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "St. Louis Blues": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blues Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Tampa Bay Lightning": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lightning Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Toronto Maple Leafs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mapleleafs Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Vancouver Canucks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/canucks Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Vegas Golden Knights": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/goldenknights Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Washington Capitals": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/capitals Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Winnipeg Jets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/winnipegjets Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "AFC Bournemouth": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/afcbournemouth Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Arsenal": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/arsenal Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Aston Villa": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/astonvilla Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Brentford": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/brentford Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Brighton & Hove Albion": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/brightonhovealbion Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Burnley": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/burnley Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Chelsea": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/chelsea Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Crystal Palace": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/crystalpalace Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Everton": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/everton Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Fulham": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/fulham Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Luton Town": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lutontown Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Leicester City": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/leicestercity Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Liverpool": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/liverpool Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Manchester City": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/manchestercity Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Manchester United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/manchesterunited Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Newcastle United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/newcastleunited Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Nottingham Forest": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nottinghamforest Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Sheffield United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sheffieldunited Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Tottenham Hotspur": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tottenhamhotspur Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Watford": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/watford Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "West Ham United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/westhamunited Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "Wolverhampton Wanderers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wolverhamptonwanderers Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "NCAA Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaalogo Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "English Premier League Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/englishpremierleague Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "MLS Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlslogo.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            # "Muhammad Naimov": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/muhammadnaimov.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Erik Silva": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/eriksilva.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Victor Altamirano": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/victoraltamirano.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Felipe dos Santos": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/felipedossantos.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Ronaldo Rodriguez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/luisrodriguez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Luis Rodriguez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/luisrodriguez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Denys Bondar": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/denysbondar.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Claudio Puelles": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/claudiopuelles.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Farés Ziam": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/faresziam.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Daniel Lacerda": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/daniellacerda.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Édgar Cháirez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/edgarchairez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Jesus Aguilar": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jesusaguilar.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Mateus Mendonca": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/mateusmendonca.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Raoni Barcelos": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/raonibarcelos.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Cristian Quiñonez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/cristianquinonez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Chris Duncan": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/chrisduncan.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Manuel Torres": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/manueltorres.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Sam Hughes": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/samhughes.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Yazmin Jauregui": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yazminjauregui.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Ricky Turcios": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/rickyturcios.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Raul Rosas Jr.": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/raulrosasjr.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Daniel Zellhuber": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/danielzellhuber.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Francisco Prado": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/franciscoprado.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Brian Ortega": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brianortega.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Yair Rodriguez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yairrodriguez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Brandon Moreno": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brandonmoreno.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Brandon Royval": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brandonroyval.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Loik Radzhabov": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/loikradzhabov.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Vinicius Oliveira": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/viniciusoliveira.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Yanis Ghemmouri": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yanisghemmouri.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Christian Leroy Duncan": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/christianleroyduncan.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Claudio Ribeiro": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/claudioribeiro.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Aiemann Zahabi": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/aiemannzahabi.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Javid Basharat": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/javidbasharat.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Ludovit Klein": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/ludovitklein.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Joel Alvarez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/joelalvarez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Eryk Anders": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/erykanders.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Jamie Pickett": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jamiepickett.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Matt Schnell": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/mattschnell.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Steve Erceg": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/steveerceg.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Umar Nurmagomedov": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/umarnurmagomedov.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Alex Perez": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/alexperez.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Muhammad Mokaev": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/muhammadmokaev.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Tyson Pedro": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/tysonpedro.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Abdul-Kareem Al-Selwady": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/tysonpedro.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Vitor Petrino": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/vitorpetrino.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Jairzinho Rozenstruik": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jairzinhorozenstruik.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            # "Shamil Gaziev": Image.open(
            #     "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/shamilgaziev.png"
            # )
            # .convert("RGB")
            # .resize((55, 40), Image.ANTIALIAS),
            "0000000000": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/defaultperson2.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            # PGA PLAYERS
            "Mexico Open": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/mexicoopen.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "golfball": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/golf_ball.png"
            )
            .convert("RGB")
            .resize((20, 20), Image.ANTIALIAS),
            "78": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/78 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "446": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/446 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "601": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/601 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3538": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3538 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3793": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3793 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9517": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9517 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9804": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9804 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10577": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10577 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4408320": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4408320 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4845307": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4845307 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5136186": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5136186 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10048": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10048 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10054": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10054 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10057": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10057 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10058": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10058 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10134": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10134 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10140": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10140 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10166": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10166 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10364": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10364 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10372": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10372 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10505": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10505 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10522": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10522 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10548": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10548 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10583": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10583 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1059": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1059 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10592": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10592 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10596": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10596 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10664": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10664 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1077": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1077 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10863": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10863 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10906 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10980": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10980 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10990": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10990 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11119": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11119 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11143": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11143 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11250": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11250 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11332": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11332 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11333": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11333 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11376": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11376 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11378": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11378 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11382": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11382 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11393": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11393 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11456": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11456 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1225": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1225 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1264": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1264 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1483": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1483 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "16": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/16 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1600": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1600 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1614": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1614 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1651": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1651 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1680": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1680 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "205": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/205 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "2230": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/2230 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "2283": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/2283 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "257": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/257 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "2571": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/2571 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3257": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3257 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3378": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3378 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3449": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3449 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3454": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3454 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3470": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3470 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3550": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3550 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3702": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3702 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3792": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3792 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3832": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3832 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "388": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/388 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3970": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3970 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "412": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/412 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4251": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4251 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4349547": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4349547 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4355673": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4355673 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4364752": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4364752 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4364873": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4364873 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4372851": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4372851 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4375972": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4375972 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4404991": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4404991 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4404992": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4404992 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4408316": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4408316 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4410932": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4410932 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4419142": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4419142 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4423323": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4423323 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4425898": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4425898 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4425906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4425906 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4426181": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4426181 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4513": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4513 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4566443": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4566443 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4587": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4587 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4589438": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4589438 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4602218": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4602218 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4602673": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4602673 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4633": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4633 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4638": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4638 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4698579": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4698579 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4832046": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4832046 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4837": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4837 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4848": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4848 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5285": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5285 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5408": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5408 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5409": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5409 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5462": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5462 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5467": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5467 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5502": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5502 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5539": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5539 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5548": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5548 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "569": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/569 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5692": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5692 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5704": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5704 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5724": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5724 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5860": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5860 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5882": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5882 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5902": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5902 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6001": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6001 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6007": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6007 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6011": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6011 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6017": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6017 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6086": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6086 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6196": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6196 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6701": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6701 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "676": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/676 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6825": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6825 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6931": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6931 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6937": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6937 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6954": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6954 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "7001": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7001 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "7081": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7081 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "7083": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7083 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "769": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/769 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "809": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/809 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8906 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8910": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8910 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8961": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8961 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8973": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8973 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8974": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8974 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9037": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9037 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9040": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9040 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9126": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9126 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9127": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9127 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10047": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10047 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11481": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11481 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3948": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3948 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4351896": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4351896 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4449": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4449 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4791221": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4791221 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4904296": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4904296 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5113335": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5113335 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6015": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6015 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9143": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9143 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9144": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9144 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9243": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9243 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9364": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9364 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9478": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9478 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9484": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9484 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9530": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9530 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9531": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9531 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9569": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9569 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9658": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9658 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9843": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9843 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9877": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9877 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9938": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9938 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9951": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9951 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10057": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10057 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10058": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10058 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10134": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10134 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10166": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10166 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10177": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10177 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1030": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1030 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1037": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1037 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10481": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10481 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10562": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10562 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1067": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1067 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10831": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10831 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10929": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10929 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11098": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11098 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11101": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11101 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11183": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11183 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11340": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11340 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11342": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11342 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11362": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11362 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11385": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11385 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11407": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11407 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1195": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1195 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1222": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1222 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1548": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1548 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1568": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1568 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1626": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1626 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "186": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/186 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3683": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3683 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3857": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3857 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3980": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3980 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4358081": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4358081 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4358083": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4358083 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4399279": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4399279 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4408315": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4408315 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4697379": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4697379 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4791222": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4791222 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4837368": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4837368 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4868733": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4868733 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5025": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5025 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5054388": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5054388 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5140": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5140 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5557": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5557 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5573": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5573 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5962": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5962 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6034": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6034 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6090": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6090 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6151": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6151 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6783": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6783 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "7110": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7110 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "962": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/962 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "18418": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18418 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "20906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/20906 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "9720": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9720 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "21300": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/21300 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "182": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/182 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "184": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/184 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "183": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/183 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "193": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/193 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "18267": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18267 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "185": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/185 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "6077": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/6077 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "20232": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/20232 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "187": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/187 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "18966": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18966 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "17362": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/17362 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "18986": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18986 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "189": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/189 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "17606": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/17606 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "190": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/190 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "12011": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/12011 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "10739": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/10739 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "9723": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9723 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "4771": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/4771 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "191": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/191 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "9726": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9726 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "21812": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/21812 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "7318": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/7318 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "9727": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9727 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 45), Image.ANTIALIAS),
            "10576": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10576 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1254": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1254 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1564": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1564 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "2552": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/2552 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4683964": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4683964 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4723205": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4723205 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4859": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4859 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5145292": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5145292 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5338": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5338 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "686": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/686 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6999": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6999 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9025": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9025 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Logan Sargeant": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Logan Sargeant Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Alexander Albon": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Alexander Albon Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Yuki Tsunoda": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Yuki Tsunoda Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Esteban Ocon": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Esteban Ocon Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Lance Stroll": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Lance Stroll Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Kevin Magnussen": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Kevin Magnussen Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Lando Norris": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Lando Norris Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Sergio Perez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Sergio Perez Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Carlos Sainz": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Carlos Sainz Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Pierre Gasly": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Pierre Gasly Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Charles Leclerc": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Charles Leclerc Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Valtteri Bottas": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Valtteri Bottas Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Fernando Alonso": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Fernando Alonso Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Guanyu Zhou": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Guanyu Zhou Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Oscar Piastri": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Oscar Piastri Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "George Russell": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/George Russell Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Nico Hulkenberg": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Nico Hulkenberg Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Lewis Hamilton": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Lewis Hamilton Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Max Verstappen": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Max Verstappen Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
            "Daniel Ricciardo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/drivers/Max Verstappen Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "F1 Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/f1logo.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "F1 Car": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/car.png"
            )
            .convert("RGB")
            .resize((125, 50), Image.ANTIALIAS),
            "Mercedes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/mercedes-logo.png"
            )
            .convert("RGB")
            .resize((30, 30), Image.ANTIALIAS),
            "Alpine": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/alpine-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((30, 30), Image.ANTIALIAS),
            "Haas F1 Team": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/haas-f1-team-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((40, 30), Image.ANTIALIAS),
            "Red Bull Racing": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/red-bull-racing-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 40), Image.ANTIALIAS),
            "McLaren": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/mclaren-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((30, 30), Image.ANTIALIAS),
            "Aston Martin": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/aston-martin-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 35), Image.ANTIALIAS),
            "RB": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/rb-logo.png"
            )
            .convert("RGB")
            .resize((50, 30), Image.ANTIALIAS),
            "Ferrari": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/ferrari-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((60, 35), Image.ANTIALIAS),
            "Kick Sauber": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/kick-sauber-logo Background Removed.png"
            )
            .convert("RGB")
            .resize((30, 30), Image.ANTIALIAS),  # Ensure the team name and file match
            "Williams": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/f1/teams/williams-logo.png"
            )
            .convert("RGB")
            .resize((30, 30), Image.ANTIALIAS),
        }
        while True:
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            # teal = graphics.Color(0, 255, 255)
            orange = graphics.Color(255, 165, 0)
            purple = graphics.Color(102, 0, 204)
            yellow = graphics.Color(255, 255, 0)
            white = graphics.Color(255, 255, 255)
            bFont = graphics.Font()
            bFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/8x13.bdf")
            font = graphics.Font()
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")
            smallFont = graphics.Font()
            smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf")
            smallestFont = graphics.Font()
            smallestFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")
            alilbiggerFont = graphics.Font()
            alilbiggerFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x7.bdf")
            middleFont = graphics.Font()
            middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf")
            print("getting responseArrrrrrrrr")
            user = userJSON["user"]
            # url = requests.get(
            #     f"https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/{user}"
            # )
            # # url = requests.get(f"http://10.0.0.22:3001/patrick/all-data-2/{user}")
            data = [
                [
                    ["ufc", "Allen vs. Curtis 2"],
                    [
                        "Nora Cornolle",
                        "Melissa Mullins",
                        "+280",
                        "-355",
                        "3:10",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "4916974",
                        "5127984",
                    ],
                    [
                        "Dylan Budka",
                        "Cesar Almeida",
                        "-140",
                        "+120",
                        "3:45",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "5032015",
                        "5144068",
                    ],
                    [
                        "Dan Argueta",
                        "Jean Matsumoto",
                        "+136",
                        "-162",
                        "4:15",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "4815973",
                        "5149439",
                    ],
                    [
                        "Pedro Falcão",
                        "Victor Hugo",
                        "+105",
                        "-130",
                        "4:45",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "3936279",
                        "4293183",
                    ],
                    [
                        "Germaine de Randamie",
                        "Norma Dumont",
                        "+100",
                        "-120",
                        "4:50",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "2552777",
                        "4418784",
                    ],
                    [
                        "Lukasz Brzeski",
                        "Valter Walker",
                        "+180",
                        "-230",
                        "5:45",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "4710386",
                        "5147389",
                    ],
                    [
                        "Court McGee",
                        "Alex Morono",
                        "+225",
                        "-300",
                        "5:59",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "2504639",
                        "3088232",
                    ],
                    [
                        "Charlie Campbell",
                        "Trevor Peek",
                        "-162",
                        "+136",
                        "6:15",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "4786358",
                        "5048900",
                    ],
                    [
                        "Christos Giagos",
                        "Ignacio Bahamondes",
                        "+240",
                        "-315",
                        "6:45",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "3089069",
                        "4038116",
                    ],
                    [
                        "Chepe Mariscal",
                        "Morgan Charrière",
                        "+105",
                        "-130",
                        "7:15",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "4040926",
                        "4324622",
                    ],
                    [
                        "Damon Jackson",
                        "Alexander Hernandez",
                        "+155",
                        "-185",
                        "7:45",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "3099187",
                        "4018757",
                    ],
                    [
                        "Chris Curtis",
                        "Brendan Allen",
                        "+195",
                        "-238",
                        "8:30",
                        "Allen vs. Curtis 2",
                        false,
                        false,
                        "2984770",
                        "4025699",
                    ],
                ],
                [
                    ["nhl logo", "nhllogo"],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-tampa-bay-lightning-logo.png",
                        250,
                        250,
                        250,
                        "Tampa Bay Lightning",
                        "https://loodibee.com/wp-content/uploads/nhl-pittsburgh-penguins-logo.png",
                        250,
                        250,
                        250,
                        "Pittsburgh Penguins",
                        "1:00",
                        "43-26-7",
                        "35-30-11",
                        "",
                        "-112",
                        "-108",
                        "6",
                        "",
                        "",
                        "4/6",
                        "1:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "ABC",
                        "",
                        "",
                        true,
                        "401560444",
                        "20",
                        "16",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-florida-panthers-logo.png",
                        229,
                        25,
                        55,
                        "Florida Panthers",
                        "https://loodibee.com/wp-content/uploads/nhl-boston-bruins-logo.png",
                        250,
                        250,
                        250,
                        "Boston Bruins",
                        "3:30",
                        "48-24-5",
                        "45-17-15",
                        "",
                        "-108",
                        "-112",
                        "5.5",
                        "",
                        "",
                        "4/6",
                        "3:30 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "ABC",
                        "",
                        "",
                        true,
                        "401560445",
                        "26",
                        "1",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-dallas-stars-logo.png",
                        32,
                        134,
                        76,
                        "Dallas Stars",
                        "https://loodibee.com/wp-content/uploads/nhl-chicago-blackhawks-logo.png",
                        227,
                        25,
                        55,
                        "Chicago Blackhawks",
                        "3:30",
                        "48-19-9",
                        "22-48-5",
                        "",
                        "-325",
                        "+260",
                        "6",
                        "",
                        "",
                        "4/6",
                        "3:30 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560447",
                        "9",
                        "4",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-winnipeg-jets-logo.png",
                        250,
                        250,
                        250,
                        "Winnipeg Jets",
                        "https://loodibee.com/wp-content/uploads/nhl-minnesota-wild-logo.png",
                        18,
                        71,
                        52,
                        "Minnesota Wild",
                        "4:00",
                        "46-24-6",
                        "36-29-10",
                        "",
                        "-125",
                        "+105",
                        "5.5",
                        "",
                        "",
                        "4/6",
                        "4:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560446",
                        "28",
                        "30",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-st-louis-blues-logo.png",
                        250,
                        250,
                        250,
                        "St. Louis Blues",
                        "https://loodibee.com/wp-content/uploads/nhl-san-jose-sharks-logo.png",
                        250,
                        250,
                        250,
                        "San Jose Sharks",
                        "6:00",
                        "40-32-4",
                        "17-50-8",
                        "",
                        "-230",
                        "+190",
                        "6",
                        "",
                        "",
                        "4/6",
                        "6:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560448",
                        "19",
                        "18",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-toronto-maple-leafs-logo.png",
                        250,
                        250,
                        250,
                        "Toronto Maple Leafs",
                        "https://loodibee.com/wp-content/uploads/nhl-montreal-canadiens-logo.png",
                        196,
                        18,
                        48,
                        "Montreal Canadiens",
                        "7:00",
                        "43-23-9",
                        "29-34-12",
                        "",
                        "-198",
                        "+164",
                        "6.5",
                        "",
                        "",
                        "4/6",
                        "7:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560449",
                        "21",
                        "10",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-new-jersey-devils-logo.png",
                        227,
                        11,
                        43,
                        "New Jersey Devils",
                        "https://loodibee.com/wp-content/uploads/nhl-ottawa-senators-logo.png",
                        221,
                        26,
                        50,
                        "Ottawa Senators",
                        "7:00",
                        "36-36-4",
                        "33-38-4",
                        "",
                        "-125",
                        "+105",
                        "6.5",
                        "",
                        "",
                        "4/6",
                        "7:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560450",
                        "11",
                        "14",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-philadelphia-flyers-logo.png",
                        254,
                        88,
                        35,
                        "Philadelphia Flyers",
                        "https://loodibee.com/wp-content/uploads/nhl-columbus-blue-jackets-logo.png",
                        250,
                        250,
                        250,
                        "Columbus Blue Jackets",
                        "7:00",
                        "36-30-11",
                        "25-39-12",
                        "",
                        "-166",
                        "+140",
                        "6.5",
                        "",
                        "",
                        "4/6",
                        "7:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560451",
                        "15",
                        "29",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-nashville-predators-logo.png",
                        253,
                        186,
                        49,
                        "Nashville Predators",
                        "https://loodibee.com/wp-content/uploads/nhl-new-york-islanders-logo.png",
                        250,
                        250,
                        250,
                        "New York Islanders",
                        "7:30",
                        "44-28-4",
                        "34-27-15",
                        "",
                        "-110",
                        "-110",
                        "6",
                        "",
                        "",
                        "4/6",
                        "7:30 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560452",
                        "27",
                        "12",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-edmonton-oilers-logo.png",
                        250,
                        250,
                        250,
                        "Edmonton Oilers",
                        "https://loodibee.com/wp-content/uploads/nhl-calgary-flames-logo.png",
                        221,
                        26,
                        50,
                        "Calgary Flames",
                        "10:00",
                        "46-24-5",
                        "34-36-5",
                        "",
                        "-170",
                        "+142",
                        "6.5",
                        "",
                        "",
                        "4/6",
                        "10:00 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560453",
                        "6",
                        "3",
                    ],
                    [
                        "game pregame nhl",
                        "https://loodibee.com/wp-content/uploads/nhl-vancouver-canucks-logo.png",
                        250,
                        250,
                        250,
                        "Vancouver Canucks",
                        "https://loodibee.com/wp-content/uploads/nhl-los-angeles-kings-logo.png",
                        250,
                        250,
                        250,
                        "Los Angeles Kings",
                        "10:00",
                        "47-21-8",
                        "40-25-11",
                        "",
                        "-105",
                        "-115",
                        "5.5",
                        "",
                        "",
                        "4/6",
                        "10:00 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "NHLPP|ESPN+",
                        "",
                        "",
                        true,
                        "401560454",
                        "22",
                        "8",
                    ],
                ],
                [
                    ["nba logo", "nbalogo"],
                    [
                        "game pregame nba",
                        "https://loodibee.com/wp-content/uploads/nba-cleveland-cavaliers-logo.png",
                        134,
                        0,
                        56,
                        "Cleveland Cavaliers",
                        "https://loodibee.com/wp-content/uploads/nba-los-angeles-lakers-logo.png",
                        85,
                        37,
                        131,
                        "Los Angeles Lakers",
                        "3:30",
                        "46-31",
                        "44-33",
                        "",
                        "+160",
                        "-192",
                        "229.5",
                        "",
                        "",
                        "4/6",
                        "3:30 PM",
                        "+4.5",
                        "-4.5",
                        [],
                        "",
                        "",
                        "",
                        true,
                        "401585755",
                        "5",
                        "13",
                    ],
                    [
                        "game pregame nba",
                        "https://loodibee.com/wp-content/uploads/nba-detroit-pistons-logo.png",
                        29,
                        66,
                        138,
                        "Detroit Pistons",
                        "https://loodibee.com/wp-content/uploads/nba-brooklyn-nets-logo.png",
                        250,
                        250,
                        250,
                        "Brooklyn Nets",
                        "7:00",
                        "13-64",
                        "30-47",
                        "",
                        "+285",
                        "-360",
                        "215",
                        "",
                        "",
                        "4/6",
                        "7:00 PM",
                        "+9",
                        "-9",
                        [],
                        "",
                        "",
                        "",
                        true,
                        "401585756",
                        "8",
                        "17",
                    ],
                    [
                        "game pregame nba",
                        "https://loodibee.com/wp-content/uploads/nba-philadelphia-76ers-logo.png",
                        29,
                        66,
                        138,
                        "Philadelphia 76ers",
                        "https://loodibee.com/wp-content/uploads/nba-memphis-grizzlies-logo.png",
                        93,
                        118,
                        169,
                        "Memphis Grizzlies",
                        "8:00",
                        "42-35",
                        "27-50",
                        "",
                        "-800",
                        "+550",
                        "211",
                        "",
                        "",
                        "4/6",
                        "8:00 PM",
                        "-12.5",
                        "+12.5",
                        [],
                        "",
                        "",
                        "",
                        true,
                        "401585757",
                        "20",
                        "29",
                    ],
                    [
                        "game pregame nba",
                        "https://loodibee.com/wp-content/uploads/nba-atlanta-hawks-logo.png",
                        200,
                        16,
                        46,
                        "Atlanta Hawks",
                        "https://loodibee.com/wp-content/uploads/nba-denver-nuggets-logo.png",
                        14,
                        34,
                        64,
                        "Denver Nuggets",
                        "9:00",
                        "36-41",
                        "53-24",
                        "",
                        "+525",
                        "-750",
                        "221",
                        "",
                        "",
                        "4/6",
                        "9:00 PM",
                        "+12",
                        "-12",
                        [],
                        "",
                        "",
                        "",
                        true,
                        "401585758",
                        "1",
                        "7",
                    ],
                ],
                [
                    ["mlb logo"],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png",
                        250,
                        250,
                        250,
                        "Oakland Athletics",
                        "https://loodibee.com/wp-content/uploads/mlb-detroit-tigers-logo.png",
                        250,
                        250,
                        250,
                        "Detroit Tigers",
                        "1:10",
                        "1-7",
                        "6-1",
                        "",
                        "+136",
                        "-162",
                        "8",
                        "P. Blackburn 0-0 0.00",
                        "K. Maeda 0-0 16.20",
                        "4/6",
                        "1:10 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568593",
                        "11",
                        "6",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png",
                        250,
                        250,
                        250,
                        "Cleveland Guardians",
                        "https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png",
                        3,
                        31,
                        64,
                        "Minnesota Twins",
                        "2:10",
                        "6-2",
                        "3-3",
                        "",
                        "+142",
                        "-170",
                        "7.5",
                        "C. Carrasco 0-0 5.40",
                        "J. Ryan 0-0 1.69",
                        "4/6",
                        "2:10 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568588",
                        "5",
                        "9",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-miami-marlins-logo.png",
                        250,
                        250,
                        250,
                        "Miami Marlins",
                        "https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png",
                        190,
                        10,
                        20,
                        "St. Louis Cardinals",
                        "2:15",
                        "0-8",
                        "4-4",
                        "",
                        "+124",
                        "-148",
                        "8",
                        "T. Rogers 0-0 7.20",
                        "S. Matz 0-0 3.38",
                        "4/6",
                        "2:15 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568591",
                        "28",
                        "24",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png",
                        223,
                        70,
                        1,
                        "Baltimore Orioles",
                        "https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png",
                        250,
                        250,
                        250,
                        "Pittsburgh Pirates",
                        "4:05",
                        "5-2",
                        "6-2",
                        "",
                        "-142",
                        "+120",
                        "8.5",
                        "T. Wells 0-1 4.50",
                        "B. Falter 0-0 13.50",
                        "4/6",
                        "4:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568585",
                        "1",
                        "23",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png",
                        250,
                        250,
                        250,
                        "Los Angeles Dodgers",
                        "https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png",
                        14,
                        51,
                        134,
                        "Chicago Cubs",
                        "4:05",
                        "7-3",
                        "5-2",
                        "",
                        "-192",
                        "+160",
                        "8",
                        "Y. Yamamoto 0-1 7.50",
                        "J. Wicks 0-0 4.50",
                        "4/6",
                        "4:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "FS1",
                        "",
                        "",
                        false,
                        "401568590",
                        "19",
                        "16",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png",
                        232,
                        24,
                        40,
                        "Philadelphia Phillies",
                        "https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png",
                        171,
                        0,
                        3,
                        "Washington Nationals",
                        "4:05",
                        "3-4",
                        "2-5",
                        "",
                        "-180",
                        "+150",
                        "8.5",
                        "R. Suarez 0-0 5.40",
                        "J. Irvin 0-0 5.40",
                        "4/6",
                        "4:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568594",
                        "22",
                        "20",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png",
                        250,
                        250,
                        250,
                        "New York Mets",
                        "https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png",
                        198,
                        1,
                        31,
                        "Cincinnati Reds",
                        "4:10",
                        "2-5",
                        "4-3",
                        "",
                        "+102",
                        "-122",
                        "9.5",
                        "L. Severino 0-1 5.40",
                        "N. Martinez 0-0 5.40",
                        "4/6",
                        "4:10 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568592",
                        "21",
                        "17",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-houston-astros-logo.png",
                        250,
                        250,
                        250,
                        "Houston Astros",
                        "https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png",
                        250,
                        250,
                        250,
                        "Texas Rangers",
                        "7:05",
                        "2-6",
                        "5-2",
                        "",
                        "-110",
                        "-110",
                        "10",
                        "J.P. France 0-0 4.76",
                        "J. Gray 0-0 12.27",
                        "4/6",
                        "7:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568589",
                        "18",
                        "13",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png",
                        19,
                        74,
                        142,
                        "Toronto Blue Jays",
                        "https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png",
                        19,
                        36,
                        72,
                        "New York Yankees",
                        "7:05",
                        "4-4",
                        "6-2",
                        "",
                        "-105",
                        "-115",
                        "7.5",
                        "K. Gausman 0-0 2.08",
                        "C. Schmidt 0-0 5.06",
                        "4/6",
                        "7:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "ESPN+",
                        "",
                        "",
                        false,
                        "401568598",
                        "14",
                        "10",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png",
                        250,
                        250,
                        250,
                        "Chicago White Sox",
                        "https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png",
                        250,
                        250,
                        250,
                        "Kansas City Royals",
                        "7:10",
                        "1-6",
                        "4-4",
                        "",
                        "+180",
                        "-218",
                        "9",
                        "C. Flexen 0-1 8.31",
                        "M. Wacha 0-0 5.40",
                        "4/6",
                        "7:10 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568587",
                        "4",
                        "7",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png",
                        250,
                        250,
                        250,
                        "Seattle Mariners",
                        "https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png",
                        19,
                        41,
                        75,
                        "Milwaukee Brewers",
                        "7:10",
                        "3-5",
                        "5-1",
                        "",
                        "+102",
                        "-122",
                        "8.5",
                        "B. Miller 0-1 7.20",
                        "D. Hall 0-0 4.50",
                        "4/6",
                        "7:10 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        true,
                        "401568596",
                        "12",
                        "8",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png",
                        170,
                        24,
                        44,
                        "Arizona Diamondbacks",
                        "https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png",
                        12,
                        35,
                        64,
                        "Atlanta Braves",
                        "7:20",
                        "4-4",
                        "4-2",
                        "",
                        "+180",
                        "-218",
                        "9",
                        "B. Pfaadt 1-0 1.80",
                        "M. Fried 0-0 40.50",
                        "4/6",
                        "7:20 PM",
                        "+1.5",
                        "-1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568584",
                        "29",
                        "15",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png",
                        9,
                        44,
                        92,
                        "Tampa Bay Rays",
                        "https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png",
                        51,
                        0,
                        111,
                        "Colorado Rockies",
                        "8:10",
                        "3-5",
                        "2-6",
                        "",
                        "-144",
                        "+122",
                        "11",
                        "T. Alexander 0-0 9.00",
                        "R. Feltner 0-1 5.40",
                        "4/6",
                        "8:10 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568597",
                        "30",
                        "27",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-san-diego-padres-logo.png",
                        62,
                        35,
                        18,
                        "San Diego Padres",
                        "https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png",
                        250,
                        250,
                        250,
                        "San Francisco Giants",
                        "9:05",
                        "4-6",
                        "3-5",
                        "",
                        "-102",
                        "-118",
                        "8",
                        "M. King 1-0 6.14",
                        "K. Winn 0-1 5.40",
                        "4/6",
                        "9:05 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "",
                        "",
                        "",
                        false,
                        "401568595",
                        "25",
                        "26",
                    ],
                    [
                        "game pregame mlb",
                        "https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png",
                        13,
                        43,
                        86,
                        "Boston Red Sox",
                        "https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png",
                        186,
                        0,
                        33,
                        "Los Angeles Angels",
                        "9:38",
                        "6-2",
                        "4-3",
                        "",
                        "-102",
                        "-118",
                        "8",
                        "G. Whitlock 1-0 1.80",
                        "R. Detmers 1-0 1.80",
                        "4/6",
                        "9:38 PM",
                        "-1.5",
                        "+1.5",
                        [],
                        "NESN",
                        "",
                        "",
                        false,
                        "401568586",
                        "2",
                        "3",
                    ],
                ],
                "MARGARITA TASTE OFF 2024!!!!!!!!",
                [
                    ["ncaa conference", "NCAA BBALL"],
                    [
                        "game pregame ncaaBasketball",
                        "https://loodibee.com/wp-content/uploads/ncaaBasketball-nc-state-wolfpack-logo.png",
                        204,
                        0,
                        0,
                        "#11 NC State Wolfpack",
                        "https://loodibee.com/wp-content/uploads/ncaaBasketball-purdue-boilermakers-logo.png",
                        250,
                        250,
                        250,
                        "#1 Purdue Boilermakers",
                        "6:09",
                        "26-14",
                        "33-4",
                        "",
                        "+340",
                        "-450",
                        "146.5",
                        "",
                        "",
                        "4/6",
                        "6:09 PM",
                        "+9.5",
                        "-9.5",
                        ["Big10", "ACC"],
                        "TBS",
                        "",
                        "",
                        true,
                        "401638643",
                        "152",
                        "2509",
                    ],
                    [
                        "game pregame ncaaBasketball",
                        "https://loodibee.com/wp-content/uploads/ncaaBasketball-alabama-crimson-tide-logo.png",
                        158,
                        22,
                        50,
                        "#4 Alabama Crimson Tide",
                        "https://loodibee.com/wp-content/uploads/ncaaBasketball-uconn-huskies-logo.png",
                        12,
                        35,
                        64,
                        "#1 UConn Huskies",
                        "8:49",
                        "25-11",
                        "35-3",
                        "",
                        "+500",
                        "-700",
                        "160.5",
                        "",
                        "",
                        "4/6",
                        "8:49 PM",
                        "+11.5",
                        "-11.5",
                        ["BigEast", "SEC"],
                        "TBS",
                        "",
                        "",
                        true,
                        "401638644",
                        "333",
                        "41",
                    ],
                ],
                [
                    ["golf", "Valero Texas Open", "Round 3 - In Progress"],
                    ["446", "", "Jimmy Walker", "", "74 • 3:14"],
                    ["4419142", "1", "Akshay Bhatia", "", "63 • 70 • 12:35"],
                    ["5409", "T2", "Russell Henley", "", "69 • 69 • 12:35"],
                    ["10054", "T2", "Denny McCarthy", "", "68 • 70 • 12:25"],
                    ["3454", "T2", "Brendon Todd", "", "66 • 72 • 12:35"],
                    ["3470", "5", "Rory McIlroy", "", "69 • 70 • 12:25"],
                    ["1614", "T6", "Webb Simpson", "", "73 • 67 • 12:15"],
                    ["5539", "T6", "Tommy Fleetwood", "", "71 • 69 • 12:25"],
                    ["10372", "T6", "Adam Schenk", "", "71 • 69 • 12:15"],
                    ["4684201", "T6", "Peter Kuest", "", "69 • 71 • 12:15"],
                    ["388", "T10", "Adam Scott", "-3(5)", "73 • 70"],
                    ["4375972", "T10", "Ludvig Åberg", "-3(5)", "72 • 71"],
                    ["9144", "T10", "Justin Lower", "-3(5)", "66 • 77"],
                    ["3857", "T10", "Kevin Chappell", "-3(2)", "69 • 73"],
                    ["9143", "T10", "Mark Hubbard", "", "73 • 68 • 11:45"],
                    ["9126", "T10", "Corey Conners", "", "70 • 71 • 11:45"],
                ],
            ]
            # responseArr = json.loads(url.text)
            responseArr = json.loads(data)
            filteredArr = [item for item in responseArr if item != " "]
            print(filteredArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = offscreen_canvas.width
            color = green
            for arr in filteredArr:
                running = True
                while running:
                    offscreen_canvas.Clear()
                    buffer = 6
                    pos -= 1
                    offset = 0
                    if isinstance(arr, list) and "mlb logo" in arr[0][0]:
                        for game in arr:
                            if "mlb logo" in game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogosMLB["MLB"], pos + offset, -9
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                awayTeamID = game[30]
                                homeTeamID = game[31]
                                try:
                                    value = teamLogosMLB[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosMLB[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[awayTeamID], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosMLB[awayTeamID].width,
                                    24,
                                    green,
                                    statusString,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + versus,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallestFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayTeam,
                                    12,
                                    white,
                                    awayTeamStatusString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallestFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam,
                                    26,
                                    white,
                                    homeTeamStatusString,
                                )
                                if awayTeam > homeTeam:
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus
                                        + buffer,
                                        12,
                                        awayBetsColor,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus
                                        + buffer,
                                        26,
                                        homeBetsColor,
                                        homeOddsString,
                                    )
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        12,
                                        yellow,
                                        OUString,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        26,
                                        yellow,
                                        overUnderString,
                                    )
                                else:
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus
                                        + buffer,
                                        12,
                                        awayBetsColor,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus
                                        + buffer,
                                        26,
                                        homeBetsColor,
                                        homeOddsString,
                                    )
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        12,
                                        yellow,
                                        OUString,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        26,
                                        yellow,
                                        overUnderString,
                                    )
                                if awayTeam > homeTeam:
                                    awayPitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        12,
                                        yellow,
                                        awayPitcherString,
                                    )
                                    homePitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayTeam
                                        + awayTeamStatus,
                                        26,
                                        yellow,
                                        homePitcherString,
                                    )
                                else:
                                    awayPitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        12,
                                        yellow,
                                        awayPitcherString,
                                    )
                                    homePitcher = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
                                        + teamLogosMLB[homeTeamID].width
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + homeTeam
                                        + homeTeamStatus,
                                        26,
                                        yellow,
                                        homePitcherString,
                                    )
                            if "inProgress" in game[0]:
                                bases = [[10, 5], [6, 0], [2, 5]]
                                outs = [[2, 20], [8, 20], [14, 20]]
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                pitcherNameString = game[17]
                                batterNameString = game[19]
                                inningString = game[20]
                                countString = game[21]
                                outsString = game[22]
                                awayOddsString = game[26]
                                homeOddsString = game[27]
                                overUnderString = game[28]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                awayTeamID = game[29]
                                homeTeamID = game[30]
                                try:
                                    value = teamLogosMLB[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosMLB[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[awayTeamID], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosMLB[awayTeamID].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                baseSize = 6
                                outsSize = 4
                                baseHalf = abs(baseSize / 2)
                                for base in bases:
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1],
                                        pos + offset + runningTotal + base[0],
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1],
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseSize,
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1] + baseSize,
                                        pos + offset + runningTotal + base[0],
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseHalf,
                                        base[1] + baseSize,
                                        pos
                                        + offset
                                        + runningTotal
                                        + base[0]
                                        + baseSize,
                                        base[1] + baseHalf,
                                        yellow,
                                    )
                                for out in outs:
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0],
                                        out[1],
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1],
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0],
                                        out[1],
                                        pos + offset + runningTotal + out[0],
                                        out[1] + outsSize,
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1] + outsSize,
                                        pos + offset + runningTotal + out[0],
                                        out[1] + outsSize,
                                        red,
                                    )
                                    graphics.DrawLine(
                                        offscreen_canvas,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1] + outsSize,
                                        pos + offset + runningTotal + out[0] + outsSize,
                                        out[1],
                                        red,
                                    )
                                if (
                                    "1st" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[0][0]
                                    y = bases[0][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    "2nd" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[1][0]
                                    y = bases[1][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    "3rd" in runnerSituationString
                                    or "Bases Loaded" in runnerSituationString
                                ):
                                    x = bases[2][0]
                                    y = bases[2][1]
                                    size = 6
                                    half = round(abs(size / 2))
                                    for testing in range(1, half + 1):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + size - testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + size - testing,
                                            yellow,
                                        )
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            - testing,
                                            y + testing,
                                            pos
                                            + offset
                                            + runningTotal
                                            + x
                                            + half
                                            + testing,
                                            y + testing,
                                            yellow,
                                        )
                                if (
                                    outsString == 1
                                    or outsString == 2
                                    or outsString == 3
                                ):
                                    x = outs[0][0]
                                    y = outs[0][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                if outsString == 2 or outsString == 3:
                                    x = outs[1][0]
                                    y = outs[1][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                if outsString == 3:
                                    x = outs[2][0]
                                    y = outs[2][1]
                                    size = 4
                                    for y_offset in range(size):
                                        graphics.DrawLine(
                                            offscreen_canvas,
                                            pos + offset + runningTotal + x,
                                            y + y_offset,
                                            pos + runningTotal + offset + x + outsSize,
                                            y + y_offset,
                                            red,
                                        )
                                situation = graphics.DrawText(
                                    offscreen_canvas,
                                    alilbiggerFont,
                                    pos + offset + runningTotal + 3,
                                    19,
                                    yellow,
                                    countString,
                                )
                                inning = graphics.DrawText(
                                    offscreen_canvas,
                                    alilbiggerFont,
                                    pos + offset + runningTotal - 5,
                                    31,
                                    yellow,
                                    inningString,
                                )
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + runningTotal + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + runningTotal + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + runningTotal + homeOdds + 50,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + runningTotal + homeOdds + 50,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                            if "final" in game[0]:
                                bases = [[2, 5], [6, 0], [10, 5]]
                                outs = [[3, 20], [9, 20], [15, 20]]
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                pitcherNameString = game[17]
                                batterNameString = game[19]
                                inningString = game[20]
                                countString = game[21]
                                outsString = game[22]
                                headline = game[29]
                                awayTeamID = game[30]
                                homeTeamID = game[31]
                                try:
                                    value = teamLogosMLB[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosMLB[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[awayTeamID], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosMLB[awayTeamID].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogosMLB[awayTeamID].width
                                    + versus
                                    + teamLogosMLB[homeTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogosMLB[awayTeamID].width
                                        + versus
                                        + teamLogosMLB[homeTeamID].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                            if "pregame" in game[0]:
                                offset = offset + 190
                            if "inProgress" in game[0]:
                                offset = offset + 190
                        time.sleep(0.015)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "nfl logo" in arr[0][0]:
                        for game in arr:
                            if "nfl logo" in game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogos["NFL"],
                                    pos + offset,
                                    -6,
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[20]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                offscreen_canvas.SetImage(
                                    teamLogosMLB[awayTeamID], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + 5
                                    + teamLogos[game[5]].width,
                                    14,
                                    green,
                                    dayString.split(",")[0].upper(),
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    26,
                                    green,
                                    statusString,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + versus,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    yellow,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    yellow,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awaySpread = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpread = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation,
                                    12,
                                    yellow,
                                    "O/U",
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                if possession == "away":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "•",
                                    )
                                elif statusString == "Halftime":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                else:
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        26,
                                        green,
                                        "•",
                                    )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    12,
                                    yellow,
                                    statusString,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    26,
                                    yellow,
                                    situationString,
                                )
                                newOffset = 0
                                if statusStr > situationStr:
                                    newOffset = statusStr
                                else:
                                    newOffset = situationStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + newOffset,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + newOffset,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + homeOdds,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + homeOdds,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + homeSpreadAmount,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + homeSpreadAmount,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 190
                            if "inProgress" in game[0]:
                                offset = offset + 190
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[game[5]], pos + offset, -5
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[game[10]],
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = (
                                        homeTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                else:
                                    scoreLocation = (
                                        awayTeam
                                        + buffer
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
                                    )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "ncaa" in arr[0][0]:
                        for game in arr:
                            if "conference" in game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogos["NCAA Logo"],
                                    pos + offset,
                                    -7,
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 120
                            pattern = r"#\d+\s"
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[20]
                                timeString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                overUnderText = ""
                                awayTeamID = game[30]
                                homeTeamID = game[31]
                                try:
                                    value = teamLogosNCAA[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosNCAA[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[awayTeamID],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosNCAA[awayTeamID].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosNCAA[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + newBuffer + buffer + buffer + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                homeSpread = 0
                                awaySpread = 0
                                if awaySpreadString != "":
                                    awaySpread = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        12,
                                        green if "+" in awaySpreadString else red,
                                        awaySpreadString,
                                    )
                                    homeSpread = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green if "+" in homeSpreadString else red,
                                        homeSpreadString,
                                    )
                                if awayOddsString != "":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + homeSpread,
                                        12,
                                        green if "+" in awayOddsString else red,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + scoreLocation
                                        + buffer
                                        + homeSpread,
                                        26,
                                        green if "+" in homeOddsString else red,
                                        homeOddsString,
                                    )
                                overUnderAmount = 0
                                if overUnderString != "":
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + homeSpread
                                        + scoreLocation,
                                        12,
                                        yellow,
                                        overUnderText,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + homeSpread
                                        + scoreLocation,
                                        26,
                                        yellow,
                                        overUnderString,
                                    )
                                dayStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + homeSpread
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    12,
                                    white,
                                    dayString,
                                )
                                timeStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + homeSpread
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    26,
                                    white,
                                    timeString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                awayTeamID = game[27]
                                homeTeamID = game[28]
                                try:
                                    value = teamLogosNCAA[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosNCAA[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[awayTeamID],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosNCAA[awayTeamID].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosNCAA[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                if possession == "away":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                elif statusString == "Halftime":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                else:
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        26,
                                        green,
                                        "",
                                    )
                                if statusString == "Halftime":
                                    statusStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + possessionPop,
                                        12,
                                        white,
                                        "HALF",
                                    )
                                else:
                                    statusStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + possessionPop,
                                        12,
                                        white,
                                        statusString.split(" - ")[0],
                                    )
                                if statusString != "Halftime":
                                    situationStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + possessionPop,
                                        26,
                                        white,
                                        statusString.split(" - ")[1],
                                    )
                                else:
                                    situationStr = 0
                                newOffset = 0
                                if statusStr > situationStr:
                                    newOffset = statusStr
                                else:
                                    newOffset = situationStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 115 + 50
                            if "inProgress" in game[0]:
                                offset = offset + 180 + 50
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                awayTeamID = game[30]
                                homeTeamID = game[31]
                                try:
                                    value = teamLogosNCAA[awayTeamID]
                                except KeyError:
                                    awayTeamID = "0000000000"
                                try:
                                    value = teamLogosNCAA[homeTeamID]
                                except KeyError:
                                    homeTeamID = "0000000000"
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[awayTeamID],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogosNCAA[awayTeamID].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogosNCAA[homeTeamID],
                                    pos
                                    + offset
                                    + teamLogosNCAA[awayTeamID].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 250
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 250
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "ufc" in arr[0][0]:
                        for game in arr:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 140
                            if "ufc" == game[0]:
                                offscreen_canvas.SetImage(
                                    mmaLogos["UFC Logo"],
                                    pos + offset,
                                    -7,
                                )
                                fightName = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + mmaLogos["UFC Logo"].width,
                                    18,
                                    white,
                                    game[1],
                                )
                            if "ufc" != game[0]:
                                awayTeamString = game[0]
                                homeTeamString = game[1]
                                awayOddsString = game[2]
                                homeOddsString = game[3]
                                timeString = game[4]
                                isAthOneWinner = game[6]
                                isAthTwoWinner = game[7]
                                athOneID = game[8]
                                athTwoID = game[9]
                                pattern = r"#\d+\s"
                                logoValueAway = athOneID
                                logoValueHome = athTwoID
                                try:
                                    value = mmaLogos[athOneID]
                                except KeyError:
                                    logoValueAway = "0000000000"
                                try:
                                    value = mmaLogos[athTwoID]
                                except KeyError:
                                    logoValueHome = "0000000000"
                                offscreen_canvas.SetImage(
                                    mmaLogos[logoValueAway],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + mmaLogos[logoValueAway].width,
                                    24,
                                    white,
                                    timeString,
                                )
                                offscreen_canvas.SetImage(
                                    mmaLogos[logoValueHome],
                                    pos
                                    + offset
                                    + mmaLogos[logoValueAway].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                if isAthOneWinner:
                                    awayColor = green
                                    homeColor = red
                                elif isAthTwoWinner:
                                    homeColor = green
                                    awayColor = red
                                else:
                                    awayColor = white
                                    homeColor = white
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                if awayOddsString != "n/a":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        12,
                                        green if "+" in awayOddsString else red,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green if "+" in homeOddsString else red,
                                        homeOddsString,
                                    )
                            if "pregame" in game[0]:
                                offset = offset + 100 + newBuffer
                            else:
                                offset = offset + homeTeam + 100 + newBuffer
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "f1" in arr[0][0]:
                        for game in arr:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 0
                            if "f1" == game[0]:
                                offscreen_canvas.SetImage(
                                    teamLogos["F1 Car"],
                                    pos + offset,
                                    -7,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos["F1 Logo"],
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + teamLogos["F1 Car"].width,
                                    -7,
                                )
                            if "f1" != game[0]:
                                teamName = game[0]
                                driverOne = game[1]
                                driverTwo = game[2]
                                pattern = r"#\d+\s"
                                offscreen_canvas.SetImage(
                                    teamLogos[teamName],
                                    pos + offset,
                                    0,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[driverOne],
                                    pos
                                    + offset
                                    + teamLogos[teamName].width
                                    + buffer
                                    + buffer,
                                    0,
                                )
                                driverOneText = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[driverOne].width
                                    + buffer
                                    + teamLogos[teamName].width,
                                    12,
                                    white,
                                    driverOne,
                                )
                                teamNameText = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[teamName].width
                                    + teamLogos[driverOne].width
                                    + buffer,
                                    26,
                                    white,
                                    teamName,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[driverTwo],
                                    pos
                                    + offset
                                    + teamLogos[teamName].width
                                    + teamLogos[driverOne].width
                                    + buffer
                                    + driverOneText
                                    + buffer
                                    + buffer
                                    + buffer,
                                    0,
                                )
                                driverTwoText = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + driverOneText
                                    + buffer
                                    + buffer
                                    + buffer
                                    + teamLogos[teamName].width
                                    + teamLogos[driverTwo].width
                                    + teamLogos[driverOne].width
                                    + buffer
                                    + buffer
                                    + newBuffer,
                                    12,
                                    white,
                                    driverTwo,
                                )
                                teamNameText2 = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + teamLogos[teamName].width
                                    + teamLogos[driverTwo].width
                                    + teamLogos[driverOne].width
                                    + buffer
                                    + buffer
                                    + driverOneText
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer,
                                    26,
                                    white,
                                    teamName,
                                )
                            if "f1" in game[0]:
                                offset = offset + 210 + newBuffer
                            else:
                                offset = offset + 400 + newBuffer
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "golf" in arr[0][0]:
                        for game in arr:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 120
                            if "golf" == game[0]:
                                tournamentName = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset,
                                    16,
                                    white,
                                    game[1],
                                )
                                offset = offset + 50
                            if "golf" != game[0]:
                                athID = game[0]
                                position = game[1]
                                # position = "1"
                                athleteName = game[2]
                                score = game[3]
                                # score = "-3"
                                teeTime = game[4]
                                pattern = r"#\d+\s"
                                positionText = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset,
                                    12,
                                    white,
                                    position,
                                )
                                scoreText = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset,
                                    26,
                                    (
                                        red
                                        if "-" in score
                                        else yellow if "E" in score else green
                                    ),
                                    score,
                                )
                                if scoreText > positionText:
                                    bufffer = scoreText
                                else:
                                    bufffer = positionText
                                logoValue = athID
                                try:
                                    value = teamLogos[athID]
                                except KeyError:
                                    logoValue = "0000000000"
                                offscreen_canvas.SetImage(
                                    teamLogos[logoValue],
                                    pos + offset + bufffer + buffer,
                                    0,
                                )
                                athleteNameText = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + positionText
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + bufffer,
                                    12,
                                    white,
                                    athleteName,
                                )
                                teeTimeText = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + positionText
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + bufffer,
                                    26,
                                    white,
                                    teeTime,
                                )
                                golfBallLocation = 0
                                if athleteNameText > teeTimeText:
                                    golfBallLocation = athleteNameText
                                else:
                                    golfBallLocation = teeTimeText
                                offscreen_canvas.SetImage(
                                    teamLogos["golfball"],
                                    pos
                                    + positionText
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + bufffer
                                    + golfBallLocation,
                                    5,
                                )
                            offset = offset + 100 + newBuffer + 60
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "xfl" in arr[0][0]:
                        for game in arr:
                            if "xfl" in game[0]:
                                conferenceName = graphics.DrawText(
                                    offscreen_canvas,
                                    font,
                                    pos + offset,
                                    26,
                                    green,
                                    "XFL",
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[20]
                                timeString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    12,
                                    yellow,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    26,
                                    yellow,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                if awaySpreadString != "":
                                    awaySpread = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        12,
                                        green,
                                        awaySpreadString,
                                    )
                                    homeSpread = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green,
                                        homeSpreadString,
                                    )
                                if awayOddsString != "":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + homeSpread,
                                        12,
                                        green,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + homeSpread,
                                        26,
                                        green,
                                        homeOddsString,
                                    )
                                overUnderAmount = 0
                                if overUnderString != "":
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + homeSpread
                                        + scoreLocation,
                                        12,
                                        green,
                                        overUnderText,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + homeSpread
                                        + scoreLocation,
                                        26,
                                        green,
                                        overUnderString,
                                    )
                                dayStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + homeSpread
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    12,
                                    yellow,
                                    dayString,
                                )
                                timeStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + homeSpread
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    26,
                                    yellow,
                                    timeString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                if possession == "away":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "•",
                                    )
                                elif statusString == "Halftime":
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        12,
                                        green,
                                        "",
                                    )
                                else:
                                    possessionPop = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer
                                        + buffer
                                        + buffer
                                        + 3,
                                        26,
                                        green,
                                        "•",
                                    )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    12,
                                    yellow,
                                    statusString,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + possessionPop,
                                    26,
                                    yellow,
                                    situationString,
                                )
                                newOffset = 0
                                if statusStr > situationStr:
                                    newOffset = statusStr
                                else:
                                    newOffset = situationStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 140
                            if "inProgress" in game[0]:
                                offset = offset + 220
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "soccer" in arr[0][0]:
                        for game in arr:
                            if "English Premier" == game[1]:
                                offscreen_canvas.SetImage(
                                    teamLogos["English Premier League Logo"],
                                    pos + offset,
                                    -7,
                                )
                            if "MLS" == game[1]:
                                offscreen_canvas.SetImage(
                                    teamLogos["MLS Logo"],
                                    pos + offset,
                                    -7,
                                )
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 120
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamLogo = awayTeamString
                                homeTeamLogo = homeTeamString
                                if "English Premier" == arr[0][1]:
                                    awayTeamLogo = awayTeamString
                                    homeTeamLogo = homeTeamString
                                if "MLS" == arr[0][1]:
                                    awayTeamLogo = game[30]
                                    homeTeamLogo = game[31]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[22]
                                timeString = game[21]
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamLogo],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamLogo].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamLogo],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamLogo].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                if awayOddsString != "":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        12,
                                        green if "+" in awayOddsString else red,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green if "+" in homeOddsString else red,
                                        homeOddsString,
                                    )
                                overUnderAmount = 0
                                if overUnderString != "":
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        12,
                                        yellow,
                                        overUnderText,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        26,
                                        yellow,
                                        overUnderString,
                                    )
                                dayStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    12,
                                    white,
                                    dayString.split(",")[0],
                                )
                                timeStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    26,
                                    white,
                                    timeString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                if "English Premier" == arr[0][1]:
                                    awayTeamLogo = awayTeamString
                                    homeTeamLogo = homeTeamString
                                if "MLS" == arr[0][1]:
                                    awayTeamLogo = game[30]
                                    homeTeamLogo = game[31]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green

                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamLogo],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamLogo].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamLogo],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamLogo].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    yellow,
                                    statusString,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    yellow,
                                    situationString,
                                )
                                newOffset = 0
                                if statusStr > situationStr:
                                    newOffset = statusStr
                                else:
                                    newOffset = situationStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 140
                            if "inProgress" in game[0]:
                                offset = offset + 220 + newBuffer
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamLogo = awayTeamString
                                homeTeamLogo = homeTeamString
                                if "English Premier" == arr[0][1]:
                                    awayTeamLogo = awayTeamString
                                    homeTeamLogo = homeTeamString
                                if "MLS" == arr[0][1]:
                                    awayTeamLogo = game[30]
                                    homeTeamLogo = game[31]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green

                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamLogo],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamLogo].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamLogo],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamLogo].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 240
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 240
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "nba" in arr[0][0]:
                        for game in arr:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 120
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[20]
                                timeString = game[21]
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                if awayOddsString != "":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + newBuffer
                                        + buffer,
                                        12,
                                        green,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green,
                                        homeOddsString,
                                    )
                                overUnderAmount = 0
                                if overUnderString != "":
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        12,
                                        green,
                                        overUnderText,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        26,
                                        green,
                                        overUnderString,
                                    )
                                dayStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    12,
                                    yellow,
                                    dayString,
                                )
                                timeStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    26,
                                    yellow,
                                    timeString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                if "of" in statusString:
                                    statusStringUpper = statusString.split(" of ")[0]
                                    statusStringLower = statusString.split(" of ")[
                                        1
                                    ].replace(" Period", "")
                                if "-" in statusString:
                                    statusStringUpper = statusString.split(" - ")[0]
                                    statusStringLower = statusString.split(" - ")[
                                        1
                                    ].replace(" Period", "")
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + newBuffer + offset + buffer + buffer + buffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + newBuffer + offset + buffer + buffer + buffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    yellow,
                                    statusStringUpper,
                                )
                                situationStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    yellow,
                                    statusStringLower,
                                )
                                newOffset = statusStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 115 + newBuffer
                            if "inProgress" in game[0]:
                                offset = offset + 180 + newBuffer
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + newBuffer
                                    + 130
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + newBuffer
                                    + 130
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "nhl" in arr[0][0]:
                        for game in arr:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            newBuffer = 120
                            if "pregame" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                statusString = game[11]
                                oddsString = game[14]
                                awayOddsString = game[15]
                                homeOddsString = game[16]
                                overUnderString = game[17]
                                dayString = game[20]
                                timeString = game[21]
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + newBuffer + buffer + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam
                                else:
                                    scoreLocation = awayTeam
                                awayOdds = 0
                                if awayOddsString != "":
                                    awayOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        12,
                                        green if "+" in awayOddsString else red,
                                        awayOddsString,
                                    )
                                    homeOdds = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + scoreLocation
                                        + buffer,
                                        26,
                                        green if "+" in homeOddsString else red,
                                        homeOddsString,
                                    )
                                overUnderAmount = 0
                                if overUnderString != "":
                                    overUnderStr = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        12,
                                        yellow,
                                        overUnderText,
                                    )
                                    overUnderAmount = graphics.DrawText(
                                        offscreen_canvas,
                                        smallFont,
                                        pos
                                        + offset
                                        + buffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + newBuffer
                                        + buffer
                                        + buffer
                                        + buffer
                                        + awayOdds
                                        + scoreLocation,
                                        26,
                                        yellow,
                                        overUnderString,
                                    )
                                dayStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    12,
                                    white,
                                    dayString,
                                )
                                timeStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + awayOdds
                                    + buffer
                                    + overUnderAmount
                                    + scoreLocation,
                                    26,
                                    white,
                                    timeString,
                                )
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                if "of" in statusString:
                                    statusStringUpper = statusString.split(" of ")[0]
                                    statusStringLower = statusString.split(" of ")[
                                        1
                                    ].replace(" Period", "")
                                if "-" in statusString:
                                    statusStringUpper = statusString.split(" - ")[0]
                                    statusStringLower = statusString.split(" - ")[
                                        1
                                    ].replace(" Period", "")
                                possession = game[17]
                                awayOddsString = game[19]
                                homeOddsString = game[20]
                                overUnderString = game[21]
                                awaySpreadString = game[22]
                                homeSpreadString = game[23]
                                OUString = ""
                                awayBetsColor = blue
                                homeBetsColor = blue
                                if "+" in awayOddsString:
                                    awayBetsColor = green
                                    homeBetsColor = red
                                else:
                                    awayBetsColor = red
                                    homeBetsColor = green
                                if overUnderString != "":
                                    OUString = "O/U"
                                    awayColor = red
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    12,
                                    white,
                                    statusStringUpper,
                                )
                                statusStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    26,
                                    white,
                                    statusStringLower,
                                )
                                newOffset = statusStr
                                awayOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awayOddsString,
                                )
                                homeOdds = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeOddsString,
                                )
                                overUnderStr = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    12,
                                    yellow,
                                    OUString,
                                )
                                overUnderAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + 35,
                                    26,
                                    yellow,
                                    overUnderString,
                                )
                                awaySpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    12,
                                    awayBetsColor,
                                    awaySpreadString,
                                )
                                homeSpreadAmount = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + scoreLocation
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newOffset
                                    + homeOdds
                                    + overUnderAmount
                                    + 35,
                                    26,
                                    homeBetsColor,
                                    homeSpreadString,
                                )
                            if "pregame" in game[0]:
                                offset = offset + 100 + newBuffer
                            if "inProgress" in game[0]:
                                offset = offset + 140 + newBuffer
                            if "final" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                statusString = game[11]
                                oddsString = game[14]
                                awayPitcherString = game[18]
                                homePitcherString = game[19]
                                runnerSituationString = game[15]
                                headline = game[29]
                                if int(awayTeamStatusString) < int(
                                    homeTeamStatusString
                                ):
                                    homeColor = green
                                    awayColor = red
                                elif int(awayTeamStatusString) == int(
                                    homeTeamStatusString
                                ):
                                    homeColor = yellow
                                    awayColor = yellow
                                else:
                                    homeColor = red
                                    awayColor = green
                                offscreen_canvas.SetImage(
                                    teamLogos[awayTeamString],
                                    pos + offset,
                                    -7,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[awayTeamString].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[homeTeamString],
                                    pos
                                    + offset
                                    + teamLogos[awayTeamString].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -7,
                                )
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    12,
                                    awayColor,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer + newBuffer,
                                    26,
                                    homeColor,
                                    homeTeamString,
                                )
                                scoreLocation = 0
                                if homeTeam > awayTeam:
                                    scoreLocation = homeTeam + buffer
                                else:
                                    scoreLocation = awayTeam + buffer
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + scoreLocation
                                    + buffer,
                                    12,
                                    awayColor,
                                    awayTeamStatusString,
                                )
                                homeTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos
                                    + offset
                                    + buffer
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + buffer
                                    + scoreLocation
                                    + buffer,
                                    26,
                                    homeColor,
                                    homeTeamStatusString,
                                )
                                runningTotal = (
                                    scoreLocation
                                    + buffer
                                    + buffer
                                    + newBuffer
                                    + awayTeamStatus
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                )
                                finalString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal,
                                    12,
                                    yellow,
                                    oddsString,
                                )
                                headlineString = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + runningTotal + newBuffer,
                                    26,
                                    green,
                                    headline,
                                )
                            if awayTeam > homeTeam:
                                offset = (
                                    offset
                                    + awayTeam
                                    + awayTeamStatus
                                    + headlineString
                                    + 205
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 205
                                )
                        time.sleep(0.018)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "stocks" in arr[0]:
                        for stock in arr[1]:
                            if stock["up"] == True:
                                color = green
                            if stock["up"] == False:
                                color = red
                            symbol = graphics.DrawText(
                                offscreen_canvas,
                                font,
                                pos + offset + buffer,
                                24,
                                color,
                                stock["stockSymbol"],
                            )
                            price = graphics.DrawText(
                                offscreen_canvas,
                                font,
                                pos + offset + buffer + symbol + buffer + buffer,
                                24,
                                color,
                                stock["regularMarketPrice"],
                            )
                            priceChange = graphics.DrawText(
                                offscreen_canvas,
                                smallFont,
                                pos
                                + offset
                                + buffer
                                + symbol
                                + price
                                + buffer
                                + buffer
                                + buffer,
                                12,
                                color,
                                stock["regularMarketChange"],
                            )
                            percentChange = graphics.DrawText(
                                offscreen_canvas,
                                smallFont,
                                pos
                                + offset
                                + buffer
                                + symbol
                                + price
                                + buffer
                                + buffer
                                + buffer,
                                26,
                                color,
                                stock["percentChange"],
                            )
                            highPrice = graphics.DrawText(
                                offscreen_canvas,
                                smallFont,
                                pos
                                + offset
                                + buffer
                                + symbol
                                + price
                                + percentChange
                                + buffer
                                + buffer
                                + buffer
                                + buffer
                                + buffer,
                                12,
                                color,
                                stock["regularMarketDayHigh"],
                            )
                            lowPrice = graphics.DrawText(
                                offscreen_canvas,
                                smallFont,
                                pos
                                + offset
                                + buffer
                                + symbol
                                + price
                                + percentChange
                                + buffer
                                + buffer
                                + buffer
                                + buffer
                                + buffer,
                                26,
                                color,
                                stock["regularMarketDayLow"],
                            )
                            offset = (
                                offset + symbol + price + percentChange + highPrice + 50
                            )
                        time.sleep(0.02)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "gainersDecliners" in arr[0]:
                        gainers = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 14, green, arr[1]["gainers"]
                        )
                        decliners = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 29, red, arr[1]["decliners"]
                        )
                        pos -= 1
                        time.sleep(0.022)
                        if pos + gainers < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "rssFeed" in arr[0]:
                        blackVs = graphics.DrawText(
                            offscreen_canvas, bFont, -500, 12, green, arr[1]
                        )
                        versus = graphics.DrawText(
                            offscreen_canvas,
                            bFont,
                            ((offscreen_canvas.width / 2) - (blackVs / 2)),
                            12,
                            blue,
                            arr[1],
                        )
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 26, green, arr[2]
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.021)
                    elif isinstance(arr, list) and "rssFeed" in arr[0]:
                        blackVs = graphics.DrawText(
                            offscreen_canvas, bFont, -500, 12, green, arr[1]
                        )
                        versus = graphics.DrawText(
                            offscreen_canvas,
                            bFont,
                            ((offscreen_canvas.width / 2) - (blackVs / 2)),
                            12,
                            blue,
                            arr[1],
                        )
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 26, green, arr[2]
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.021)
                    elif arr == None:
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == False:
                        # running = False
                        pos = offscreen_canvas.width
                    elif arr == "":
                        print("it was empty string")
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == "MAKE THE HOUSTON OPEN YOUR BITCH, JIMMY":
                        offscreen_canvas.SetImage(
                            teamLogos["446"],
                            pos + offset,
                            0,
                        )
                        mancavedisplays = graphics.DrawText(
                            offscreen_canvas, font, pos + 60, 26, orange, arr
                        )
                        offscreen_canvas.SetImage(
                            teamLogos["446"],
                            pos + mancavedisplays + 60 + offset,
                            0,
                        )
                        pos -= 1
                        if pos + 60 + mancavedisplays + 60 < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.025)
                    elif arr == "MANCAVEDISPLAYS":
                        www = graphics.DrawText(
                            offscreen_canvas, middleFont, pos, 26, green, "www."
                        )
                        mancavedisplays = graphics.DrawText(
                            offscreen_canvas, font, pos + www, 26, green, arr
                        )
                        com = graphics.DrawText(
                            offscreen_canvas,
                            middleFont,
                            pos + www + mancavedisplays,
                            26,
                            green,
                            ".com",
                        )
                        pos -= 1
                        if pos + www + mancavedisplays + com < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.018)
                    elif isinstance(arr, list) and ("rankings" in arr[0]):
                        blackVs = graphics.DrawText(
                            offscreen_canvas, bFont, -500, 12, green, arr[1]
                        )
                        versus = graphics.DrawText(
                            offscreen_canvas,
                            bFont,
                            ((offscreen_canvas.width / 2) - (blackVs / 2)),
                            12,
                            blue,
                            arr[1],
                        )
                        # versus2 = graphics.DrawText(offscreen_canvas, bFont,(offscreen_canvas.width / 2)+ versus + 25, 12, blue, arr[2])
                        length = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 26, green, arr[3]
                        )
                        pos -= 1
                        time.sleep(0.020)
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                    else:
                        length = graphics.DrawText(
                            offscreen_canvas, font, pos, 24, green, arr
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.021)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
