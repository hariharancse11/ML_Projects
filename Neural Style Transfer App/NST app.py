from flask import Flask,render_template,request, session
import os
from werkzeug.utils import secure_filename
import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import cv2
import numpy as np

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

app = Flask(__name__)

# Define upload folder
UPLOAD_FOLDER  = os.path.join('static','upload')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=("GET", "POST"))
def store_image():
    if request.method=='POST':

        #For image 1
        img = request.files['upload-file']

        img_filename = secure_filename(img.filename)

        img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

        #For image 2

        img2 = request.files['upload-file2']

        img_filename2 = secure_filename(img2.filename)

        img2.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename2))

        session['uploaded_img_file_path2'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename2)

        return render_template('index.html')

@app.route('/showimage')
def showimage():
    processed_img = session.get('uploaded_img_file_path', None)
    processed_img2 = session.get('uploaded_img_file_path2', None)
    return render_template('result.html', show_image = processed_img,show_image2 = processed_img2)

@app.route('/stylize')
def stylize():
    processed_img = session.get('uploaded_img_file_path', None)
    processed_img2 = session.get('uploaded_img_file_path2', None)
    
    
    
    target_image = load_image(processed_img)
    style_image = load_image(processed_img2)
    stylized_image = model (tf.constant(target_image), tf.constant(style_image))[0]
    #final_image=np.squeeze(stylized_image)
    cv2.imwrite('static/upload/generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))
    session['stylized_image'] = os.path.join(app.config['UPLOAD_FOLDER'], 'generated_img.jpg')

    final_image = session.get('stylized_image', None)



    return render_template('result.html', show_image = final_image)

if __name__ == "__main__":
    app.run(debug=True)