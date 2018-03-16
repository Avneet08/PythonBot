from PIL import ImageGrab
import os
import time

def screenGrab():
    x=190
    y=185
    im = ImageGrab.grab((x,y,x+635,y+480))
    im.save(os.getcwd() + "\\full_snap_" + str(int(time.time()))+".png","PNG")

if __name__=='__main__':
    screenGrab()
