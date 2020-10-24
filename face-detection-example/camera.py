#Modified by smartbuilds.io
#Date: 23.10.20
#for more haarcascade examples visit:
#https://github.com/opencv/opencv/tree/master/data/haarcascades

# Importing Packages
import cv2

#define haarcascade variable
haar_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    #Capture Video from camera - compatible with Pi HQ Camera 
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        #Iterating over each frame
        stream, image = self.video.read()
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        obect_rects=haar_cascade.detectMultiScale(gray,1.3,5)
 
        for (x,y,w,h) in obect_rects:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            break
        #OpenCV video capture to JPEG -> to main.py
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

