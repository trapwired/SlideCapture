import time
import pyautogui
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2


# path to location to store screenshots
FILEPATH = 'C:/Users/do-we/Desktop/Screenshots/'

# seconds to wait before capturing screen
TIMEOUT = 2

# Thresholds
MSE_THRESH = 100
SSIM_THRESH = 0.95

# Use bounding box for comparison of screenshots (i.e. on zoom)
CROP_COMPARISON_IMAGE = False


def mse(im1, im2):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((im1.astype("float") - im2.astype("float")) ** 2)
    err /= float(im1.shape[0] * im1.shape[1])
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(im1, im2):
    # return true if pictures not similar
    m = mse(im1, im2)
    s = ssim(im1, im2)
    if (m > MSE_THRESH) or (s < SSIM_THRESH):
        return True
    return False


def take_screenshot():
    # return whole screenshot for saving and grey for comparison
    # im1 = pyautogui.screenshot(region=(0,0, 300, 400))
    im1 = pyautogui.screenshot()
    im = im1
    if CROP_COMPARISON_IMAGE:
        # specify the crop-box
        left = 0
        right = im1.width
        top = int(0.1*im1.height)
        bottom = int(0.9*im1.height)
        im = im1.crop((left, top, right, bottom))

    cv2im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    res = cv2.cvtColor(cv2im, cv2.COLOR_BGR2GRAY)
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
    time.sleep(5)
    start()


