from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
import uuid
import random

sense = SenseHat()
color = (31, 38, 80)
ball_color = (75, 0, 130)
brick_color = (47, 79, 79)
bat_x = 4
ball_pos = [random.randrange(2, 6), 4]
ball_vel = [1, 1]
chance = 3
pre = 3
total = 0
end = False

x = 0
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

sense.show_message('You have 3 lives', text_colour=list(color))
board = [[i, j] for i in range(8) for j in range(4)]

total = len(board)

def draw_ball():
    global chance
    global highest
    global score
    global board
    global end
    global ball_vel

    global ball_pos
    global total

    ld = False
    rd = False
    lu = False
    ru = False
    
    sense.set_pixel(ball_pos[0], ball_pos[1], ball_color)
    for i in board:
        sense.set_pixel(i[0], i[1], brick_color)
        
    # if lives are used up and ball hits the ground
    if(ball_pos[1] == 7 and chance == 1):
        end = True
        sleep(0.25)
        #compare with the stored highest
        # score is the number of bricks cleared
        if(score <= highest):
            sense.show_message('Score: '+str(score), text_colour=list(color))
        else:
            sense.show_message('New record: ' + str(score), text_colour = list(color))
            client.publish(send_to, str(score), retain=True)
    #still have lives? go on then
    elif(ball_pos[1] == 7):
        chance -= 1
        sleep(0.25)
        sense.show_message(str(chance), text_colour=list(color))

    else:
        # predict future
        # check where the next step is before moving
        pos = [0, 0]
        pos[0] = ball_pos[0]
        pos[1] = ball_pos[1]

        pos[0] += ball_vel[0]
        pos[1] += ball_vel[1]

        # bounce
        # when it's going to hit corners 
        if(pos == [0, 0] and not pos in board):
            ball_pos = pos
            ball_vel = [1, 1]
        elif(pos == [7, 0] and not pos in board):
            ball_pos = pos
            ball_vel = [-1, 1]
        # when it's stuck between a brick and ceilling
        elif(ball_vel == [-1, 1] and pos in board and ball_pos[1] == 0):
            ball_vel = [1, 1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
         # hit a brick a not stuck : update velocity according to current velocity
        elif(ball_vel == [-1, 1] and pos in board):
            l = [ball_pos[0]-1, ball_pos[1]]
            d = [ball_pos[0], ball_pos[1]+1]
            # should I remove 1 brick on the diagonal, or 2 bricks around the ball (if any)
            if((l in board and d in board)):
                ld = True
            ball_vel = [-1, -1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
        #stuck
        elif(ball_vel == [1, 1] and pos in board and ball_pos[1] == 0):
            ball_vel = [-1, 1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
         #same velocity but not stuck
        elif(ball_vel == [1, 1] and pos in board):
            r = [ball_pos[0]+1, ball_pos[1]]
            d = [ball_pos[0], ball_pos[1]+1]
            if((r in board and d in board)):
                rd = True
            ball_vel = [1, -1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
        # hit bricks with different velocities
        elif(ball_vel == [-1, -1] and pos in board):
            l = [ball_pos[0]-1, ball_pos[1]]
            u = [ball_pos[0], ball_pos[1]-1]
            if((l in board and u in board)):
                lu = True
            ball_vel = [-1, 1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
        elif(ball_vel == [1, -1] and pos in board):
            r = [ball_pos[0]+1, ball_pos[1]]
            u = [ball_pos[0], ball_pos[1]-1]
            if((r in board and u in board)):
                ru = True
            ball_vel = [1, 1]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
        elif(pos[1] == 0):
            # print('hit the ceiling')
            ball_vel[1] = -ball_vel[1]
            ball_pos = pos
        elif(pos[0] < 0 and pos[1] != 7):
            # print('hit the left wall')
            ball_vel[0] = - ball_vel[0]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1] 
        elif(pos[0] == 0 and pos[1] != 7):
            # print('hit the left wall')
            ball_vel[0] = - ball_vel[0]
            ball_pos = pos 
        elif(pos[0] > 7 and pos[1] != 7):
            # print('right wall')
            ball_vel[0] = - ball_vel[0]
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
        elif(pos[0] == 7 and pos[1] != 7):
            # print('hit the right wall')
            ball_vel[0] = - ball_vel[0]
            ball_pos = pos
        elif(pos[1] == 7 and ball_pos[0] in [bat_x-1, bat_x, bat_x+1]):
            # print('hit the bat')
            if(ball_pos[0] != 0 and ball_pos[0] != 7):
                ball_vel[1] = -ball_vel[1]
                ball_pos[0] += ball_vel[0]
                ball_pos[1] += ball_vel[1]
            elif(ball_pos[0] == 0):
                ball_vel = [1, -1]
                ball_pos[0] += ball_vel[0]
                ball_pos[1] += ball_vel[1]
            else:
                ball_vel = [-1, -1]
                ball_pos[0] += ball_vel[0]
                ball_pos[1] += ball_vel[1]
        else:
            #nothing will happend ok!
            ball_pos = pos
        # I have updated ball velocity. Now let's remove some bricks 
        if(pos in board):
            pre = [0, 0]
            pre[0] = (ball_pos[0] - ball_vel[0])
            pre[1] = (ball_pos[1] - ball_vel[1])
            if(ld): #meaning that there are two bricks on the left and right that close the way through which the ball reaches the intended position on the diagonal
                #clear these bricks instead
                # prine('left down')
                lgrid1 = [pre[0]-1, pre[1]]
                lgrid2 = [pre[0]-2, pre[1]]
                dgrid1 = [pre[0], pre[1]+1]
                dgrid2 = [pre[0]+1, pre[1]+1]
                board = [i for i in board if i!=lgrid1 and i!=lgrid2 and i!=dgrid1 and i!=dgrid2] 
            elif(rd):
                # print('right down')
                rgrid1 = [pre[0]+1, rpe[1]]
                rgrid2 = [pre[0]+2, pre[1]]
                dgrid1 = [pre[0], pre[1]+1]
                dgrid2 = [pre[0]+1, pre[1]+1]
                board = [i for i in board if i!=rgrid1 and i!=rgrid2 and i!=dgrid1 and i!=dgrid2]
            elif(lu):
                # print('left up')
                lgrid1 = [pre[0]-1, pre[1]]
                lgrid2 = [pre[0]-2, pre[1]]
                ugrid1 = [pre[0], pre[1]-1]
                ugrid2 = [pre[0]+1, pre[1]-1]
                board = [i for i in board if i!=lgrid1 and i!=lgrid2 and i!=ugrid1 and i!=ugrid2]
            elif(ru):
                # print('right up')
                rgrid1 = [rpe[0]+1, pre[1]]
                rgrid2 = [pre[0]+2, pre[1]]
                ugrid1 = [pre[0], pre[1]-1]
                ugrid2 = [pre[0]+1, pre[1]-1]
                board = [i for i in board if i!=rgrid1 and i!=rgrid2 and i!=ugrid1 and i!=ugrid2]
            else:
                score += 1
                grid1 = pos
                grid2 = [0, 0]
                #remember that two grids is one brick. The ball can only hit one part of the brick
                #but we should clear the brick as a whole. 
                if(pos[0]%2 == 0):
                    grid2 = [grid1[0]+1, grid1[1]]
                elif(pos[0]%2 == 1):
                    grid2 = [grid1[0]-1, grid1[1]]
                board = [i for i in board if i!=grid1 and i!=grid2] 


def draw_bat():
    sense.set_pixel(bat_x-1, 7, color)
    sense.set_pixel(bat_x, 7, color)
    sense.set_pixel(bat_x+1, 7, color)

def move_left(event):
    global bat_x
    global x

    if(x < 0):
        bat_x -= 1

def move_right(event):
    global bat_x
    global x

    if(x>0):
        bat_x += 1

sense.stick.direction_left = move_left
sense.stick.direction_right = move_right
speed = 0.5

update = False

client.loop_start()

while (len(board)>0 and not end and speed>0.2):

    acc = sense.get_accelerometer_raw()
    x = acc['x']
    if(x<0 and bat_x>1):
        bat_x -= 1
    elif(x>0 and bat_x <6):
        bat_x += 1
    draw_bat()
    draw_ball()
    if(pre != chance):
        ball_vel = [1, 1]
        ball_pos = [random.randrange(2, 6), 4]
        bat_x = 4
        pre = chance
    if(len(board) == 0 and not end):
        sense.show_message('Speed up!', text_colour=list(color))
        speed -= 0.05
        board = [[i, j] for i in range(8) for j in range(4)]
        ball_vel = [1, 1]
        ball_pos = [random.randrange(2, 6), 4]
        bat_x = 4

    sleep(speed)
    sense.clear(0, 0, 0)

if(speed == 0.2 and len(board)==0):
    sense.show_message('You cleared the game', text_colour=list(color))

