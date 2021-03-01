import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
#import adafruit_rgb_display.st7789 as st7789

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

if disp.rotation % 180 == 90:
    height2 = disp.width  # we swap height/width to rotate it to landsca$
    width2 = disp.height
else:
    width2 = disp.width  # we swap height/width to rotate it to landscap$
    height2 = disp.height
image2 = Image.new("RGB", (width2, height2))
draw2 = ImageDraw.Draw(image2)
draw2.rectangle((0, 0, width2, height2), outline=0, fill=(0, 0, 0))
image2 = Image.open("red.jpg")
image_ratio = image2.width / image2.height
screen_ratio = width2 / height2
#image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
if screen_ratio < image_ratio:
    scaled_width = image2.width * height2 // image2.height
    scaled_height = height2
else:
    scaled_width = width2
    scaled_height = image2.height * width2 // image2.width
image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
x = scaled_width // 2 - width2 // 2
y = scaled_height // 2 - height2 // 2
image2 = image2.crop((x, y, x + width2, y + height2))

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

while True:
    sem_end = datetime.strptime('05 25 2021  23:59', '%m %d %Y %H:%M')
    line_1 = "Spring term ends on\n " + str(sem_end)
    line_2 = "\n People typically take \n 12 min to eat an \n ice cream cone"
    current_time = datetime.now()
    while buttonA.value and buttonB.value:
        sem_end = datetime.strptime('05 25 2021  23:59', '%m %d %Y %H:%M')
        line_1 = "Spring term ends on\n " + str(sem_end)
        line_2 = "\n People typically take \n 12 min to eat an \n ice cream cone"
        current_time = datetime.now()
        remaining_time = sem_end - current_time
        num_ice_cream = remaining_time.total_seconds()/720
        line_3 = "\n\n\n You are "+str(num_ice_cream)+"\n cones away from the summer!"
        y = top
        draw.text((x, y), line_1, font=font, fill="#FFFFFF")
        y += font.getsize(line_1)[1]
        draw.text((x, y), line_2, font=font, fill="#FFFFFF")
        y += font.getsize(line_2)[1]
        draw.text((x, y), line_3, font=font, fill="#FFFFFF")
        # Display image.
        disp.image(image, rotation)
    switch = True
    while switch:
        disp.image(image2)
        if(buttonA.value):
            switch = False


        








    
    
    
    
    
















    
    
    
    
    
