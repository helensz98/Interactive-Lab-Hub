import paho.mqtt.client as mqtt
import uuid
from sense_hat import SenseHat
from time import sleep


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

send_to = f"IDD/pong/history"
read_from = f"IDD/pong/history"

highest = 0
score = 0

def on_connect(client, userdata, flags, rc):
    client.subscribe(read_from)

def on_message(cleint, userdata, msg):
    global highest
    message = msg.payload.decode('UTF-8')
    print(message)
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

sense = SenseHat()
color = (31, 38, 80)
ball_color = (75, 0, 130)
bat_x = 4
ball_pos = [3, 3]
ball_vel = [1, 1]
chance = 3
pre = 3
bounce = 0

sense.show_message('3', text_colour=list(color))

def draw_ball():
    global chance
    global bounce
    global update
    global highest
    global score

    sense.set_pixel(ball_pos[0], ball_pos[1], ball_color)

    if(ball_pos[1] == 7):

        chance -= 1
        score = max(bounce, score)

        if(chance>0):

            sense.show_message(str(chance), text_colour=list(color))

        else:

            if(score <= highest):

                sense.show_message('Score: '+str(score), text_colour=list(color))

            else:

                sense.show_message('New record: ' + str(score), text_colour = list(color))
                client.publish(send_to, str(score), retain=True)

    if (chance > 0):

        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if (ball_pos[1] == 0):

            ball_vel[1] = -ball_vel[1]

        if (ball_pos[1] == 6 and ball_pos[0] in (bat_x-1, bat_x, bat_x+1)):

            bounce += 1
            ball_vel[1] = -ball_vel[1]

            if(bounce%5 == 0):

                update = True

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

client.loop()

while (chance>0 and speed >0.05):

    draw_bat()
    draw_ball()

    if(pre > chance):

        pre = chance
        ball_pos = [3, 3]
        ball_vel = [1, 1]
        bat_x = 4
        speed = 0.5
        bounce = 0

    if(update):

        speed -= 0.05
        update = False

    sleep(speed)
    sense.clear(0, 0, 0)

if(speed == 0.05):
    sense.show_message('You cleared the game', text_colour=list(color))




