import time
import numpy as np
import cv2
import mss
from PIL import Image


"""
http://python-mss.readthedocs.io/examples.html

Suggestions for improvement.

There are currently two image capturing functions running serially at this moment.
It would be better if they ran parallell (if framerates becomes an issue...)

@TODO: keep in mind that score is saved between deaths! We do want the keep each game independent?
    Find a way to parse image into a python integer.
"""
        

def screen_record_efficient(top, left, width, height):
    # 800x600 windowed mode
    mon = {'top': top, 'left': left, 'width': width, 'height': height} #This is formatted so it looks nice on unity desktop, with the window top left.

    title = '[MSS] FPS benchmark'
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while time.time() - last_time < 1:
        img = np.asarray(sct.grab(mon))
        fps += 1

        cv2.imshow(title, img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return fps


if __name__ == '__main__':
    while(True):
        #print(screen_record_efficient(110,710,110,30)) #captures the score

        #print(screen_record_efficient(110,540,80,30)) #capture time
        print(screen_record_efficient(50,60,800,600)) #captures entire screen