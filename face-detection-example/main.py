#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This Example Stream works with Face Detection using Haarcascasde Models
# Also Compatible with Pi HQ Camera. This can be modified to suit your application.
#Implented for one client device to stream
# main.py

# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

# App Globals (do not edit)
app = Flask(__name__)

#background process happening without any refreshing
@app.route('/lock')
def lock():
    print ("Lock")
    os.system("python servo.py 1 2 0.4 1")       
    return ("nothing")

@app.route('/unlock')
def unlock():
    print ("Unlock")
    os.system("python servo.py 179 180 0.4 1")       
    return ("nothing")


@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
