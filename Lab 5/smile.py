#nano indentation is super weird. 
 # for loops and if have different requirements
 # this version of smile.py has indentation specifically adjusted for nano file in my computer


 import numpy as np
 import cv2
 import sys

 from gtts import gTTS
 import os

 #t1 = 'No user detected.'
 #t2 = 'Say cheese!'
 t3 = 'cheese!'
 language = 'en'

 #m1 = gTTS(text=t1, lang=language, slow=False)
 #m1.save("no_user.mp3")

 #m2 = gTTS(text=t2, lang=language, slow=False)
 #m2.save("cheese.mp3")

 m3 = gTTS(text=t3, lang=language, slow=False)
 m3.save("smile.mp3")

 face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 smile_casecade = cv2.CascadeClassifier('haarcascade_smile.xml')


 img=None

 webCam = False
 if(len(sys.argv)>1):
    try:
       print("I'll try to read your image");
       img = cv2.imread(sys.argv[1])
       if img is None:
          print("Failed to load image file:", sys.argv[1])
    except:
       print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
 else:
    try:
       print("Trying to open the Webcam.")
       cap = cv2.VideoCapture(0)
       if cap is None or not cap.isOpened():
          raise("No camera")
       webCam = True
    except:
       img = cv2.imread("../data/test.jpg")
       print("Using default image.")

 state = 0
 pre = 0

 while(True):

    if webCam:
       ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    users = False
    smiling = False
    for (x,y,w,h) in faces:
        users = True
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        smiles = smile_casecade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            smiling = True
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    if (not users):
       state = 0
       pre = 0
       cv2.putText(img, "No user detected", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
 #      if(state != pre):
 #         os.system("mpg321 no_user.mp3")
    elif (not smiling):
       state = 1
       pre = 1
       cv2.putText(img, "Say cheese ------", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
 #      if(state != pre):
 #         os.system("mpg321 cheese.mp3")
 #         pre = state
    else:
       state = 2
       cv2.putText(img, "Nice smile!", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
       if(state != pre):
         #this is the silence file so that words are not cut off
          os.system("mpg321 out.mp3")
          os.system("mpg321 smile.mp3")
          pre = state

    if webCam:
       cv2.imshow('face-detection (press q to quit.)',img)
       if cv2.waitKey(1) & 0xFF == ord('q'):

          cap.release()
          break
    else:
       break

 cv2.imwrite('faces_detected.jpg',img)
 cv2.destroyAllWindows()
