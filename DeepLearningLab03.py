from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPool2D,Flatten
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2 as cv
from PIL import Image

classes=10
inputSize = 784
#Load mnist Data set
(train_data,train_lbl),(test_data,test_lbl) = mnist.load_data()
#Convert to categorical Label
train_lbl = to_categorical(train_lbl,classes)
test_lbl = to_categorical(test_lbl,classes)
#Fully connected neural networks or dense neural network
model=Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    MaxPool2D((2,2)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPool2D((2,2)),
    Flatten(),
    Dense(100,input_dim=1600,activation='sigmoid'),
    Dense(classes,activation='softmax')
])
print(model.summary())
# provide basic settings for neural networks
model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics='accuracy')
#perform training of neural network
hist = model.fit(train_data,train_lbl,epochs=20,batch_size=80,verbose=1)
#perform testing on the nural network
model.save('modelcnn.hdf5')