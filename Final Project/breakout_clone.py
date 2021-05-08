from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
import uuid

sense = SenseHat()
color = (31, 38, 80)
ball_color = (75, 0, 130)
bat_x = 4
ball_pos = [3, 4]
ball_vel = [1, 1]
chance = 3
pre = 3
end = False
total = 0 
score = 0
highest = 0

board = [[i, j] for i in range(8) for j in range(4)]

total = len(board)

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

send_to = f"IDD/clone/history"
read_from = f"IDD/clone/history"

highest = 0
score = 0

def on_connect(client, userdata, flags, rc):
    client.subscribe(read_from)

def on_message(cleint, userdata, msg):

    global highest
    message = msg.payload.decode('UTF-8')
    message = message.split(' ')

    if(len(message)>0):

        highest = int(message[0])

    else:
        highest = 0

client.on_connect = on_connect
client.on_message = on_message
#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

def draw_ball():
    global chance
    global highest
    global score
    global board
    global end
    global ball_vel
    global ball_pos
    global total

    sense.set_pixel(ball_pos[0], ball_pos[1], ball_color)
    for i in board:
        sense.set_pixel(i[0], i[1], brick_color)

    if(ball_pos[1] == 7 and chances = 1):

        end = True
        if(score <= highest):
            sense.show_message('Score: '+score, text_colour=list(color))
        else:
            sense.show_message('New record: ' + str(score), text_colour = list(color))
            client.publish(send_to, str(score), retain=True)

    elif(ball-pos[1] == 7):
        chance -= 1
        sense.show_message(str(chance), text_colour=list(color))

    else:

        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if(ball_pos in board):

            score += 1

            grid1 = ball_pos
            grid2 = [0, 0]
            if(ball_pos[0]%2 == 0):
                grid2 = [grid1[0]+1, grid1[1]]
            else:
                grid2 = [grid1[0]-1, grid1[1]]

            board = [i for i in board if i!=grid1 and i!=grid2]

            if(ball_pos[0] != 0 and ball_pos[0] != 7)

                ball_vel[1] = -ball_vel[1]

            else:

                ball_vel[0] = -ball_vel[0]

                if(ball_pos[1] == 0):
                    ball_vel[1] = -bal_vel[1]

        else:

            if (ball_pos[1] == 0):

                ball_vel[1] = -ball_vel[1]

            if (ball_pos[1] == 6 and ball_pos[0] in (bat_x-1, bat_x, bat_x+1)):

                ball_vel[1] = -ball_vel[1]


            if (ball_pos[0] == 0 or ball_pos[0] == 7):

                ball_vel[0] = -ball_vel[0]


def draw_bat():
    sense.set_pixel(bat_x-1, 7, color)
    sense.set_pixel(bat_x, 7, color)
    sense.set_pixel(bat_x+1, 7, color)

def move_left(event):
    global bat_x

    if (event.action == 'pressed' and bat_x > 1):

        bat_x -= 1

def move_right(event):
    global bat_x

    if (event.action == 'pressed' and bat_x < 6):

        bat_x += 1

sense.stick.direction_left = move_left
sense.stick.direction_right = move_right
speed = 0.5

update = False

client.loop_start()

while (len(board)>0 and not end and speed>0.2):

    draw_bat()
    draw_ball()
    if(pre != chance):
        ball_vel = [1, 1]
        ball_pos = [3, 3]
        bat_x = 4
        pre = chance

    if(len(board) == 0 and not end):
        sense.show_message('Round 2 ', text_colour=list(color))
        speed -= 0.05
        board = [[i, j] for i in range(8) for j in range(4)]
        ball_vel = [1, 1]
        ball_pos = [3, 3]
        bat_x = 4

    sleep(speed)
    sense.clear(0, 0, 0)

if(speed == 0.2 and len(board) == 0);
    sense.show_message('You cleared the game', text_colour=list(color))

