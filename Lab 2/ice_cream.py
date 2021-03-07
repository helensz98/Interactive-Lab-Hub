import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
#import adafruit_rgb_display.st7789 as st7789
# saved in file test.py
# part E import starts
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331
from datetime import datetime, date, timedelta
# part E import ends


#add images vie
#scp /Users/helen/Downloads/vanilla.jpg pi@100.64.5.82:"Interactive-Lab-Hub/Lab\\ 2"

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# part E prep starts
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True 
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()

backlight.value = True

vanilla = 0
chocolate = 0
straberry = 0

while True:
    
    if (buttonA.value and buttonB.value): #no button pressed
        #Part E starts
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        line_1 = "Magical ice cream of time! "
        line_2 = "\n You've haved "+str(straberry)+" straberry"
        line_3 = "\n \n You've haved "+str(chocolate)+" chocolate"
        line_4 = "\n \n \n You've haved "+str(vanilla)+" vanilla"
        y = top
        draw.text((x, y), line_1, font=font, fill="#FFFFFF")
        y += font.getsize(line_1)[1]
        draw.text((x, y), line_2, font=font, fill="#FFFFFF")
        y += font.getsize(line_2)[1]
        draw.text((x, y), line_3, font=font, fill="#FFFFFF")
        y += font.getsize(line_3)[1]
        draw.text((x, y), line_4, font=font, fill="#FFFFFF")
        # disp.image(image, rotation)

    elif(buttonA.value): #buttonB pressed
        image = Image.open("red.jpg")
        image = image.convert('RGB')
        image = image.resize((width, height), Image.BICUBIC)
        #draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    disp.image(image, rotation)
        
#      Part E ends
