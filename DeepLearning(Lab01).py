#import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.utils import to_categorical
#import numpy as np
(train_data,train_lbl),(test_data,test_lbl) = mnist.load_data()
print('Before reshape\n',train_data.shape)
print(test_data.shape)
train_data=train_data.reshape(60000,784)
test_data=test_data.reshape(10000,784)
print('After reshape\n',train_data.shape)
print(test_data.shape)
train_lbl = to_categorical(train_lbl)
test_lbl = to_categorical(test_lbl)
model=Sequential([
    Dense(100,input_dim=784),
    Activation('sigmoid'),
    Dense(10),
    Activation('softmax')
])
print(model.summary())
# Z=np.array([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7])
# def sigmoid(z):
#     return 1/(1+np.exp(-z))
#
# g=sigmoid(Z)
# plt.plot(Z,g)
# plt.show()
