using rpi_rgb_led_matrix_sharp;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

class RunText : SampleBase
{
    private string[] leagueMembers = {
        "TEDDIE", "CALEB", "BILL", "BRAIN", "DUG", "JAPAN",
        "DUDDY", "DONNY", "OSCAR", "DENNY", "SNAKE", "ZANE"
    };
    private int currentRound = 1;
    private int currentPick = 1;
    private int seconds = 5;
    
    public RunText()
    {
    }
    
    public override void Run()
    {
        var offscreenCanvas = Matrix.CreateFrameCanvas();
        var font = new Graphics.Font();
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf");
        var middleFont = new Graphics.Font();
        middleFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/9x18B.bdf");
        var smallFont = new Graphics.Font();
        smallFont.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf");
        
        var green = new Graphics.Color(0, 255, 0);
        var red = new Graphics.Color(255, 0, 0);
        var blue = new Graphics.Color(0, 0, 255);
        var teal = new Graphics.Color(0, 255, 255);
        var purple = new Graphics.Color(102, 0, 204);
        var yellow = new Graphics.Color(255, 255, 0);
        var white = new Graphics.Color(255, 255, 255);
        var textColor = new Graphics.Color(255, 255, 0);
        
        while (true)
        {
            offscreenCanvas.Clear();
            string roundText = "Rd " + currentRound + "." + currentPick;
            Thread.Sleep(1000);
            seconds--;
            var timeColor = green;
            
            if (seconds < 60)
                timeColor = yellow;
            if (seconds < 20)
                timeColor = red;
            
            if (seconds == 60 || seconds == 59)
            {
                int blackHurryUpText = Graphics.DrawText(
                    offscreenCanvas,
                    middleFont,
                    -1000,
                    26,
                    green,
                    leagueMembers[currentPick] + " GET YOUR FINGER OUT YO ASS"
                );
                int hurryUpText = Graphics.DrawText(
                    offscreenCanvas,
                    middleFont,
                    (offscreenCanvas.Width / 2) - (blackHurryUpText / 2),
                    26,
                    green,
                    leagueMembers[currentPick] + " GET YOUR FINGER OUT YO ASS"
                );
            }
            // Handle other cases similarly
            
            if (seconds == -1)
            {
                Console.WriteLine("Press Enter to continue...");
                Console.ReadLine();
                currentPick++;
                seconds = 10;
                if (currentPick > 12)
                {
                    currentRound++;
                    currentPick = 1;
                }
            }
            
            offscreenCanvas = Matrix.SwapOnVSync(offscreenCanvas);
        }
    }

    public static void Main(string[] args)
    {
        var runText = new RunText();
        runText.Run();
    }
}
