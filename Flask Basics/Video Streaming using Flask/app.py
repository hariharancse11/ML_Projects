from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)
camara = cv2.VideoCapture(0)

def generateframes():
    while True:

        success,frame = camara.read()
        if not success:
            break
        else:
            ret,buffer= cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generateframes(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__  == '__main__':
    app.run(debug=True)