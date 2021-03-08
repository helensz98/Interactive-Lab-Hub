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

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()

backlight.value = True

vanilla = 0
chocolate = 0
strawberry = 0
add = False
which = 0
switch = 0
s = False
c = False
v = False

while True:

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    if (buttonA.value and buttonB.value and not add): #no button pressed
        #Part E starts
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        sem_end = datetime.strptime('05 25 2021  23:59', '%m %d %Y %H:%M')
        current_time = datetime.now()
        remaining_time = sem_end-current_time 
        remaining_days = remaining_time.total_seconds()//86400 - strawberry-2*chocolate-3*vanilla
        if int(remaining_days) < 0:
            remaining_days = 0
        
        line_1 = "Eat away your time!"
        line_2 = "You've ate "+str(strawberry)+" straberry"
        line_3 = "You've ate "+str(chocolate)+" chocolate"
        line_4 = "You've ate "+str(vanilla)+" vanilla"
        line_5 = "You are "+ str(remaining_days) +" days away \n from the summer!"
        line_6 = "\n Press buttonA to view and \n buttonB to buy ice creams :)"
        y = top
        draw.text((x, y), line_1, font=font, fill="#FFFFFF")
        y += font.getsize(line_1)[1]
        draw.text((x, y), line_2, font=font, fill="#FFFFFF")
        y += font.getsize(line_2)[1]
        draw.text((x, y), line_3, font=font, fill="#FFFFFF")
        y += font.getsize(line_3)[1]
        draw.text((x, y), line_4, font=font, fill="#FFFFFF")
        y += font.getsize(line_4)[1]
        draw.text((x, y), line_5, font=font, fill="#FFFFFF")
        y += font.getsize(line_5)[1]
        draw.text((x, y), line_6, font=font, fill="#FFFFFF")
        disp.image(image, rotation)
    elif(not buttonA.value and not add): #buttonA pressed
        which = 0
        add = True

    elif(buttonB.value and add): 

        if(not buttonA.value and switch == 0 and s):
            which = 1
            switch += 1

        elif(not buttonA.value and switch == 0 and c):
            which = 2
            switch += 1

        elif(not buttonA.value and switch == 0 and v):
            which = 0
            switch += 1

        if(buttonA.value and which == 0):
            s = True
            c = False
            v = False
            switch = 0
            image = Image.open("strawberry.jpg")
            image = image.convert('RGB')
            image = image.resize((width, height), Image.BICUBIC)
            draw = ImageDraw.Draw(image)
            draw.rectangle((5, 10, width, 40), fill='white')
            draw.text((5, 10), 'one strawberry costs 1 day', font=font, fill="#000000")
            
        elif(buttonA.value and which == 1):
            s = False
            c = True
            v = False
            switch = 0
            image = Image.open("chocolate.jpg")
            image = image.convert('RGB')
            image = image.resize((width, height), Image.BICUBIC)
            draw = ImageDraw.Draw(image)
            draw.rectangle((5, 10, width, 40), fill='white')
            draw.text((5, 10), 'one chocolate costs 2 days', font=font, fill="#000000")
            
        elif(buttonA.value and which == 2):
            s = False
            c = False
            v = True
            switch = 0
            image = Image.open("vanilla.jpg")
            image = image.convert('RGB')
            image = image.resize((width, height), Image.BICUBIC)
            draw = ImageDraw.Draw(image)
            draw.rectangle((5, 10, width, 40), fill='white')
            draw.text((5, 10), 'one vanilla costs 3 days', font=font, fill="#000000")
            
            
        disp.image(image, rotation)

    if(not buttonB.value and add): #finalize add
        add = False
        if(s):
            strawberry += 1
        elif(c):
            chocolate += 1
        elif(v):
            vanilla += 1
        s = False
        c = False
        v = False
