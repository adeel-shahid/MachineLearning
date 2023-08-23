import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
#Median Filter
snp_noise = cv.imread('SaltandPepper.png')
gray = cv.imread('img1.png')

def SaltnPeppernois(ref):
    s_and_p = np.random.rand(ref.shape[0], ref.shape[1])

    # if we consider 5% salt and pepper noise, we'd like to have
    # 2.5% salt and 2.5% pepper. thus:
    salt = s_and_p > .975
    pepper = s_and_p < .025

    # in order to add some noise, we should turn off black (pepper) locations and
    # turn on white (white) locations.
    channel_2 = np.atleast_1d(ref[:, :, 1])
    noisy = np.zeros_like(channel_2)

    for i in range(channel_2.shape[0] * channel_2.shape[1]):
        if salt.ravel()[i] == 1:
            noisy.ravel()[i] = 255
        elif pepper.ravel()[i] == 1:
            noisy.ravel()[i] = 0
        else:
            noisy.ravel()[i] = channel_2.ravel()[i]
    return noisy

def MedianFilter(noisy):
    Med = cv.medianBlur(noisy, 5)

    # Display the results
    fig = plt.figure(figsize=(14, 14), dpi=80, facecolor='w', edgecolor='k')
    plt.subplot(121), plt.xticks([]), plt.yticks([])
    plt.imshow(noisy, cmap='gray'), plt.grid(False)
    plt.subplot(122), plt.xticks([]), plt.yticks([])
    plt.imshow(Med, cmap='gray'), plt.grid(False)
    plt.show()

# noisy = SaltnPeppernois(gray)
# MedianFilter(noisy)
# MedianFilter(snp_noise)

#Gausian Filter
def GausianNoise(ref):
    # Creating random normal (gaussian) noise with pre-defined mean and std.
    # The noisy image should be the size of the reference image.
    mean = 0
    sigma = 20.0
    gauss_noise = np.random.normal(mean, sigma, (ref.shape[0], ref.shape[1]))

    # Convert RGB image to Grayscale image using cvtColor()
    gray = cv.cvtColor(ref, cv.COLOR_BGR2GRAY)

    # Add gaussian noise to the image
    g_noisy = gray + gauss_noise  # Gaussian noisy image

    # Showing gray image, noise image, and noisy image
    # fig = plt.figure(figsize=(14, 14), dpi=80, facecolor='w', edgecolor='k')
    # plt.subplot(131), plt.xticks([]), plt.yticks([])
    # plt.imshow(gray, cmap='gray'), plt.grid(False)
    # plt.subplot(132), plt.xticks([]), plt.yticks([])
    # plt.imshow(gauss_noise, cmap='gray'), plt.grid(False)
    # plt.subplot(133), plt.xticks([]), plt.yticks([])
    # plt.imshow(g_noisy, cmap='gray'), plt.grid(False)
    # plt.show()
    return g_noisy


def GausianFilter(ref):
    g_filtered = cv.GaussianBlur(ref, (3, 3), 20, 20)

    # Display the result
    plt.subplot(121), plt.xticks([]), plt.yticks([])
    plt.imshow(ref, cmap='gray'), plt.grid(False)
    plt.subplot(122), plt.xticks([]), plt.yticks([])
    plt.imshow(g_filtered, cmap='gray'), plt.grid(False)
    plt.show()
# ganoise = GausianNoise(gray)
# GausianFilter(ganoise)

########################################################################################
#Intensity transformation


live = cv.imread('Skull.PNG')
mask = cv.imread('skullMask.PNG')
def MasknLive():
    plt.figure(figsize=(10, 10))
    plt.subplot(131), plt.imshow(mask - live, cmap='gray')
    plt.subplot(132), plt.imshow(-(mask - live + 128), cmap='gray')
    plt.subplot(133), plt.imshow(mask - live + 128, cmap='gray')
    plt.show()

def Difference(live):
    plt.figure(figsize=(10, 10))
    plt.subplot(121), plt.imshow(live, cmap='gray')
    plt.subplot(122), plt.imshow(live - 20, cmap='gray')
    plt.show()

# MasknLive()
def TengstanShadding():
    shaded = cv.imread('Tungsten.PNG')
    shading = cv.imread('shading.PNG')

    plt.figure(figsize=(10, 10))
    plt.subplot(131), plt.imshow(shaded, cmap='gray')
    plt.subplot(132), plt.imshow(shading, cmap='gray')
    plt.subplot(133), plt.imshow(np.multiply(shaded, 1 / shading), cmap='gray')
    plt.show()

TengstanShadding()