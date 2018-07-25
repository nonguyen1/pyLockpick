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
lock_image1 = 'lock_center1.png'
lock_image2 = 'lock_center2.png'
lock_image3 = 'lock_center3.png'

timer = 0
for _ in range(timer):
    print(timer)
    time.sleep(1)
    timer -= 1


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

        if (lock_coords):
            print(lock_coords[0], lock_coords[1])
            pyautogui.click(x=lock_coords[0] / 2, y=lock_coords[1] / 2)

        print('screen size: ', screen.size)
        print('The loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

#        if cv2.waitKey(25) & 0xFF == ord('q'):
#            cv2.destroyAllWindows()
#            break


# OpenCV fun process image.
#def process_img(original_image):
#    processed_img = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
#    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
#    return processed_img

