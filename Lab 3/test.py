from vosk import Model, KaldiRecognizer
import sys
import os
import wave

print("Dear traveller! I have been lying here for so long and now I'm coated in dirst. \n Could you please help me shake it off?")
print('Say [yes/no]')

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
    if(max(mpu.acceleration)>30):
        print("Nice and clean again!")
        break
    elif(max(mpu.acceleration)<=30):
        print('Please try harder!')
        # print(rec.PartialResult())
print('The book has resumed to sleep')
# print(rec.FinalResult())