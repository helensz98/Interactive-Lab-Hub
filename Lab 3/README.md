# You're a wizard, [Jingjun]

# Hardware problem occurs. I Need to replace my SD card (have consulted Professor Ju). The lab is therefore incomplete. 



<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

You come upon a book burried under a pile of cloths. Surprise! It's a magical book once belonged to a witch. It asks nicely if you can help shake off the dust on it, and even if you say no, it won't be mad at you!

1. Sketch ideas for what you'll work on in lab on Wednesday.

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%203/sketch.png" height="600">

script:

The Magical Book: You've found me, dear traveller! Could you please help me shake off the dust? I have been lying here for so long. 
Insturction: Please say [Yes/No].

If yes: You are so kind! Please shake me now:
   
      if shake:
      
         Nice and clean again
 
If no: that's ok! Have a good day:)

The book has resumed to sleep

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Yingshan Wang (my sister): It's interesting how you always come up with stories to go with the design. 

Panglei(Panda) Xu: I like your idea of the Magical Book that allows users to pysically interact with the Book by shaking the device. One thing that I would suggest is that your magical book can have multiple responses based on how users shake it. Make sure and secure the accelerometer on the Pi to have accurate movement reading. 


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

[video](https://youtu.be/YQlVD_0VM1M)

<img src="https://github.com/helensz98/Interactive-Lab-Hub/blob/Spring2021/Lab%203/controller.jpeg" height="500">

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?

The sensors easily captures movement and voice input. However, one participant told me that she had to raise her volume, or the pi might not register her answer.  

### What worked well about the controller and what didn't?

I use the terminal to control the running of the program, which is simple to operate. However, it is weird to look at the screen and see the logs while interacting with the Pi. It'd be better to show text and pictures on the Pi, which also helps build up the sense of magic. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

Users interact with system differently. Using a bluetooth headphone might help users better interact with the system. I should also consider using text2speech to output system's response with voice.    


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

I can record how long it takes for each user to decide whether to help the book, if they try to communicate with it other than saying yes or no, and what they say after seeing the Good day wish even though they have refused to help. Will users reciprocate if the system appears to be polite and understanding? I can build a voice interaction database focusing on the questions above. No additional sensing modalities are needed.    



