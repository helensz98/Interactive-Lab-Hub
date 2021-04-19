import numpy as np
import cv2
import sys

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
      print("Failed to load the image are you sure that:", sys.argv[1],"is a pas a path to an image?")
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
      cv2.putText(img, "No user detected", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
   elif (not smiling):
      cv2.putText(img, "Say cheese ------", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)

   else:
      cv2.putText(img, "Nice smile!", (50, 50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),25)

   if webCam:
      cv2.imshow('face-detection (press q to quit.)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break

cv2.imwrite('faces_detected.jpg',img)
cv2.destroyAllWindows()

