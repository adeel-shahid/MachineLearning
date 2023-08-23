import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Define a function to easily handle manipulation.
def manip_image(image, alpha, beta):
    new_image = np.zeros(image.shape, image.dtype)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            new_image[y, x] = np.clip(alpha * image[y, x] + beta, 0, 255)

    return new_image

low_gray = cv.imread('download.png')
# Test on the dark image
l_bright = manip_image(low_gray, 1, 150)
l_dark = manip_image(low_gray, 1, -25)

# Compare the results
plt.figure()
plt.subplot(231), plt.imshow(l_dark, cmap='gray')
plt.grid(False), plt.xticks([]), plt.yticks([])

plt.subplot(232), plt.imshow(low_gray, cmap='gray')
plt.grid(False), plt.xticks([]), plt.yticks([])

plt.subplot(233), plt.imshow(l_bright, cmap='gray')
plt.grid(False), plt.xticks([]), plt.yticks([])

plt.subplot(234)
plt.plot(cv.calcHist([l_dark], [0], None, [256], [0, 256])), plt.ylim((0, 1100))

plt.subplot(235)
plt.plot(cv.calcHist([low_gray], [0], None, [256], [0, 256])), plt.ylim((0, 1100))

plt.subplot(236)
plt.plot(cv.calcHist([l_bright], [0], None, [256], [0, 256])), plt.ylim((0, 1100))

plt.show()