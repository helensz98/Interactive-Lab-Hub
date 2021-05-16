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

Code breakdown:

<MQTT>
 
Use MQTT to send/load past highest record. By sending and subscribing to the same topic, users and read and load previous data. Normally, MQTT only allow subsribers to receive real time messages. However, by setting the retain flag as True (client.publish(, ..., retain = True)), users can loop_start once in the beginning of the program and get the previous message. 



## Deliverables

1. Documentation of design process
2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)
4. Reflections on process (What have you learned or wish you knew at the start?)


## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
