from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Activation
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
#Perform Flattening Operation
# train_data=train_data.reshape(60000,inputSize)
# test_data=test_data.reshape(10000,inputSize)
# #Convert to categorical Label
# train_lbl = to_categorical(train_lbl,classes)
# test_lbl = to_categorical(test_lbl,classes)
# #Fully connected neural networks or dense neural network
# model=Sequential([
#     Dense(100,input_dim=inputSize),
#     Activation('sigmoid'),
#     Dense(classes),
#     Activation('softmax')
# ])
# #provide basic settings for neural networks
# model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics='accuracy')
# #perform training of neural network
# hist = model.fit(train_data,train_lbl,epochs=20,batch_size=80,verbose=1)
# #perform testing on the nural network
# result=model.evaluate(test_data,test_lbl)
# print('Accuracy of test is ',result[1])
# print('Result is ',result)
# #saves the training model
# model.save('model.hdf5')
# # Task
# # EpocVSLoss
# # losses = []
# # epochs =[]
# # for epoch,loss in enumerate(hist.history['loss'],1):
# #     epochs.append(epoch)
# #     losses.append(loss)
#
#
#
# plt.subplot(1,2,1)
# plt.plot(hist.history['loss'])
# plt.title('Loss vs Epoch')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
#
# #EpochVsAccuracy
# plt.subplot(1,2,2)
# plt.plot(hist.history['accuracy'])
# plt.title('Accuracy vs Epoch')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.show()

#Show Images
# for i in range(1,11):
#     plt.subplot(2,5,i)
#     plt.imshow(train_data[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()
# plt.imshow(train_data[5])
# plt.xticks([])
# plt.yticks([])
# plt.show()
#PredictionOfImage
# model = load_model('model.hdf5')
# img = Image.open('ZeroSample.PNG').convert('L')
# img = img.resize((28, 28))
# x = np.array(img)
# x = x.reshape((1, 784))
# x = x / 255.0
# prediction = model.predict(x)
# digit = np.argmax(prediction)
# print(digit)
cv.imwrite('Sample3.png',test_data[2])

