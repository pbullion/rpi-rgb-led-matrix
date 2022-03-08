#!/usr/bin/env python
#Display a runtext with double-buffering.
#path = cd /home/pi/rpi-rgb-led-matrix/bindings/python/samples
#run = sudo python stones.py --led-slowdown-gpio=4 --led-cols=64 --led-chain=8
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import multiprocessing
import yfinance as yf
import threading
from PIL import Image

class RunText(SampleBase):
    def init(self, *args, **kwargs):
        super(RunText, self).init(*args, **kwargs)
        #new
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/nvdia.ppm" )
        #ticker data holder
        self.tickerData = {}
        #list of tickers
        self.tickers = ["MSFT", "NVDA", "DIS"]

        self.maxTickers = len(self.tickers)
        
        self.counter = 0
    
    
def updateTickerData(self, i):
    #ticker data
    data = yf.Ticker(self.tickers[self.counter])
    self.greeting = str(data.info['regularMarketOpen'])
    #fun.greeting = str(fun.counter) (maybe don't need)
    
    #print(fun.tickers[fun.counter] + " is valued at " + "$" + str(current.info['regularMarketOpen']))
    #threading.Thread(target=getTicker).start()
   
def run(self):
    if not 'image' in self.__dict__:
        self.image = Image.open(self.args.image)
        print("hello i did it")
    self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
    
    offscreen_canvas = self.matrix.CreateFrameCanvas()
    
    #self.data
    font = graphics.Font()
    font.LoadFont("../../../fonts/aver-20.bdf")
    textColor = graphics.Color(255, 255, 255)
    pos = offscreen_canvas.width
    data = yf.Ticker(self.tickers[self.counter])
    self.greeting = "THE PRICE OF " + self.tickers[self.counter] + " IS " + "!!!" + str(data.info['regularMarketOpen'])
    print(self.greeting)
    my_text = self.greeting
    #self.image
    
    while True:
        offscreen_canvas.Clear()
        img_width, img_height = self.image.size
        len = graphics.DrawText(offscreen_canvas, font, pos, 22, textColor, my_text) + img_width
        pos -= 1
        if (pos + len < 0):
            if (self.counter < 2):
                self.counter += 1
            else:
                self.counter = 0
            print(self.counter)
            pos = offscreen_canvas.width
            
            #offscreen_canvas.Clear()
            run_text.run()
            # self.cryptoData = self.return_dict['data']
            
            

        time.sleep(.05)

        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
#Main function
if name == "main":
run_text = RunText()
if (not run_text.process()):
run_text.print_help()

`