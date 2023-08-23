from base64 import b64decode

from flask import  Flask,request
from keras.models import load_model
import numpy as np
from PIL import Image
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.utils import to_categorical

app = Flask(__name__)
@app.route('/')
def ProcessImage():
    model = load_model('model.hdf5')
    image = request.files['img']
    imgs = Image.open(image).convert('L')
    img = imgs.resize((28, 28))
    x = np.array(img)
    x = x.reshape((1, 784))
    x = x / 255.0
    prediction = model.predict(x)
    digit = np.argmax(prediction)
    return str(digit)

if __name__ == '__main__':
    app.run()