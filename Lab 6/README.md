# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

Blackjack!


## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 

## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png?raw=true)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.



## Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python.  Lets spend a few minutes running these and seeing how messages are transferred and show up. 

**Running Examples**

* Install the packages from `requirements.txt`, ideally in a python environment. We've been using the circuitpython environment we setup earlier this semester. To install them do `pip install -r requirements.txt`
* to run `sender.py` type `python sender.py` and fill in a topic name, then start sending messages. You should see them on MQTT Explorer
* to run `reader.py` type `python reader.py` and you should see any messages being published to `IDD/` subtopics.

## Streaming a Sensor

We've included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%204) that streams sensor inputs over MQTT. Feel free to poke around with it!

## The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB we too can find unity in our heart, minds and souls. With the help of machines can  overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [Pi Display](https://www.adafruit.com/product/4393).

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="300">

You are almost there!

The second step to achieving our great enlightenment is to run `python color.py`

You will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one. 

I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also I have't load tested it so things might just immediately break when every pushes the button at once.

You may ask "but what if I missed class?"

Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can got to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs.

Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 



## Make it your own

I worked with Erin Gong (yg545) for this assignment.

**1. Explain your design** 

We designed a simple version of the blackjack game that allows players to remotely participate. Our current version of the game only allows two players at a time but the game can be easily modified to support more players. The rules of the game are described as follows:

1. The players share the score.
2. At each turn, a random number between 1 to 10 is generated and the number is not shown to the players.
3. The players take turns and choose "Yes" or "No" to receive or reject the current number.
4. If the player exceeds a sum of 21 ("busts"), the player loses.

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Participants: Our simplified blackjack game involves 2 players. Observers are welcome!
Time/location: There is no restraint of time and space! Communicate with your friend and start the gamble.
Operations: Players need to be close enough to the twizzlers to select “Yes” or “No”. 
Sound: No voice input/output is included.
Input, output and computation: Players provide different input (“Yes” or “No”) at their own risk. The pi prints the output on the screen, showing the current player and sum after adding in the randomly generated number, should players choose to draw cards.

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

A novice user would need to read the rules of the game and the instructions on how to use the device before playing the game because our rules are different from the classic blackjack.  To help the user understand the current state of the game, the screen on the pie shows the current score and the current player. Two twizzlers labeled "Yes" and "No" are provided as an input device to the user. We chose to use the touch input because it is a quiet interface and allows the users to play the game in quiet places (e.g. libraries and classrooms.)


**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you the input in one location clearly causing response in another location.

## Make it your own

I worked with Erin Gong (yg545) for this assignment.

**1. Explain your design** 

We designed a simple version of the blackjack game that allows players to remotely participate. Our current version of the game only allows two players at a time but the game can be easily modified to support more players. The rules of the game are described as follows:

1. The players share the score.
2. At each turn, a random number between 1 to 10 is generated and the number is not shown to the players.
3. The players take turns and choose "Yes" or "No" to receive or reject the current number.
4. If the player exceeds a sum of 21 ("busts"), the player loses.

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Participants: Our simplified blackjack game involves 2 players. Observers are welcome!

Time/location: There is no restraint of time and space! Communicate with your friend and start the gamble.

Operations: Players need to be close enough to the Erin's twizzlers and my box to select “Yes” or “No”. 

Sound: No voice input/output is included.

Input, output and computation: Players provide different input (“Yes” or “No”) at their own risk. The pi prints the output on the screen, showing the current player and sum after adding in the randomly generated number, should players choose to draw cards.

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

A novice user would need to read the rules of the game and the instructions on how to use the device before playing the game because our rules are different from the classic blackjack.  To help the user understand the current state of the game, the screen on the pie shows the current score and the current player. Two twizzlers labeled "Yes" and "No" are provided as an input device to the user. We chose to use the touch input because it is a quiet interface and allows the users to play the game in quiet places (e.g. libraries and classrooms.)

Interior                                                                                                        | Interior
:--------------------------------------------------------------------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%206/exterior.jpeg" height="300"> |:<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%206/interior.jpeg" height="300">

There was a third touch grid before we revised the game, but now we only use two grids. 

**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you the input in one location clearly causing response in another location.

[simplified blackjack game](https://youtu.be/Zus_SmZWfz8)

**5. BONUS (Wendy didn't approve this so you should probably ignore it)** get the whole class to run your code and make your distributed system BIGGER.
