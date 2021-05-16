# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description

Wanna have some fun in the depth of finals? Distract yourself from the world of infinite due and insanity, let's play something simple and fun!

[breakout clone](https://youtu.be/ivUhyYDvSVo)

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/breakout_clone.jpg" height="300"> 

Game instruction: 

Green: bricks

Red: ball

Blue: bat

Players have three lives! They can use the bat to bounce the ball. When all bricks are cleared, players enter the next round. In each new round, the ball gains a higher velocity.

Players move the bat by changing the value on the x axis of the led matrix, namely shaking the sense hat. If the sense hat tilts to the left, the bat moves to the left, and vice versa. (a bit of wrist exercices too (੭ˊᵕˋ)੭）

Game is cleared when velocity reaches 0.2 and all bricks are removed. 

Requirements:

1. raspberry pi
2. Led matrix (I use Sense hat)
3. cardboxes, tapes, scissor and wrapping paper to custonm the device

## Design process:

----------MQTT------------
 
Use MQTT to send/load past highest record. By sending and subscribing to the same topic, users and read and load previous data. Normally, MQTT only allow subsribers to receive real time messages. However, by setting the retain flag as True (client.publish(, ..., retain = True)), users can loop_start once in the beginning of the program and get the previous message. 

-----------Bat-------------

The bat is a 3 by 3 sqaure positioned on the last row. Users move the bat by tilting the matrix. The accelerometer will detect change in x-axis and update the bat position according. 

-----------Ball------------

The ball is a 1 by 1 sqaure moving inside the matrix. It has either one of the four velocities(x row, y column): (-1, -1), (-1, 1), (1, -1), (1, 1)

The initial speed is 0.5 defined by sleep(0.5) in the while loop. Each time all bricks are cleared (len(board) = 0), a 0.05 decrement is given to the speed. 

The most troubling thing is to consider reasonable physics for the ball to bounce when hitting obstacle. In general, I want the ball to reverse y velocity when it hits an obstable from above, reverse its x velocity with an obstable on the left, etc. However, there are many edge cases to consider. 

![input settings](https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/setup.png?raw=true)

In case 1 where the ball hit one of the four corners from the blue vector, it should reverse both x and y velocities and follow the red vector. 

In cases 2 and case 3, the ball is stuck between the ceilling and the brick. It flies from the blue vector direction, hits the ceilling and reverse its y velocity. However, before it can move it's stoped by the brick on its diagonal, making it bounce back to the celling. One way to address this is to let it follow the red vector. 

Similarly, in case 4, the ball is stuck between the wall and the brick, and should follow the red vector to escape the delimma. 

In case 5, we consider which brick to break. Usually, the ball breaks any brick on the diagonal of its moving direction, which is brick k. However, it does not look like the ball can reach brick k at all: before doing that, it encounters h and j. Thus, it makes more sense to break h and j and reverse both x and y velocities. I use several boolean variables (up, ur, ll, lr) as well as ball velocity to check whther we should break 1 brick on the diagonal or 2 bricks on the side. 

Cases 6 and 7 show how the ball should behave without edge cases. 

In generally, I consider each possible situation and specify how the ball should move. There should be a better (more clever way) of doing this. Some cases are less likely to occur than others, but it's nice to include them. 


--------- Brick -----------

Bricks are laid out on the first four rows of the matrix (row 0 to 3, columns 0 to 7). They are stored as pairs of postion tuples in the list (var board). Each
 time the ball moves, it will check whether it's going to hit a brick one move after (if ball_position in board)
 
 Since the ball moves with specified velocity and dirctions, there are some bricks that the ball will never reaches if brick.size is 1 by 1. Therefore, I make each brick a 1 by 2 sqaure consisted of two position tuples. Each time the ball hit one part of the brick, the other part is found by modulo 2 operation and removed from the board (list) as well. 
 
-------- Wizarding ----------

I came back to my old good friend cardboxes because they are lightweight and easy to shape. I wanted to make a game controller! Hiding all part of the device and showing only the led screen was easy once I found an apporopriate box, attached the pi inside and showed the led screen through the window. As for the handle, I used toothpaste package and cut them in halves. 


Nest, I used tapes to attach the cardbox and packages. The final step is to do some make up so that the device looks less messy.





--------- Reflection ---------


4. Reflections on process (What have you learned or wish you knew at the start?)


## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
