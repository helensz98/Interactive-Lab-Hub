# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.
our interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/contour.jpeg"  width="400"/>

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/face-detect.jpeg"  width="400"/>

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/flow.jpeg"  width="400"/>

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/object.jpeg"  width="400"/>

#### Teachable Machines (beta, optional)

I made a personal face-mask and sickness detector on teachable machine. If I leave without wearing a mask or show syptoms like coughing, the program will notice immediately. 

[Please click to watch the video](https://youtu.be/4SlWbWK8rR0)

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

The teacahble machine model performs poorly (and frustratingly so) with the pi camera. I spent hours changing epoch and increasing dataset without success. Therefore, I decided to use the face detection openCV model. I also modifeid it so that it when it detects a smile, it says "cheese" to the users and takes a picture. 

I added a 0.5 sec silent out.mp3 file to play before cheese.mp3 so that syllables won't get cut off.

Without user:

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/no.png"  width="400"/>

Without smile:

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/ns.png"  width="400"/>

With (fake) smile:

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/smile.png"  width="400"/>

When the pi detects faces, it prompts users to smile by printing say cheese on the screen. When users smile, the pi says "cheese" to inform users that their smiling faces are captured. 

I connected the pi with my bluetooth headphone. I tried different angles and illumination. It turns out that both detections work best when I'm facing the the camera in a space with ample light. With lower illumination, the face detection performs better than the smile detection which only detects wide, beaming smiles. 


### Part C
### Test the interaction prototype

1. When does it do what it is supposed to do?

    It works in a light setting where users hold the camera from a suitable distance with face front.  

2. When does it fail?

    It fails when any of the above requirements is not met.

3. When it fails, why does it fail?

    Illumination: camera cannot capture enough details to generalize features in dim light. 

    Angle: the pre-trained model is not suitable for face recognition from different angles and disance.

    Distance: The facial detection works well even if users are relatively far from the camera, but the smile detection is not so. Both fail when users get too             
    close. 

4. Based on the behavior you have seen, what other scenarios could cause problems?

    No more than one user can use the device at the same time. With multiple users, the device cannot determine whether it should say cheese or ask users to smile. 


**Think about someone using the system. Describe how you think this will work.**

1. Are they aware of the uncertainties in the system?

    They will not be aware of such things until they encounter problems

2. How bad would they be impacted by a misclassification?
    
    With only 1 user: Suppose that the system misclassifies other events as smiling. It might be annoying to hear a series of "cheese" when the user is not smilling, but it won't hurt since it's just a selfie machine. User will need to look for the picture that she is really smiling though afterwords. 
                      Now, suppose that the system fails to detect a smile. The only thing hurts is user's patience. 
                      
    With multiple users: It'd be chaos. A misclassification will produce the same result as the above but a lot messier. 
    
3. How could you change your interactive system to address this?
   

4. Are there optimizations you can try to do on your sense-making algorithm.

    

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
  
* What is a good environment for X?

* What is a bad environment for X?

* When will X break?

* When it breaks how will X break?

* What are other properties/behaviors of X?

* How does X feel?

**Include a short video demonstrating the answers to these questions.**

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**

[Please click to watch the video](https://youtu.be/LbZ4NJ2dGcU)




