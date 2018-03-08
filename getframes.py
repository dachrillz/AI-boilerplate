import time
import numpy as np
import cv2
import mss
import sys
from PIL import Image
from mario_level_1 import start_game
import _thread
import threading


"""
http://python-mss.readthedocs.io/examples.html

Suggestions for improvement.

There are currently two image capturing functions running serially at this moment.
It would be better if they ran parallell (if framerates becomes an issue...)

@TODO: keep in mind that score is saved between deaths! We do want the keep each game independent?
    Find a way to parse image into a python integer.
"""

class score_container():
    def __init__(self):
        self.score = 0
        self.time = 0
        self.x = 0
        
        
    def update_score(self, score):
        self.score = score
        
    def update_time(self, time):
        self.time = time
        
        
    def get_time(self):
        return self.time
        
    def get_score(self):
        return self.score
        
    def set_x(self, x):
        self.x = x
        
    def get_x(self):
        return self.x
        

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

def start_capture():
    while(True):
        print(screen_record_efficient(50,60,800,600)) #captures entire screen
        
def print_scores(sc):
    while(True):
        print(sc.get_x())


if __name__ == '__main__':
    sc = score_container()

    t1 = threading.Thread(target=start_game,args=(sc,))
    
    t1.start()
    print("started first thread")
    
    time.sleep(2)
    print("slept")
    
    
    print("starting thread 2")
    t2 = threading.Thread(target=start_capture,args=())
    t2.start()
    print("started second thread")
    
    
    t3 = threading.Thread(target=print_scores,args=(sc,))
    t3.start()
    
    
    
    t1.join()
    t2.join()
    t3.join()
    
    
    

    


    #while(True):
        #print(screen_record_efficient(110,710,110,30)) #captures the score

        #print(screen_record_efficient(110,540,80,30)) #capture time
      #  print(screen_record_efficient(50,60,800,600)) #captures entire screen
