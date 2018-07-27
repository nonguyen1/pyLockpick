# Filename: pyLock.py
# Author: Nathaniel Nguyen
# Description: TODO
# Date: Jul 24 2018

import numpy as np
import cv2
#from mss.darwin import mss
import mss
import mss.tools
import pyautogui
import time

#pyautogui.PAUSE = 1.5
lock_image1 = 'lock1.png'
lock_image2 = 'lock2.png'
lock_image3 = 'lock3.png'
lock_image4 = 'lock4.png'

picks = 100;
last_time = time.time() 
with mss.mss() as sct:
    while(True):
        monitor = {'top': 0, 'left': 0, 'width': 350, 'height': 270}
        screen = sct.grab(monitor)
        mss.tools.to_png(screen.rgb, screen.size, output="test.png")
        lock_coords = pyautogui.locate(lock_image1, "test.png")
        if (not lock_coords):
            lock_coords = pyautogui.locate(lock_image2, "test.png")
            if (not lock_coords):
                lock_coords = pyautogui.locate(lock_image3, "test.png")
                if (not lock_coords):
                    lock_coords = pyautogui.locate(lock_image4, "test.png")

        if (lock_coords and picks):
            #picks -= 1
            pyautogui.click(x=lock_coords[0] / 2, y=lock_coords[1] / 2 + 5)
