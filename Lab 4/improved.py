import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_mpr121
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
spi = board.SPI()

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

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

theBoard = {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }

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

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

def printBoard(board, turn, state):
	image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    l1 = ' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9])
    l2 = '-------------'
    l3 = ' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6])
    l4 = '-------------'
    l5 = ' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3])
    l6 = ''
    if (state == 0):
    	l6 = "It's your turn, "+turn+"."
    elif (state == 1):
    	l6 = "That palce has been filled."
    elif (state == 2):
    	l6 = turn+" won. Press 1 to restart. "
    else:
    	l6 = "Game over. It's a tie"
    y = top
    draw.text((x, y), l1, font=font, fill="#FFFFFF")
    y += font.getsize(l1)[1]
    draw.text((x, y), l2, font=font, fill="#FFFFFF")
    y += font.getsize(l2)[1]
    draw.text((x, y), l3, font=font, fill="#FFFFFF")
    y += font.getsize(l3)[1]
    draw.text((x, y), l4, font=font, fill="#FFFFFF")
    y += font.getsize(l4)[1]
    draw.text((x, y), l5, font=font, fill="#FFFFFF")
    y += font.getsize(l5)[1]
    draw.text((x, y), l6, font=font, fill="#FFFFFF")
	disp.image(image, rotation)

count = 0
state = 0
turn = 'X'
end = False


while True:

    move = 0

    if (not end):

	    for i in range(1, 10):
	    	if(mpr121[i].value):
	    		move = i
	    		break

	    if(move != 0):

		    if (theBoard[move] == ' '):
		        theBoard[move] = turn
		        count += 1
		        state = 0
		    else:
# 		    	state = 1
		    	move = 0

	    if count >= 5 and move != 0:

	        if (theBoard[7] == theBoard[8] == theBoard[9] != ' '):
	            state = 2
	            end = True              
	         
	        elif (theBoard[4] == theBoard[5] == theBoard[6] != ' '):
	            state = 2
	            end = True
	     
	        elif (theBoard[1] == theBoard[2] == theBoard[3] != ' '):
	            state = 2
	            end = True
	 
	        elif (theBoard[1] == theBoard[4] == theBoard[7] != ' '):
	            state = 2

	        elif (theBoard[2] == theBoard[5] == theBoard[8] != ' '):
	            state = 2
	            end = True

	        elif (theBoard[3] == theBoard[6] == theBoard[9] != ' '):
	            state = 2
	            end = True

	        elif (theBoard[7] == theBoard[5] == theBoard[3] != ' '):
	            state = 2
	            end = True

	        elif (theBoard[1] == theBoard[5] == theBoard[9] != ' '):
	            state = 2
	            end = True

    if (count == 9 and not end):
    	state = 3

    if (move != 0 and not end):
	    if turn =='X':
	        turn = 'O'
	    else:
	        turn = 'X'  

    if (end):
	if(mpr121[1].value):
	    end = False
	    count = 0
	    state = 0
	    turn = 'X'
	    for i in range(1, 10):
	        theBoard[i] = ' '
	
    printBoard(theBoard, turn, state)      
    

