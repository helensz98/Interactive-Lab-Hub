# broke the pi (talked to Professor Ju-my fault I'm so sorry...) I ordered a new one which will arrive tomorrow. I will upload what I have now and update the act like video tomorrow. 



# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Pull the new Github Repo.
2. Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes


### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. 

Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

### Part A
### Capacitive Sensing, a.k.a. Human Banana Interaction

I connected two bananas to pads 8 and 10. 

[![](https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/hb.jpeg)](https://youtu.be/fXvc5rzlyJk)

### Part B
### OLED screen

No OLED now so let's move to the next part

### Part C
### Paper Display

Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

Inspiration: I finished watching the Queen's Gambit one afternoon and was all ready to buy a chessborad. Then a thought hit me: what if I make a chess game out of raspberry pi! Such a brilliant idea! Help me save money too. So how should I start?

...

OK tic-tac-toe it is. (I claim it's similar to chess - JK)

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/show.jpeg"  width="500"/>

There are two states in this game. Either player 'X' or 'O' wins, or they have a draw. 

Here's my cardbox tic-tac-toe game. 

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/design.jpeg"  width="250"/>

Length: 16 cm

Width: 14 cm

Height: 5 cm 

The smaller grids (9 in total) will represent grid 1 to 9 in a tic-tac-toe game. The upper larger grid will be the place I fix the pi sreen. Players ('X' and 'Y') will look at the screen to see the game board and whose turn it is. 

I need to consider hardware problem. Since the sensor is very small, I need to carefully separate the touch grids so that they can connect to their corresponding sensor positions without getting tangled. 

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/interior.jpeg"  width="250"/>

Interim: coding (done - uplaoded as tic_tac_toe.py) -> think of where to place touch grids -> check if that works with the sensor -> if not go back to rearrange touch grids -> check ... until it works. 


**b. Make a video of your paper display in action.**

Video to be uploaded.

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

It needs to have relatively long length and width so that I can separate the grids. Moreover, if two players are going to play the game, it's better to have a larger display. However, I need to make do with the small screen now. The current prototype is meant to be used in a close distance due to the size of the screen. Otherwise, players will not see the board. 

### Part D
### Materiality

**Open Ended**: 

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

I want players focus on the game, so I used cardbox to hide the pi, touching sensor, and the conductive tape. 

**b. explain the selection.**

Reasons: cardboxes are easy to get and shape. conductive tape helps connect the touch grids and the touching sensor. I also used normal tape to reassemble the box. 

### Part E

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/paper.jpeg"  width="250"/>

### Part F

video tp be uploaded.

### Part 2.

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/document.png"  width="500"/>

2. "Looks like" prototypes: show us how the device should look, feel, sit, weigh, etc.

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%204/paper.jpeg"  width="250"/>

The device is a lightweight rectangular cardbox-made tic-tac-toe game. Each player takes turn using the touch grids to draw 'X' or 'O'. Raspberry pi screen shows the game board on the top and prompts players to make their move. 

3. "Works like" prototypes: show us what the device can do

The device allows users to play the tic-tac-toe game.

There are three possibilities: Player 'X' wins, player 'O' wins, and tie. I updated the code (improved.py) so that when a game ends, the device allows players to restart by touching grid 1. 

I aslo switched to allegator clips. Since I need 9 touch grids to align properly, allegator clips are better than conductive tape. 

4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device

Video to be uploaded.


