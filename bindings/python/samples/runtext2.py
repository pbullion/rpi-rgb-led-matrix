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
        # crawfishLogo = Image.open(
        #         requests.get(
        #             "https://thumbs.dreamstime.com/b/shrimp-crayfish-black-background-beautiful-colour-nature-under-water-shrimp-crayfish-black-background-111681193.jpg",
        #             stream=True,
        #         ).raw
        #     ).convert("RGB").resize((50, 50), Image.ANTIALIAS)
        # venmoLogo = Image.open(
        #         requests.get(
        #             "https://is5-ssl.mzstatic.com/image/thumb/Purple122/v4/40/43/e8/4043e84a-182c-c361-5bf8-b14b472d41a6/AppIcon-1x_U007emarketing-0-7-0-85-220.png/512x512bb.jpg",
        #             stream=True,
        #         ).raw
        #     ).convert("RGB").resize((50, 50), Image.ANTIALIAS)
        # crawfishLogo2 = Image.open(
        #         requests.get(
        #             "https://i.pinimg.com/564x/bb/c2/95/bbc295ff2f2fd6e579d5c02c562bc230.jpg",
        #             stream=True,
        #         ).raw
        #     ).convert("RGB").resize((50, 50), Image.ANTIALIAS)
        teamLogos = {
            # "MLB": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_ Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
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
            # .resize((50, 50), Image.ANTIALIAS),
            # "Washington Nationals": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-Washington-Nationals- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Texas Rangers": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcvkAI8sinNSRfodR342oUFAo6JXPJUW9M8vM3yC5f3g&s",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "New York Mets": Image.open(
            #     requests.get(
            #         "https://www.mlbstatic.com/team-logos/share/121.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Miami Marlins": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO_zP8e4N4bDCCuMrkp1eGA7rIc8akKKqFmg&usqp=CAU",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Oakland Athletics": Image.open(
            #     requests.get(
            #         "https://1000logos.net/wp-content/uploads/2018/05/Oakland-Athletics-Logo-Color.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Kansas City Royals": Image.open(
            #     requests.get(
            #         "https://img.mlbstatic.com/mlb-images/image/private/t_1x1/t_w1024/mlb/y4j3k0mxap2tx6ozuac6.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Toronto Blue Jays": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Milwaukee Brewers": Image.open(
            #     requests.get(
            #         "https://purepng.com/public/uploads/large/milwaukee-brewers-logo-9xg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Boston Red Sox": Image.open(
            #     requests.get(
            #         "https://www.freepnglogos.com/uploads/boston-red-sox-logo-png/boston-red-sox-circle-hd-picture-download-11.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cleveland Guardians": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cincinnati Reds": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cincinnati_Reds_Logo.svg/1200px-Cincinnati_Reds_Logo.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "San Francisco Giants": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/bI0AAOSwqo1gMvNf/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Colorado Rockies": Image.open(
            #     requests.get(
            #         "https://cdn.cdnlogo.com/logos/c/19/colorado-rockies.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Minnesota Twins": Image.open(
            #     requests.get(
            #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW5d4zuFojuvYldGSmfFDf_L4YDpkGNNr1kP-gAUg&s",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Los Angeles Dodgers": Image.open(
            #     requests.get(
            #         "https://cdn.shopify.com/s/files/1/1949/1233/products/183165943449-0.jpg?v=1575428281",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Atlanta Braves": Image.open(
            #     requests.get(
            #         "https://images.fineartamerica.com/images/artworkimages/medium/1/atlanta-braves-logo-jeromi-cesk-transparent.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Seattle Mariners": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Seattle_Mariners_logo_%28low_res%29.svg/1200px-Seattle_Mariners_logo_%28low_res%29.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # # https://loodibee.com/wp-content/uploads/Seattle-Mariners-Logo-1977-1980-300x300.png
            # .convert("RGB").resize((50, 50), Image.ANTIALIAS),
            # "Los Angeles Angels": Image.open(
            #     requests.get(
            #         "https://media-s3-us-east-1.ceros.com/mlb/images/2022/05/31/20ba2e8b96bd79f5c4c3fe0367fed23f/patch.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Detroit Tigers": Image.open(
            #     requests.get(
            #         "https://1000logos.net/wp-content/uploads/2017/08/Detroit-Tigers-Logo-1994.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arizona Diamondbacks": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Philadelphia Phillies": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-Philadelphia-Phillies- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "San Diego Padres": Image.open(
            #     requests.get(
            #         "https://s.yimg.com/it/api/res/1.2/3.wJ5Gj6m_PwuYk8zbM0.g--~A/YXBwaWQ9eW5ld3M7dz0xMjAwO2g9NjMwO3E9MTAw/https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Pittsburgh Pirates": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tampa Bay Rays": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/ctwAAOSwYshgyTRa/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Baltimore Orioles": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/Baltimore-Orioles-Logo-1989-1991-300x300.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Chicago White Sox": Image.open(
            #     requests.get(
            #         "https://i.ebayimg.com/images/g/ducAAOSwXGxgQuJM/s-l500.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "St. Louis Cardinals": Image.open(
            #     requests.get(
            #         "https://i.pinimg.com/originals/34/2c/0b/342c0baa25c6344e9cb9e3dddaec3f25.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Chicago Cubs": Image.open(
            #     requests.get(
            #         "https://i.etsystatic.com/16901505/r/il/638115/1932889911/il_fullxfull.1932889911_4max.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Houston Astros": Image.open(
            #     requests.get(
            #         "https://images.ctfassets.net/iiozhi00a8lc/t117_favicon117_qgouernt_ehw9pj78_png/700d0ebafa92b5499f3dc09bf465fc98/t117_favicon.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Arizona Cardinals": Image.open(
            #     requests.get(
            #         "https://seeklogo.com/images/A/arizona-cardinals-logo-60AFACA5B9-seeklogo.com.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Atlanta Falcons": Image.open(
            #     requests.get(
            #         "https://cdn.freebiesupply.com/images/large/2x/atlanta-falcons-logo-on-black.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Baltimore Ravens": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b09.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Buffalo Bills": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/03/Buffalo_Bills_logo_blue-700x502.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Carolina Panthers": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/02/Carolina_Panthers_logo_blue-700x380.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Chicago Bears": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b16.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cincinnati Bengals": Image.open(
            #     requests.get(
            #         "https://cdn.freebiesupply.com/images/thumbs/1x/cincinnati-bengals- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Cleveland Browns": Image.open(
            #     requests.get(
            #         "https://i.redd.it/1rsnuls0llu71.jpg",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Jacksonville Jaguars": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b2f.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Las Vegas Raiders": Image.open(
            #     requests.get(
            #         "https://content.sportslogos.net/logos/7/6708/full/8521_las_vegas_raiders-primary-20201.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Dallas Cowboys": Image.open(
            #     requests.get(
            #         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/1076px-Dallas_Cowboys.svg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Denver Broncos": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b21.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Detroit Lions": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-detroit-lions-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Green Bay Packers": Image.open(
            #     requests.get(
            #         "https://seeklogo.com/images/G/green-bay-packers-logo-2A5FB2D033-seeklogo.com.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Houston Texans": Image.open(
            #     requests.get(
            #         "https://assets.stickpng.com/images/580b585b2edbce24c47b2b29.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Indianapolis Colts": Image.open(
            #     requests.get(
            #         "https://s.yimg.com/it/api/res/1.2/1U2AxCGOmhypKITxE2PNMw--~A/YXBwaWQ9eW5ld3M7dz0xMjAwO2g9NjMwO3E9MTAw/https://s.yimg.com/cv/apiv2/default/nfl/20190724/500x500/2019_IND_wbg.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Los Angeles Chargers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-los-angeles-chargers-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Los Angeles Rams": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/los-angeles-rams-2020- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Miami Dolphins": Image.open(
            #     requests.get(
            #         "https://logos-download.com/wp-content/uploads/2018/02/Miami_Dolphins_logo_bright-609x700.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Minnesota Vikings": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-minnesota-vikings-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            "Kansas City Chiefs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-kansas-city-chiefs-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # "New England Patriots": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-england-patriots-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "New Orleans Saints": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-orleans-saints-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "New York Giants": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-new-york-giants-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "New York Jets": Image.open(
            #     requests.get(
            #         "https://www.liblogo.com/img-logo/max/ne809n810-new-york-jets-logo-new-york-jets-logos-history-amp-images-logos-lists-brands.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Philadelphia Eagles": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-philadelphia-eagles-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Pittsburgh Steelers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-pittsburgh-steelers-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            "San Francisco 49ers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # "Seattle Seahawks": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-seattle-seahawks-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tampa Bay Buccaneers": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/tampa-bay-buccaneers-2020- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Tennessee Titans": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/nfl-tennessee-titans-team-logo-2.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            # "Washington Commanders": Image.open(
            #     requests.get(
            #         "https://loodibee.com/wp-content/uploads/washington-commanders- Background Removed.png",
            #         stream=True,
            #     ).raw
            # )
            # .convert("RGB")
            # .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Hawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hawks.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Boston Celtics": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/celtics.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Brooklyn Nets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nets.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Charlotte Hornets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hornets.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Bulls": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bulls.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Cavaliers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/cavs.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Dallas Mavericks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mavs.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Denver Nuggets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nuggets.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Pistons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pistons.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Golden State Warriors": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/warriors.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Rockets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/rockets.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indiana Pacers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pacers.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Clippers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/clippers.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Lakers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lakers.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Memphis Grizzlies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/grizzlies.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Heat": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/heat.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Milwaukee Bucks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bucks.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Timberwolves": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/twolves.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New Orleans Pelicans": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pelicans.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Knicks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/knicks.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oklahoma City Thunder": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/thunder.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Orlando Magic": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/magic.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia 76ers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/76ers.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Phoenix Suns": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/suns.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Portland Trail Blazers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blazers.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Sacramento Kings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kings.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Antonio Spurs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/spurs.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Toronto Raptors": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/raptors.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Utah Jazz": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/jazz.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Wizards": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wizards.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Ducks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ducks Background Removed.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Coyotes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coyotes Background Removed.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Blue Jackets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bluejackets Background Removed.png",
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Anaheim Ducks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ducks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Coyotes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coyotes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Boston Bruins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bruins Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Buffalo Sabres": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sabres Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Calgary Flames": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/flames Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Carolina Hurricanes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hurricanes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Blackhawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blackhawks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Colorado Avalanche": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/avalanche Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Columbus Blue Jackets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bluejackets Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Dallas Stars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/stars Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Red Wings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/redwings Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Edmonton Oilers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oilers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Florida Panthers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/panthers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Kings": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lakings Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Wild": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wild Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Montreal Canadiens": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/canadiens Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Nashville Predators": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/predators Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New Jersey Devils": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/devils Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Islanders": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/islanders Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Rangers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nyrangers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Ottawa Senators": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/senators Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia Flyers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/flyers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pittsburgh Penguins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/penguins Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Jose Sharks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sharks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seattle Kraken": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kraken Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "St. Louis Blues": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/blues Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tampa Bay Lightning": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lightning Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Toronto Maple Leafs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mapleleafs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Vancouver Canucks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/canucks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Vegas Golden Knights": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/goldenknights Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Capitals": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/capitals Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Winnipeg Jets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/winnipegjets Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # Big 12 Teams
            "BYU Cougars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/byucougars Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Baylor Bears": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/baylorbears Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Iowa State Cyclones": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/iowastatecyclones Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas Jayhawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kansasjayhawks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas State Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kansasstatewildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oklahoma Sooners": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oklahomasooners Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oklahoma State Cowboys": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oklahomastatecowboys Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "TCU Horned Frogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tcuhornedfrogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Texas Tech Red Raiders": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/texastechredraiders Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "West Virginia Mountaineers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/westvirginiamountaineers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Texas Longhorns": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/texaslonghorns Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # SEC Teams
            "Alabama Crimson Tide": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/alabamacrimsontide Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arkansas Razorbacks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/arkansasrazorbacks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Auburn Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/auburntigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Florida Gators": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/floridagators Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Georgia Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/georgiabulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kentucky Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/kentuckywildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "LSU Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lsutigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Mississippi State Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mississippistatebulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Missouri Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/missouritigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Ole Miss Rebels": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/olemissrebels Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "South Carolina Gamecocks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/southcarolinagamecocks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tennessee Volunteers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tennesseevolunteers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Texas A&M Aggies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/texasa&maggies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Vanderbilt Commodores": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/vanderbiltcommodores Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # Big Ten Teams
            "Illinois Fighting Illini": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/illinoisfightingillini Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indiana Hoosiers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/indianahoosiers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Iowa Hawkeyes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/iowahawkeyes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Maryland Terrapins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/marylandterrapins Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Michigan Wolverines": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/michiganwolverines Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Michigan State Spartans": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/michiganstatespartans Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Golden Gophers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/minnesotagoldengophers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Nebraska Cornhuskers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nebraskacornhuskers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Northwestern Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/northwesternwildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Ohio State Buckeyes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ohiostatebuckeyes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Penn State Nittany Lions": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pennstatenittanylions Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Purdue Boilermakers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/purdueboilermakers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Rutgers Scarlet Knights": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/rutgersscarletknights Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Wisconsin Badgers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wisconsinbadgers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # ACC Teams
            "Boston College Eagles": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bostoncollegeeagles Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Clemson Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/clemsontigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Duke Blue Devils": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/dukebluedevils Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Florida State Seminoles": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/floridastateseminoles Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Georgia Tech Yellow Jackets": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/georgiatechyellowjackets Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Louisville Cardinals": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/louisvillecardinals Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Hurricanes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/miamihurricanes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "North Carolina Tar Heels": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/northcarolinatarheels Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "NC State Wolfpack": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncstatewolfpack Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Notre Dame Fighting Irish": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/notredamefightingirish Background Removed.png"
            )
            .convert("RGB")
            .resize(
                (50, 50), Image.ANTIALIAS
            ),  # Note: Notre Dame is a partial ACC member for certain sports
            "Pittsburgh Panthers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pittsburghpanthers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Syracuse Orange": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/syracuseorange Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Virginia Cavaliers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/virginiacavaliers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Virginia Tech Hokies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/virginiatechhokies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Wake Forest Demon Deacons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wakeforestdemondeacons Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Bearcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/cincinnatibearcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "East Carolina Pirates": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/eastcarolinapirates Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Cougars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/houstoncougars Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Memphis Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/memphistigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Navy Midshipmen": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/navymidshipmen Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "SMU Mustangs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/smumustangs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "South Florida Bulls": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/southfloridabulls Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Temple Owls": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/templeowls Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tulane Green Wave": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tulanegreenwave Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tulsa Golden Hurricane": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tulsagoldenhurricane Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UCF Knights": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ucfknights Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Wichita State Shockers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wichitastateshockers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Butler Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/butlerbulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Creighton Bluejays": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/creightonbluejays Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "DePaul Blue Demons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/depaulbluedemons Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Georgetown Hoyas": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/georgetownhoyas Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Marquette Golden Eagles": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/marquettegoldeneagles Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Providence Friars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/providencefriars Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "St. John's Red Storm": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/stjohnsredstorm Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seton Hall Pirates": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/setonhallpirates Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Villanova Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/villanovawildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Florida Atlantic Owls": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/floridaatlanticowls Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Xavier Musketeers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/xaviermusketeers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UConn Huskies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/uconnhuskies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Air Force Falcons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/airforcefalcons Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Boise State Broncos": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/boisestatebroncos Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Colorado State Rams": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coloradostaterams Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Fresno State Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/fresnostatebulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Hawaii Rainbow Warriors": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/hawaiirainbowwarriors Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),  # Note: Hawaii football only
            "Nevada Wolf Pack": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nevadawolfpack Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New Mexico Lobos": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/newmexicolobos Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Diego State Aztecs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sandiegostateaztecs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Jose State Spartans": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sanjosestatespartans Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UNLV Rebels": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/unlvrebels Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Utah State Aggies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/utahstateaggies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Wyoming Cowboys": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wyomingcowboys Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Davidson Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/davidsonwildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Dayton Flyers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/daytonflyers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Duquesne Dukes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/duquesnedukes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Fordham Rams": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/fordhamrams Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "George Mason Patriots": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/georgemasonpatriots Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "George Washington Colonials": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/georgewashingtoncolonials Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "La Salle Explorers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lasalleexplorers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UMass Minutemen": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/umassminutemen Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Rhode Island Rams": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/rhodeislandrams Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Richmond Spiders": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/richmondspiders Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Saint Joseph's Hawks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/saintjosephshawks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Saint Louis Billikens": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/saintlouisbillikens Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "St. Bonaventure Bonnies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/stbonaventurebonnies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "VCU Rams": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/vcurams Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Bradley Braves": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/bradleybraves Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Drake Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/drakebulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Evansville Purple Aces": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/evansvillepurpleaces Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Illinois State Redbirds": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/illinoisstateredbirds Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indiana State Sycamores": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/indianastatesycamores Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Loyola Chicago Ramblers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/loyolachicagoramblers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Missouri State Bears": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/missouristatebears Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Northern Iowa Panthers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/northerniowapanthers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Southern Illinois Salukis": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/southernillinoissalukis Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Valparaiso Beacons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/valparaisobeacons Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Gonzaga Bulldogs": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/gonzagabulldogs Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Loyola Marymount Lions": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/loyolamarymountlions Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pacific Tigers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pacifictigers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pepperdine Waves": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pepperdinewaves Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Portland Pilots": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/portlandpilots Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Saint Mary's Gaels": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/saintmarysgaels Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Diego Toreros": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sandiegotoreros Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Francisco Dons": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sanfranciscodons Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Santa Clara Broncos": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/santaclarabroncos Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Wildcats": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/arizonawildcats Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona State Sun Devils": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/arizonastatesundevils Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "California Golden Bears": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/californiagoldenbears Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Colorado Buffaloes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/coloradobuffaloes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oregon Ducks": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oregonducks Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oregon State Beavers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/oregonstatebeavers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Stanford Cardinal": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/stanfordcardinal Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UCLA Bruins": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/uclabruins Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "USC Trojans": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/usctrojans Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Utah Utes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/utahutes Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Huskies": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/washingtonhuskies Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington State Cougars": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/washingtonstatecougars Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            # English Premier League Teams
            "AFC Bournemouth": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/afcbournemouth Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arsenal": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/arsenal Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Aston Villa": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/astonvilla Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Brentford": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/brentford Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Brighton & Hove Albion": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/brightonhovealbion Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Burnley": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/burnley Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chelsea": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/chelsea Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Crystal Palace": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/crystalpalace Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Everton": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/everton Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Fulham": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/fulham Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Luton Town": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/lutontown Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Leicester City": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/leicestercity Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Liverpool": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/liverpool Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Manchester City": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/manchestercity Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Manchester United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/manchesterunited Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Newcastle United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/newcastleunited Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Nottingham Forest": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/nottinghamforest Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Sheffield United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/sheffieldunited Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tottenham Hotspur": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/tottenhamhotspur Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Watford": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/watford Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "West Ham United": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/westhamunited Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Wolverhampton Wanderers": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/wolverhamptonwanderers Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "NCAA Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ncaalogo Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "English Premier League Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/englishpremierleague Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "UFC Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/ufclogo.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "MLS Logo": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mlslogo.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Muhammad Naimov": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/muhammadnaimov.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Erik Silva": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/eriksilva.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Victor Altamirano": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/victoraltamirano.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Felipe dos Santos": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/felipedossantos.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Ronaldo Rodriguez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/luisrodriguez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Luis Rodriguez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/luisrodriguez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Denys Bondar": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/denysbondar.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Claudio Puelles": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/claudiopuelles.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Farés Ziam": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/faresziam.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Daniel Lacerda": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/daniellacerda.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Édgar Cháirez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/edgarchairez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Jesus Aguilar": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jesusaguilar.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Mateus Mendonca": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/mateusmendonca.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Raoni Barcelos": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/raonibarcelos.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Cristian Quiñonez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/cristianquinonez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Chris Duncan": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/chrisduncan.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Manuel Torres": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/manueltorres.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Sam Hughes": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/samhughes.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Yazmin Jauregui": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yazminjauregui.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Ricky Turcios": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/rickyturcios.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Raul Rosas Jr.": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/raulrosasjr.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Daniel Zellhuber": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/danielzellhuber.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Francisco Prado": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/franciscoprado.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Brian Ortega": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brianortega.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Yair Rodriguez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yairrodriguez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Brandon Moreno": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brandonmoreno.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Brandon Royval": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/brandonroyval.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Loik Radzhabov": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/loikradzhabov.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Vinicius Oliveira": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/viniciusoliveira.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Yanis Ghemmouri": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/yanisghemmouri.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Christian Leroy Duncan": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/christianleroyduncan.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Claudio Ribeiro": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/claudioribeiro.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Aiemann Zahabi": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/aiemannzahabi.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Javid Basharat": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/javidbasharat.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Ludovit Klein": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/ludovitklein.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Joel Alvarez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/joelalvarez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Eryk Anders": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/erykanders.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Jamie Pickett": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jamiepickett.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Matt Schnell": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/mattschnell.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Steve Erceg": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/steveerceg.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Umar Nurmagomedov": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/umarnurmagomedov.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Alex Perez": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/alexperez.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Muhammad Mokaev": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/muhammadmokaev.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Tyson Pedro": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/tysonpedro.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Abdul-Kareem Al-Selwady": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/tysonpedro.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Vitor Petrino": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/vitorpetrino.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Jairzinho Rozenstruik": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/jairzinhorozenstruik.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "Shamil Gaziev": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mma/shamilgaziev.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
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
            "10548": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10548 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10562": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10562 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10583": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10583 Background Removed.png"
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
            "10906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10906 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10929": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10929 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10990": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10990 Background Removed.png"
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
            "11143": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11143 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11183": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11183 Background Removed.png"
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
            "11376": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11376 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11385": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11385 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11393": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11393 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11407": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11407 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11456": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11456 Background Removed.png"
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
            "1483": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1483 Background Removed.png"
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
            "3970": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3970 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "3980": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3980 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4251": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4251 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4355673": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4355673 Background Removed.png"
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
            "4408316": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4408316 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4423323": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4423323 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4426181": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4426181 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4566443": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4566443 Background Removed.png"
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
            "4633": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4633 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4697379": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4697379 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4698579": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4698579 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4791222": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4791222 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4837": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4837 Background Removed.png"
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
            "5962": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5962 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6017": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6017 Background Removed.png"
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
            "6701": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6701 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6783": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6783 Background Removed.png"
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
            "7083": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7083 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "7110": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7110 Background Removed.png"
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
            "8974": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8974 Background Removed.png"
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
            "9364": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9364 Background Removed.png"
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
            "962": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/962 Background Removed.png"
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
            "9951": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9951 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "18418": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18418 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "20906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/20906 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "9720": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9720 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "21300": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/21300 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "182": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/182 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "184": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/184 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "183": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/183 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "193": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/193 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "18267": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18267 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "185": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/185 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "6077": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/6077 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "20232": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/20232 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "187": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/187 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "18966": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18966 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "17362": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/17362 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "18986": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/18986 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "189": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/189 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "17606": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/17606 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "190": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/190 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "12011": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/12011 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "10739": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/10739 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "9723": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9723 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "4771": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/4771 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "191": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/191 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "9726": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9726 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "21812": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/21812 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "7318": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/7318 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "9727": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/mls/9727 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "10048": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10048 Background Removed.png"
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "10054": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10054 Background Removed.png"
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
            "10576": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10576 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1059": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1059 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "10596": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/10596 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1077": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1077 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "11382": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/11382 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1254": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1254 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1264": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1264 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1564": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1564 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "1651": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/1651 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "2552": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/2552 Background Removed.png"
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
            "3832": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/3832 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4349547": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4349547 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4364752": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4364752 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4372851": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4372851 Background Removed.png"
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
            "4425906": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4425906 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4587": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4587 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4602673": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4602673 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "4638": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4638 Background Removed.png"
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
            "4832046": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/4832046 Background Removed.png"
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
            "5285": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5285 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5338": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5338 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "5409": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/5409 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "569": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/569 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "6011": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/6011 Background Removed.png"
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
            "676": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/676 Background Removed.png"
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
            "7001": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/7001 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "8961": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/8961 Background Removed.png"
            )
            .convert("RGB")
            .resize((55, 40), Image.ANTIALIAS),
            "9025": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9025 Background Removed.png"
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
            "9243": Image.open(
                "/home/pi/rpi-rgb-led-matrix/bindings/python/samples/images/logos/pga/9243 Background Removed.png"
            )
            .convert("RGB")
            .resize((45, 40), Image.ANTIALIAS),
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
            .resize((55, 40), Image.ANTIALIAS),
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
            url = requests.get(
                f"https://sheline-art-website-api.herokuapp.com/patrick/all-data-2/{user}"
            )
            # url = requests.get(f"http://10.0.0.22:3001/patrick/all-data-2/{user}")
            responseArr = json.loads(url.text)
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
                                    teamLogos["MLB"], pos + offset, -9
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
                                    teamLogos[game[5]], pos + offset, -10
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + buffer + teamLogos[game[5]].width,
                                    24,
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
                                    -10,
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
                                    white,
                                    awayTeamString,
                                )
                                awayTeamStatus = graphics.DrawText(
                                    offscreen_canvas,
                                    smallestFont,
                                    pos
                                    + offset
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
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
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
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
                                    + teamLogos[game[5]].width
                                    + versus
                                    + teamLogos[game[10]].width
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + teamLogos[game[10]].width
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
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
                                        + teamLogos[game[5]].width
                                        + versus
                                        + homeOdds
                                        + overUnderStr
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
                                    teamLogos[game[5]], pos + offset, -10
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
                                    -10,
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
                                    teamLogos[game[5]], pos + offset, -10
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
                                    -10,
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
                                    teamLogos[game[5]], pos + offset, -10
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
                                    -10,
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
                                    teamLogos[game[5]], pos + offset, -10
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
                                    -10,
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
                                    teamLogos[game[5]], pos + offset, -10
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
                                    -10,
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
                                    -10,
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
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                offscreen_canvas.SetImage(
                                    teamLogos[re.sub(pattern, "", awayTeamString)],
                                    pos + offset,
                                    -10,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[re.sub(pattern, "", homeTeamString)],
                                    pos
                                    + offset
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
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
                                    teamLogos[re.sub(pattern, "", awayTeamString)],
                                    pos + offset,
                                    -10,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[re.sub(pattern, "", homeTeamString)],
                                    pos
                                    + offset
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
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
                                    teamLogos[re.sub(pattern, "", awayTeamString)],
                                    pos + offset,
                                    -10,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos
                                    + offset
                                    + buffer
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width,
                                    24,
                                    white,
                                    "vs",
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[re.sub(pattern, "", homeTeamString)],
                                    pos
                                    + offset
                                    + teamLogos[
                                        re.sub(pattern, "", awayTeamString)
                                    ].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    -10,
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
                                    teamLogos["UFC Logo"],
                                    pos + offset,
                                    -10,
                                )
                                fightName = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + teamLogos["UFC Logo"].width,
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
                                pattern = r"#\d+\s"
                                logoValueAway = awayTeamString
                                logoValueHome = homeTeamString
                                try:
                                    value = teamLogos[awayTeamString]
                                except KeyError:
                                    logoValueAway = "0000000000"
                                try:
                                    value = teamLogos[homeTeamString]
                                except KeyError:
                                    logoValueHome = "0000000000"
                                offscreen_canvas.SetImage(
                                    teamLogos[logoValueAway],
                                    pos + offset,
                                    0,
                                )
                                versus = graphics.DrawText(
                                    offscreen_canvas,
                                    middleFont,
                                    pos + offset + teamLogos[logoValueAway].width,
                                    24,
                                    white,
                                    timeString,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos[logoValueHome],
                                    pos
                                    + offset
                                    + teamLogos[logoValueAway].width
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer,
                                    0,
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
                                    teamLogos["F1 Logo"],
                                    pos + offset,
                                    -10,
                                )
                                offscreen_canvas.SetImage(
                                    teamLogos["F1 Car"],
                                    pos + offset + 60,
                                    -10,
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
                                offset = offset + 160 + newBuffer
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
                            offset = offset + 100 + newBuffer + 10
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
                                    -10,
                                )
                            if "MLS" == game[1]:
                                offscreen_canvas.SetImage(
                                    teamLogos["MLS Logo"],
                                    pos + offset,
                                    -10,
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
                                print(arr[0][0])
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    statusString.split(" - ")[0],
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
                                    statusString.split(" - ")[1],
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    -10,
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
                                    + 180
                                )
                            else:
                                offset = (
                                    offset
                                    + homeTeam
                                    + homeTeamStatus
                                    + headlineString
                                    + 180
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
                            offscreen_canvas, bFont, -1000, 12, green, arr[1]
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
                            offscreen_canvas, bFont, -1000, 12, green, arr[1]
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
                        running = False
                        pos = offscreen_canvas.width
                    elif arr == "":
                        print("it was empty string")
                        running = False
                        pos = offscreen_canvas.width
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
                            offscreen_canvas, bFont, -1000, 12, green, arr[1]
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
