import os
import time
import win32api, win32con
from PIL import ImageOps
from PIL import ImageGrab
from numpy import *


x = 145
y = 220
def screenGrab():
    im = ImageGrab.grab((x,y,x+635,y+480))
    im.save(os.getcwd() + "\\full_snap_" + str(int(time.time())) + ".png", "PNG")
    return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print("left Down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print("left release")


def mousepos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))

def get_cords():
    x,y=win32api.GetCursorPos()
    print(x,y)

##### Navigate through start menu ####
def StartGame():
    #click on Play button
    mousepos((526,401))
    leftClick()
    time.sleep(1)
    
    #click on continue button
    mousepos((494,593))
    leftClick()
    time.sleep(1)
    #click on skip button
    mousepos((778,660))
    leftClick()
    time.sleep(1)
    #click on continue button
    mousepos((544,575))
    leftClick()
    time.sleep(1)

##### Coordinator Class ####
class Cord:
    t_rice=(271,488)
    t_nori=(227,551)
    t_roe=(273,551)

    foldMat=(384,570)

    phone=(740,515)

    menuTop=(698,431)
    menuRice=(702,453)
    
    Exit=(786,490)
    Back=(686,497)
    
    nori=(681,440)
    roe=(742,437)
    rice=(734,444)

############## Keeping Track of Ingredients ##########
foodOnHand = {'rice':10, 'nori':10, 'roe':10}
############# Making Sushi #############
def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousepos(Cord.t_rice)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_nori)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_roe)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1 
        mousepos(Cord.t_rice)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_rice)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_nori)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousepos(Cord.t_rice)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_nori)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_roe)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.t_roe)
        leftClick()
        time.sleep(.1)
        mousepos(Cord.foldMat)
        leftClick()
        time.sleep(1.5)

############## Buy Food/Navigating Phone Menu ##########
def buyFood(food):
    if food == 'rice':
        mousepos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousepos(Cord.menuRice)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.rice[0]-x, Cord.rice[1]-y)) != (127, 127, 127):
            print('rice is available')
            mousepos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousepos(Cord.Exit)
            foodOnHand['rice'] += 10     
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('rice is NOT available')
            mousepos(Cord.back)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousepos(Cord.menuTop)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.nori[0]-x, Cord.nori[1]-y)) != (33, 30, 11):
            print('nori is available')
            mousepos(Cord.nori)
            time.sleep(.1)
            leftClick()
            mousepos(Cord.Exit)
            foodOnHand['nori'] += 10         
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('nori is NOT available')
            mousepos(Cord.Back)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousepos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menuTop)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel((Cord.roe[0]-x, Cord.roe[1]-y)) != (127, 61, 0):
            print('roe is available')
            mousepos(Cord.roe)
            time.sleep(.1)
            leftClick()
            mousepos(Cord.Exit)
            foodOnHand['roe'] += 10                
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available')
            mousepos(Cord.Back)
            leftClick()
            time.sleep(1)
            buyFood(food)    


########### Clearing Tables ##########
def clear_tables():
    mousepos((268, 360))
    leftClick()

    mousepos((374, 368))
    leftClick()
 
    mousepos((467, 370))
    leftClick()
 
    mousepos((580, 372))
    leftClick()
 
    mousepos((675, 372))
    leftClick()
 
    mousepos((779, 371))
    leftClick()

    time.sleep(1)


################# Setting New Bounding Boxes ########
def get_seat_one():
    box = (191,282,212,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (292,282,313,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (393,282,414,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (494,282,515,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (595,282,616,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (696,282,717,294)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a

################### Sushi Types Dictionary ##############
sushiTypes = {1088:'onigiri', 1345:'caliroll', 760:'gunkan',}

########### Checking Food on Hand #################
def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print('%s is low and needs to be replenished' % i)
                buyFood(i)

         
######## Putting It All Together ######### Final Flow #########
#Check seats > if customer, make order > check food > if low,
#buy food > clear tables > repeat.
def check_customers():
    s1 = get_seat_one()
    if s1 in sushiTypes:
        print('table 1 is occupied and needs %s' % sushiTypes[s1])
        makeFood(sushiTypes[s1])
    else:
        print('sushi not found!\n sushiType = %i' % s1)
 
    s2 = get_seat_two()
    if s2 in sushiTypes:
        print('table 2 is occupied and needs %s' % sushiTypes[s2])
        makeFood(sushiTypes[s2])
    else:
        print('sushi not found!\n sushiType = %i' % s2)

    s3 = get_seat_three()
    if s3 in sushiTypes:
        print('table 3 is occupied and needs %s' % sushiTypes[s3])
        makeFood(sushiTypes[s3])
    else:
        print('sushi not found!\n sushiType = %i' % s3)
 
    s4 = get_seat_four()
    if s4 in sushiTypes:
        print('table 4 is occupied and needs %s' % sushiTypes[s4])
        makeFood(sushiTypes[s4])
    else:
        print('sushi not found!\n sushiType = %i' % s4)

    s5 = get_seat_five()
    if s5 in sushiTypes:
        print('table 5 is occupied and needs %s' % sushiTypes[s5])
        makeFood(sushiTypes[s5])
    else:
        print('sushi not found!\n sushiType = %i' % s5)
 
    s6 = get_seat_six()
    if s6 in sushiTypes:
        print('table 1 is occupied and needs %s' % sushiTypes[s6])
        makeFood(sushiTypes[s6])
    else:
        print('sushi not found!\n sushiType = %i' % s6)
 
    clear_tables()
    checkFood()


#################### MAIN FUNCTION ##################
def main():
    StartGame()
    while True:
        check_customers()
