from flask import Flask, render_template, Response
import cv2
from Untitled37 import maskcheck
app = Flask(__name__)

#camera = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        frame = maskcheck()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')