import time
import pyautogui
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import tkinter as tk


# path to location to store screenshots
FILEPATH = 'C:/Users/do-we/Desktop/Screenshots/'

# seconds to wait before capturing screen
TIMEOUT = 2

# Thresholds
MSE_THRESH = 300
SSIM_THRESH = 0.92


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # return true if pictures not similar
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    if (m > MSE_THRESH) or (s < SSIM_THRESH):
        return True
    return False


def take_screenshot():
    # return whole screenshot for saving and grey for comparison
    # im1 = pyautogui.screenshot(region=(0,0, 300, 400))
    im1 = pyautogui.screenshot()
    opencvImage = cv2.cvtColor(np.array(im1), cv2.COLOR_RGB2BGR)
    res = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2GRAY)
    return im1, res


def start():
    counter = 0
    last_image, last_image_grey = take_screenshot()
    last_image.save(f"{FILEPATH}slide{counter}.png")
    counter += 1
    while (True):
        new_image, new_image_grey = take_screenshot()
        if compare_images(last_image_grey, new_image_grey, 'first try'):
            last_image_grey = new_image_grey
            new_image.save(f"{FILEPATH}slide{counter}.png")
            counter += 1
        time.sleep(TIMEOUT)


if __name__ == '__main__':
    start()


