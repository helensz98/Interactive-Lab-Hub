from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import time
import board
import busio
import adafruit_mpu6050
import json
import socket

import signal
import sys
from queue import Queue


i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), "yes no [unk]")
shake = False 

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        if 'yes' in rec.PartialResult():
            print('Thank you! Pleas shake me now!')
            shake = True
        else:
            print("That's fine! Have a good day:)")
        break

while shake:
    if(max(mpu.acceleration)>10):
        print("Nice and clean again!")
        break

print('The book has resumed to sleep')

