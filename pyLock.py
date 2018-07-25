# Filename: pyLock.py
# Author: Nathaniel Nguyen
# Description: TODO
# Date: Jul 24 2018

import numpy as np
from PIL import ImageGrab
import cv2
import time
#from mss import mss
from mss.darwin import MSS as mss
import pyautogui

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

last_time = time.time() 
with mss() as sct:
    while(True):

        monitor = {'top': 45, 'left': 0, 'width': 320, 'height': 240}
        screen = np.array(sct.grab(monitor)) 
        new_screen = process_img(screen)

        #cv2.imshow('window', screen)

        cv2.imshow('window', new_screen)

        print('The loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
