import tensorflow as tf
from tensorflow import keras
# Load the model
from tensorflow.keras.preprocessing import image
import numpy as np

CLASS_NAMES = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

def prepare_image(file):
    img = image.load_img(file, target_size=(256,256))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.vgg16.preprocess_input(img_array_expanded_dims)

def predict(img):
    preprocessed_image = prepare_image(img)
    loaded_model = tf.keras.models.load_model('flowers.h5')
    predictions = loaded_model.predict(preprocessed_image)
    np.argmax(predictions)
    return CLASS_NAMES[np.argmax(predictions)]