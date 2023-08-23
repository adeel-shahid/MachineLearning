# import cv2 as cv
# img = cv.imread('amir.png')
# print(type(img))
# print(img.shape)
# cv.imshow('Amir Image',img)
# cv.waitKey(0)
###################################################################################
#Video
# frames = cv.VideoCapture('Kitten.mp4')
#
# while True:
#     isTrue,frame = frames.read()
#
#     if isTrue:
#         cv.imshow('video',frame)
#         if cv.waitKey(20) and 0xFF==ord('d'):
#             break
#     else:
#         break
#
# frames.release()
###################################################################################
# import cv2 as cv
# img = cv.imread('amir.png')
# print(type(img))
# print("Shape before Conversion",img.shape)
# cv.imshow('Amir Image',img)
# cv.waitKey(0)
# grayimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# print("Shape after Conversion",grayimg.shape)
# cv.imshow('Amir Gray Scale Image',grayimg)
# cv.waitKey(0)
########################################################################################33
#Edge Detection
# import cv2 as cv
# import matplotlib.pyplot as plt
# img = cv.imread('amir.png')
# plt.subplot(1,3,1)
# plt.imshow(img)
# plt.title('Orignial Image')
# grayimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# im_edge = cv.Canny(grayimg,50,100)
# plt.subplot(1,3,2)
# plt.imshow(grayimg,cmap='gray')
# plt.title('Gray Scale Image')
# plt.subplot(1,3,3)
# plt.imshow(im_edge,cmap='gray')
# plt.title('Edge Detection Image')
# plt.show()
##############################################################################################
#Histogram
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
im = cv.imread('amir.png')
hist = cv.calcHist([im],[0],None,[256],[0,255])
plt.figure(figsize=(8,5))
plt.bar(np.arange(256),hist.flatten(),width=1)
plt.title('Image Histogram')
plt.ylabel('Frequency')
plt.xlabel('Pixel Intensity')
plt.xlim([0,256])
plt.show()
