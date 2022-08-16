#!/usr/bin/env python
# Display a runtext with double-buffering.
from ast import If
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests, json
import json
from PIL import Image

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
        teamLogos = {
            "MLB": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/Major_League_Baseball_MLB_transparent_logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "NFL": Image.open(
                requests.get(
                    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/National_Football_League_logo.svg/1200px-National_Football_League_logo.svg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((40, 40), Image.ANTIALIAS),
            "New York Yankees": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-new-york-yankees-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Nationals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-washington-nationals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Texas Rangers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-texas-rangers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Mets": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-new-york-mets-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Marlins": Image.open(
                requests.get(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO_zP8e4N4bDCCuMrkp1eGA7rIc8akKKqFmg&usqp=CAU",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Oakland Athletics": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-oakland-athletics-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas City Royals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-kansas-city-royals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Toronto Blue Jays": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-toronto-blue-jays-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Milwaukee Brewers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-milwaukee-brewers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Boston Red Sox": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-boston-red-sox-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Guardians": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-cleveland-guardians-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Reds": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-cincinnati-reds-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Francisco Giants": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-san-francisco-giants-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Colorado Rockies": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-colorado-rockies-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Twins": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-minnesota-twins-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Dodgers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-los-angeles-dodgers-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Braves": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-atlanta-braves-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seattle Mariners": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-seattle-mariners-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Angels": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-los-angeles-angels-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Tigers": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2016/04/Detroit_Tigers_Insignia_logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Diamondbacks": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-arizona-diamondbacks-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia Phillies": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-philadelphia-phillies-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Diego Padres": Image.open(
                requests.get(
                    "https://s.yimg.com/cv/apiv2/default/mlb/20200508/500x500/padres_wbgs.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pittsburgh Pirates": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-pittsburgh-pirates-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tampa Bay Rays": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-tampa-bay-rays-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Baltimore Orioles": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-baltimore-orioles-logo-bird.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago White Sox": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-chicago-white-sox-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "St. Louis Cardinals": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-st-louis-cardinals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Cubs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/mlb-chicago-cubs-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Astros": Image.open(
                requests.get(
                    "https://images.ctfassets.net/iiozhi00a8lc/t117_favicon117_qgouernt_ehw9pj78_png/700d0ebafa92b5499f3dc09bf465fc98/t117_favicon.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Arizona Cardinals": Image.open(
                requests.get(
                    "https://seeklogo.com/images/A/arizona-cardinals-logo-60AFACA5B9-seeklogo.com.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Atlanta Falcons": Image.open(
                requests.get(
                    "https://cdn.freebiesupply.com/images/large/2x/atlanta-falcons-logo-on-black.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Baltimore Ravens": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b09.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Buffalo Bills": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/03/Buffalo_Bills_logo_blue-700x502.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Carolina Panthers": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/02/Carolina_Panthers_logo_blue-700x380.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Chicago Bears": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b16.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cincinnati Bengals": Image.open(
                requests.get(
                    "https://cdn.freebiesupply.com/images/thumbs/1x/cincinnati-bengals-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Cleveland Browns": Image.open(
                requests.get(
                    "https://i.redd.it/1rsnuls0llu71.jpg",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Jacksonville Jaguars": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b2f.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Las Vegas Raiders": Image.open(
                requests.get(
                    "https://content.sportslogos.net/logos/7/6708/full/8521_las_vegas_raiders-primary-20201.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Dallas Cowboys": Image.open(
                requests.get(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/1076px-Dallas_Cowboys.svg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Denver Broncos": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b21.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Detroit Lions": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-detroit-lions-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Green Bay Packers": Image.open(
                requests.get(
                    "https://seeklogo.com/images/G/green-bay-packers-logo-2A5FB2D033-seeklogo.com.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Houston Texans": Image.open(
                requests.get(
                    "https://assets.stickpng.com/images/580b585b2edbce24c47b2b29.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Indianapolis Colts": Image.open(
                requests.get(
                    "https://s.yimg.com/it/api/res/1.2/1U2AxCGOmhypKITxE2PNMw--~A/YXBwaWQ9eW5ld3M7dz0xMjAwO2g9NjMwO3E9MTAw/https://s.yimg.com/cv/apiv2/default/nfl/20190724/500x500/2019_IND_wbg.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Chargers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-los-angeles-chargers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Los Angeles Rams": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/los-angeles-rams-2020-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Miami Dolphins": Image.open(
                requests.get(
                    "https://logos-download.com/wp-content/uploads/2018/02/Miami_Dolphins_logo_bright-609x700.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Minnesota Vikings": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-minnesota-vikings-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Kansas City Chiefs": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-kansas-city-chiefs-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New England Patriots": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-england-patriots-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New Orleans Saints": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-orleans-saints-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Giants": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-new-york-giants-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "New York Jets": Image.open(
                requests.get(
                    "https://www.liblogo.com/img-logo/max/ne809n810-new-york-jets-logo-new-york-jets-logos-history-amp-images-logos-lists-brands.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Philadelphia Eagles": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-philadelphia-eagles-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Pittsburgh Steelers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-pittsburgh-steelers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "San Francisco 49ers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Seattle Seahawks": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-seattle-seahawks-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tampa Bay Buccaneers": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/tampa-bay-buccaneers-2020-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Tennessee Titans": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/nfl-tennessee-titans-team-logo-2.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
            "Washington Commanders": Image.open(
                requests.get(
                    "https://loodibee.com/wp-content/uploads/washington-commanders-logo.png",
                    stream=True,
                ).raw
            )
            .convert("RGB")
            .resize((50, 50), Image.ANTIALIAS),
        }
        while True:
            green = graphics.Color(0, 255, 0)
            red = graphics.Color(255, 0, 0)
            blue = graphics.Color(0, 0, 255)
            teal = graphics.Color(0, 255, 255)
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
            # responseArr = json.loads(url.text)
            responseArr = [
                [
                    "gainersDecliners",
                    {
                        "gainers": "BioAtla Inc. (BCAB) 11.87 48.38% • Artelo Biosciences Inc. (ARTL) 6.36 45.87% • fuboTV Inc. (FUBO) 6.35 44.98% • Forza X1 Inc. (FRZA) 8.25 36.14% • SkyWater Technology Inc. (SKYT) 18.95 32.98% • Ventyx Biosciences Inc. (VTYX) 24.55 31.99% • Kirkland's Inc. (KIRK) 5.29 31.92% • IonQ Inc. (IONQ) 8.38 31.76% • Bed Bath & Beyond Inc. (BBBY) 20.65 29.06% • Blend Labs Inc. (BLND) 3.55 28.62% • Navitas Semiconductor Corp. (NVTS) 7.76 25.97% • Global-E Online Ltd. (GLBE) 34.00 24.36% • AMTD IDEA Group ADR (AMTD) 2.81 24.34% • Energy Services of America Corp. (ESOA) 2.97 24.01% • RealReal Inc. (REAL) 3.37 22.55% • Quest Resource Holding Corp. (QRHC) 6.01 20.93% • F45 Training Holdings Inc. (FXLV) 2.44 20.79% • Advanced Emissions Solutions Inc. (ADES) 5.92 20.57% • Stitch Fix Inc. Cl A (SFIX) 8.56 20.22% • Accelerate Diagnostics Inc. (AXDX) 3.19 19.03% • Nu Holdings Ltd. Cl A (NU) 5.52 17.95% • ThredUp Inc. Cl A (TDUP) 3.58 17.38% • Gritstone bio Inc. (GRTS) 4.75 16.71% • Blue Apron Holdings Inc. (APRN) 5.38 16.20% • Weber Inc. Cl A (WEBR) 8.47 16.19% • Viridian Therapeutics Inc. (VRDN) 25.50 15.91% • Charge Enterprises Inc. (CRGE) 3.32 15.28% • Mainz Biomed B.V. (MYNZ) 10.64 15.15% • Fabrinet (FN) 115.75 14.93% • Big 5 Sporting Goods Corp. (BGFV) 15.44 14.46% • aTyr Pharma Inc. (LIFE) 4.15 14.01% • MoonLake Immunotherapeutics (MLTX) 8.10 13.60% • Hibbett Inc. (HIBB) 62.58 13.55% • Veru Inc. (VERU) 22.25 13.46% • System1 Inc. (SST) 10.53 13.35% • Nocera Inc. (NCRA) 2.30 13.30% • WM Technology Inc. (MAPS) 3.25 13.24% • Terns Pharmaceuticals Inc. (TERN) 4.98 13.18% • Hydrofarm Holdings Group Inc. (HYFM) 4.64 12.62% • American Resources Corp. (AREC) 2.58 12.17% • Nextdoor Holdings Inc. (KIND) 3.53 12.06% • FaZe Holdings Inc. (FAZE) 13.32 12.03% • Smart Powerr Corp. (CREG) 3.73 11.95% • Tattooed Chef Inc. (TTCF) 8.06 11.79% • Overstock.com Inc. (OSTK) 34.13 11.76% • Express Inc. (EXPR) 2.57 11.74% • Nutex Health Inc. (NUTX) 4.32 11.63% • Tarena International Inc. ADR (TEDU) 6.35 11.60% • SmartRent Inc. (SMRT) 3.66 11.59% • Zevia PBC (ZVIA) 4.69 11.40% • GasLog Partners LP (GLOP) 6.17 11.17% • Capstone Green Energy Corp. (CGRN) 3.85 10.95% • Biomea Fusion Inc. (BMEA) 13.61 10.92% • Sonder Holdings Inc. (SOND) 2.55 10.87% • Tempest Therapeutics Inc. (TPST) 2.76 10.84% • Barnes & Noble Education Inc. (BNED) 3.17 10.84% • Berkshire Grey Inc. (BGRY) 2.78 10.76% • Amtech Systems Inc. (ASYS) 10.11 10.73% • Children's Place Inc. (PLCE) 54.95 10.05% • Centessa Pharmaceuticals PLC ADR (CNTA) 4.28 10.03% • Inter & Co. Inc. (INTR) 3.84 9.71% • Upstart Holdings Inc. (UPST) 36.28 9.67% • FlexShopper Inc. (FPAY) 2.52 9.57% • Big Lots Inc. (BIG) 27.31 9.55% • Membership Collective Group Inc. (MCG) 8.17 9.52% • NextDecade Corp. (NEXT) 8.41 9.51% • a.k.a. Brands Holding Corp. (AKA) 2.55 9.44% • V2X Inc. (VVX) 40.09 9.27% • AST SpaceMobile Inc. (ASTS) 13.93 9.25% • Oncology Institute Inc. (TOI) 6.76 9.21% • Reneo Pharmaceuticals Inc. (RPHM) 3.12 9.09% • Abercrombie & Fitch Co. (ANF) 21.58 9.04% • Sotherly Hotels Inc. (SOHO) 2.71 8.84% • Tile Shop Holdings Inc. (TTSH) 4.32 8.82% • Veritone Inc. (VERI) 8.03 8.66% • Flexible Solutions International Inc. (FSI) 2.68 8.50% • Local Bounti Corp. (LOCL) 3.83 8.50% • AppHarvest Inc. (APPH) 3.45 8.49% • Rigetti Computing Inc. (RGTI) 5.39 8.45% • PetVivo Holdings Inc. (PETV) 2.52 8.39% • Zymergen Inc. (ZY) 3.37 8.36% • Wilhelmina International Inc. (WHLM) 5.23 8.32% • Koss Corp. (KOSS) 10.15 8.21% • Solo Brands Inc. (DTC) 5.67 8.21% • Grove Collaborative Holdings Inc. (GROV) 5.83 8.16% • Calithera Biosciences Inc. (CALA) 4.47 8.10% • Torrid Holdings Inc. (CURV) 7.75 8.09% • Innovid Corp. (CTV) 3.63 8.04% • Conn's Inc. (CONN) 12.51 8.03% • Lands' End Inc. (LE) 17.92 8.02% • Markforged Holding Corp. (MKFG) 3.14 7.90% • Purple Innovation Inc. (PRPL) 4.15 7.79% • Zumiez Inc. (ZUMZ) 30.75 7.78% • CalAmp Corp. (CAMP) 6.25 7.76% • Youdao Inc. ADR (DAO) 5.30 7.72% • LSI Industries Inc. (LYTS) 7.02 7.67% • Toast Inc. (TOST) 20.64 7.67% • Potbelly Corp. (PBPB) 6.46 7.67% • Nordstrom Inc. (JWN) 26.82 7.62% • Wayfair Inc. Cl A (W) 73.54 7.61%",
                        "decliners": "Rubicon Technologies Inc. (RBT) 6.00 -38.84% • Save Foods Inc. (SVFD) 2.92 -38.66% • Hallmark Financial Services Inc. (HALL) 1.58 -36.75% • Sema4 Holdings Corp. (SMFR) 1.60 -33.33% • Sunlight Financial Holdings Inc. (SUNL) 3.21 -27.87% • Albireo Pharma Inc. (ALBO) 18.08 -27.48% • Charah Solutions Inc. (CHRA) 3.34 -26.75% • Sunrise New Energy Co. Ltd. (EPOW) 2.49 -26.33% • Liberty TripAdvisor Holdings Inc. Series B (LTRPB) 42.00 -25.37% • AEye Inc. (LIDR) 2.24 -24.07% • Tremor International Ltd. ADR (TRMR) 8.06 -22.57% • Magic Empire Global Ltd. (MEGL) 14.01 -20.98% • Icosavax Inc. (ICVX) 7.28 -20.96% • Virios Therapeutics Inc. (VIRI) 6.71 -19.93% • CASI Pharmaceuticals Inc. (CASI) 3.24 -19.40% • GAN Ltd. (GAN) 3.50 -19.35% • Greenidge Generation Holdings Inc. (GREE) 3.76 -19.14% • SilverSun Technologies Inc. (SSNT) 3.10 -17.11% • urban-gro Inc. (UGRO) 5.21 -17.04% • Faraday Future Intelligent Electric Inc. (FFIE) 2.32 -16.85% • iSun Inc. (ISUN) 4.11 -15.95% • Wag! Group Co. (PET) 5.68 -15.46% • Lucira Health Inc. (LHDX) 2.83 -15.27% • Eos Energy Enterprises Inc. (EOSE) 1.96 -15.15% • WeTrade Group Inc. (WETG) 8.49 -15.10% • Amplitech Group Inc. (AMPG) 2.37 -14.93% • Sea Ltd. ADR (SE) 77.43 -13.94% • Scholar Rock Holding Corp. (SRRK) 9.72 -13.91% • Iridex Corp. (IRIX) 2.88 -13.25% • DarioHealth Corp. (DRIO) 5.86 -13.06% • InVivo Therapeutics Holdings Corp. (NVIV) 8.36 -12.92% • Aerovate Therapeutics Inc. (AVTE) 22.26 -12.84% • PAVmed Inc. (PAVM) 1.98 -12.78% • Allot Ltd. (ALLT) 4.66 -12.73% • Retractable Technologies Inc. (RVP) 3.74 -12.21% • AMMO Inc. (POWW) 4.76 -11.94% • QualTek Services Inc. (QTEK) 1.93 -11.87% • TOP Financial Group Ltd. (TOP) 11.66 -11.87% • Immersion Corp. (IMMR) 5.32 -11.84% • GeoVax Labs Inc. (GOVX) 2.25 -11.76% • Bloom Energy Corp. (BE) 26.80 -11.73% • CEL-SCI Corp. (CVM) 4.62 -11.66% • Stronghold Digital Mining Inc. (SDIG) 3.19 -11.63% • Eton Pharmaceuticals Inc. (ETON) 2.37 -11.57% • Sunnova Energy International Inc. (NOVA) 26.34 -11.55% • Liquidia Corp. (LQDA) 7.45 -11.20% • Outbrain Inc. (OB) 5.32 -11.19% • Invitae Corp. (NVTA) 4.45 -11.18% • TELA Bio Inc. (TELA) 8.13 -11.15% • Berkeley Lights Inc. (BLI) 4.64 -11.11% • BuzzFeed Inc. (BZFD) 1.93 -11.06% • LianBio ADR (LIAN) 2.66 -11.04% • Kymera Therapeutics Inc. (KYMR) 30.09 -10.82% • Pioneer Power Solutions Inc. (PPSI) 3.56 -10.66% • CVD Equipment Corp. (CVV) 5.29 -10.49% • MAIA Biotechnology Inc. (MAIA) 4.42 -10.49% • Zenvia Inc. Cl A (ZENV) 2.31 -10.47% • Personalis Inc. (PSNL) 4.77 -10.34% • Transphorm Inc. (TGAN) 5.13 -10.31% • Biodesix Inc. (BDSX) 2.38 -10.19% • TPI Composites Inc. (TPIC) 20.13 -10.13% • NanoViricides Inc. (NNVC) 2.58 -10.10% • Argo Group International Holdings Ltd. (ARGO) 20.37 -9.95% • Hallador Energy Co. (HNRG) 6.46 -9.71% • Talaris Therapeutics Inc. (TALS) 4.38 -9.69% • Akoya Biosciences Inc. (AKYA) 13.99 -9.68% • Beam Therapeutics Inc. (BEAM) 63.56 -9.60% • MyMD Pharmaceuticals Inc. (MYMD) 3.92 -9.26% • Macrogenics Inc. (MGNX) 4.51 -9.26% • Atreca Inc. Cl A (BCEL) 2.49 -9.12% • Design Therapeutics Inc. (DSGN) 23.27 -8.99% • Achieve Life Sciences Inc. (ACHV) 5.14 -8.87% • Generation Bio Inc. (GBIO) 7.22 -8.84% • Dynavax Technologies Corp. (DVAX) 14.24 -8.83% • Surgalign Holdings Inc. (SRGA) 4.47 -8.78% • Fate Therapeutics Inc. (FATE) 32.90 -8.76% • Adicet Bio Inc. (ACET) 14.01 -8.67% • 89bio Inc. (ETNB) 4.33 -8.65% • CI&T Inc. (CINT) 13.68 -8.62% • Arcimoto Inc. (FUV) 2.79 -8.52% • AeroClean Technologies Inc. (AERC) 4.34 -8.44% • Praxis Precision Medicines Inc. (PRAX) 4.27 -8.37% • Sorrento Therapeutics Inc. (SRNE) 2.52 -8.36% • Beyond Air Inc. (XAIR) 10.44 -8.34% • PMV Pharmaceuticals Inc. (PMVP) 15.53 -8.32% • Cardiff Oncology Inc. (CRDF) 2.77 -8.28% • Bitfarms Ltd. (BITF) 2.00 -8.26% • Rain Therapeutics Inc. (RAIN) 7.16 -8.21% • Azure Power Global Ltd. (AZRE) 11.25 -8.16% • IHS Holding Ltd. (IHS) 7.80 -8.13% • RVL Pharmaceuticals PLC (RVLP) 1.94 -8.06% • Precigen Inc. (PGEN) 2.41 -8.02% • CuriosityStream Inc. (CURI) 2.14 -7.76% • EverQuote Inc. Cl A (EVER) 9.77 -7.74% • Virax Biolabs Group Ltd. (VRAX) 6.71 -7.70% • Alignment Healthcare Inc. (ALHC) 15.13 -7.69% • Pineapple Energy Inc. (PEGY) 3.73 -7.67% • Greenwave Technology Solutions Inc. (GWAV) 3.41 -7.59% • Hive Blockchain Technologies Ltd. (HIVE) 6.73 -7.55% • Seer Inc. Cl A (SEER) 10.91 -7.54%",
                        "movers": "Bed Bath & Beyond Inc. (BBBY) 20.65 29.06% • fuboTV Inc. (FUBO) 6.35 44.98% • Nu Holdings Ltd. Cl A (NU) 5.52 17.95% • AMTD IDEA Group ADR (AMTD) 2.81 24.34% • Ginkgo Bioworks Holdings Inc. (DNA) 3.74 7.16% • AMC Entertainment Holdings Inc. Cl A (AMC) 24.81 2.48% • Snap Inc. (SNAP) 12.61 3.02% • Advanced Micro Devices Inc. (AMD) 100.20 -0.80% • Carnival Corp. (CCL) 11.19 4.48% • Amazon.com Inc. (AMZN) 144.78 1.12% • SoFi Technologies Inc. (SOFI) 7.58 -0.52% • Apple Inc. (AAPL) 173.03 -0.09% • Ford Motor Co. (F) 16.43 0.67% • NVIDIA Corp. (NVDA) 188.79 -0.80% • Tilray Brands Inc. Cl 2 (TLRY) 4.20 -2.10% • Palantir Technologies Inc. (PLTR) 9.74 -1.72% • Forza X1 Inc. (FRZA) 8.25 36.14% • AT&T Inc. (T) 18.57 0.98% • Warner Bros. Discovery Inc. Series A (WBD) 13.69 4.34% • Itau Unibanco Holding S/A ADR (ITUB) 5.25 0.00% • Blue Apron Holdings Inc. (APRN) 5.38 16.20% • NIO Inc. ADR (NIO) 20.91 -1.83% • Bank of America Corp. (BAC) 36.64 1.08% • Invitae Corp. (NVTA) 4.45 -11.18% • Shopify Inc. Cl A (SHOP) 39.58 -0.65% • Walmart Inc. (WMT) 139.37 5.11% • Tesla Inc. (TSLA) 919.69 -0.89% • Uber Technologies Inc. (UBER) 32.38 -0.34% • Southwestern Energy Co. (SWN) 7.50 3.59% • Magic Empire Global Ltd. (MEGL) 14.01 -20.98% • Roblox Corp. (RBLX) 47.76 -2.45% • Sea Ltd. ADR (SE) 77.43 -13.94% • Intel Corp. (INTC) 36.19 -0.41% • Vale S.A. ADR (VALE) 13.58 1.27% • American Airlines Group Inc. (AAL) 15.50 1.11% • GameStop Corp. Cl A (GME) 42.19 6.33% • Faraday Future Intelligent Electric Inc. (FFIE) 2.32 -16.85% • Annaly Capital Management Inc. (NLY) 6.79 0.00% • SmileDirectClub Inc. (SDC) 1.99 -6.57% • Ambev S.A. ADR (ABEV) 2.97 -1.00% • Plug Power Inc. (PLUG) 29.19 -2.57% • Nokia Corp. ADR (NOK) 5.17 1.17% • Kirkland's Inc. (KIRK) 5.29 31.92% • DraftKings Inc. (DKNG) 20.66 -0.67% • Petroleo Brasileiro S/A ADR (PBR) 13.73 0.37% • IonQ Inc. (IONQ) 8.38 31.76% • Cisco Systems Inc. (CSCO) 46.77 0.39% • Meta Platforms Inc. (META) 179.47 -0.79% • Gerdau S/A ADR (GGB) 4.77 -3.88% • Tencent Music Entertainment Group ADR (TME) 4.79 2.57% • Robinhood Markets Inc. (HOOD) 10.90 -1.00% • Riot Blockchain Inc. (RIOT) 9.17 -6.05% • Alphabet Inc. Cl A (GOOGL) 121.70 -0.31% • Canopy Growth Corp. (CGC) 3.78 -1.05% • Norwegian Cruise Line Holdings Ltd. (NCLH) 14.56 2.82% • Veru Inc. (VERU) 22.25 13.46% • Barrick Gold Corp. (GOLD) 16.85 1.08% • Microsoft Corp. (MSFT) 292.71 -0.26% • Comcast Corp. Cl A (CMCSA) 40.36 -0.52% • Banco Bradesco S/A Pref ADR (BBD) 3.80 -0.26% • Fisker Inc. (FSR) 9.25 -0.11% • Rivian Automotive Inc. Cl A (RIVN) 38.23 2.55% • Marathon Digital Holdings Inc. (MARA) 16.88 -4.36% • Coinbase Global Inc. (COIN) 90.39 -1.72% • Macy's Inc. (M) 21.11 5.76% • Occidental Petroleum Corp. (OXY) 63.51 -1.29% • Revlon Inc. Cl A (REV) 8.49 -0.93% • Opendoor Technologies Inc. (OPEN) 5.68 -5.49% • GEO Group Inc. (GEO) 7.89 3.82% • Artelo Biosciences Inc. (ARTL) 6.36 45.87% • Alphabet Inc. Cl C (GOOG) 122.51 -0.30% • Petroleo Brasileiro S/A ADR A (PBR.A) 12.44 -0.24% • Upstart Holdings Inc. (UPST) 36.28 9.67% • ironSource Ltd. (IS) 4.45 0.00% • Peloton Interactive Inc. (PTON) 13.69 1.18% • Marqeta Inc. (MQ) 8.20 -4.32% • FuelCell Energy Inc. (FCEL) 4.92 -4.84% • Hut 8 Mining Corp. (HUT) 3.33 -6.46% • Citigroup Inc. (C) 54.18 0.20% • Walt Disney Co. (DIS) 124.96 0.56% • PayPal Holdings Inc. (PYPL) 102.08 0.56% • Verizon Communications Inc. (VZ) 45.80 0.53% • Exxon Mobil Corp. (XOM) 91.46 -0.93% • General Motors Co. (GM) 38.99 -1.04% • Grab Holdings Ltd. (GRAB) 3.66 -2.92% • Energy Transfer LP (ET) 11.80 1.90% • GoodRx Holdings Inc. (GDRX) 7.31 1.39% • Marathon Oil Corp. (MRO) 23.05 -1.12% • Pinterest Inc. (PINS) 22.99 -1.67% • JetBlue Airways Corp. (JBLU) 9.05 -1.31% • Lucid Group Inc. (LCID) 18.93 0.91% • XPeng Inc. ADR (XPEV) 22.91 -2.51% • Pfizer Inc. (PFE) 49.86 0.22% • Sirius XM Holdings Inc. (SIRI) 6.60 -2.51% • Teva Pharmaceutical Industries Ltd. ADR (TEVA) 11.03 -1.52% • CSX Corp. (CSX) 34.44 0.88% • Nikola Corp. (NKLA) 6.90 2.68% • Affirm Holdings Inc. Cl A (AFRM) 39.91 3.88% • Carvana Co. Cl A (CVNA) 54.59 7.04% • Amcor PLC (AMCR) 13.29 2.00%",
                    },
                ]
            ]
            print(responseArr)
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            print(offscreen_canvas)
            pos = offscreen_canvas.width
            color = green
            print(responseArr)
            for arr in responseArr:
                running = True
                print("-------------------------------")
                print(arr)
                print("-------------------------------")
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
                                        green,
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
                                        green,
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
                                        green,
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
                                        + awayTeam
                                        + awayTeamStatus,
                                        26,
                                        green,
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
                                        green,
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
                                        green,
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
                                        green,
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
                                        + homeTeam
                                        + homeTeamStatus,
                                        26,
                                        green,
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
                                    green,
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
                                    green,
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
                        time.sleep(0.01)
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
                                # awayOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 12, green, awayOddsString)
                                # homeOdds = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer+ buffer + buffer + buffer + homeTeam + buffer, 26, green, homeOddsString)
                                # overUnderStr = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer+ buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + homeTeam, 12, green, 'O/U')
                                # overUnderAmount = graphics.DrawText(offscreen_canvas, smallFont, pos + offset + teamLogos[game[5]].width + versus + teamLogos[game[10]].width + buffer + buffer + buffer + buffer + buffer+ buffer + buffer + buffer+ buffer + buffer + buffer + buffer+ buffer + buffer+ homeTeam, 26, green, overUnderString)
                            if "inProgress" in game[0]:
                                awayTeamString = game[5]
                                homeTeamString = game[10]
                                awayTeamStatusString = game[12]
                                homeTeamStatusString = game[13]
                                situationString = game[15]
                                statusString = game[16]
                                possession = game[17]
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
                                    green,
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
                                    green,
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
                        time.sleep(0.01)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "ncaa" in arr[0][0]:
                        for game in arr:
                            if "conference" in game[0]:
                                conferenceName = graphics.DrawText(
                                    offscreen_canvas,
                                    font,
                                    pos + offset,
                                    24,
                                    green,
                                    game[1],
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
                                overUnderText = ""
                                if overUnderString != "":
                                    overUnderText = "O/U"
                                awayTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    12,
                                    white,
                                    awayTeamString,
                                )
                                homeTeam = graphics.DrawText(
                                    offscreen_canvas,
                                    smallFont,
                                    pos + offset + buffer + buffer + buffer,
                                    26,
                                    white,
                                    homeTeamString,
                                )
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
                                    + homeTeam
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
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam
                                    + buffer,
                                    26,
                                    green,
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
                                    + homeTeam,
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
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + buffer
                                    + homeTeam,
                                    26,
                                    green,
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
                                    green,
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
                                    green,
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
                        time.sleep(0.01)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "stocks" in arr[0]:
                        for game in arr[1]:
                            awayTeam = 0
                            homeTeam = 0
                            headlineString = 0
                            awayTeamStatus = 0
                            homeTeamStatus = 0
                            if "up" in game[5]:
                                color = green
                            if "down" in game[5]:
                                color = red
                            logo = game[0]
                            stockStr = game[4]
                            # offscreen_canvas.SetImage(logo, pos + offset, -10)
                            string = graphics.DrawText(
                                offscreen_canvas,
                                font,
                                pos + offset + buffer,
                                24,
                                color,
                                stockStr,
                            )
                            offset = offset + string + 80
                        time.sleep(0.015)
                        if pos + offset < 0:
                            running = False
                            pos = offscreen_canvas.width
                    elif isinstance(arr, list) and "gainersDecliners" in arr[0]:
                        gainers = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 11, green, arr[1]["gainers"]
                        )
                        time.sleep(0.010)
                        decliners = graphics.DrawText(
                            offscreen_canvas, bFont, pos, 27, red, arr[1]["decliners"]
                        )
                        time.sleep(0.005)
                        pos -= 1
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
                        time.sleep(0.020)
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
                        if pos + com < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.020)
                    elif isinstance(arr, list) and (
                        arr[0] == "golf" or "rankings" in arr[0]
                    ):
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
                            offscreen_canvas, bFont, pos, 20, green, arr
                        )
                        pos -= 1
                        if pos + length < 0:
                            running = False
                            pos = offscreen_canvas.width
                        time.sleep(0.03)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
