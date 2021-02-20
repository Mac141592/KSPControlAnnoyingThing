from pynput.keyboard import Controller, Key, Listener, KeyCode
#from pynput.mouse import Button, Controller
import math
import random
import time

'''import krpc
conn = krpc.connect(name='Hello World')
vessel = conn.space_center.active_vessel
print(vessel.name)'''



keyboard = Controller()



def random_throttle():

    keyboard.press('z')
    keyboard.release('z')
def random_dethrottle():

    keyboard.press('x')
    keyboard.release('x')
def rcs_loop_one():
    keyboard.press('r')
def take_helmet():
    keyboard.press('o')
def map():
    keyboard.press('m')
def throttle():
    keyboard.press('z')
def dethrottle():
    keyboard.press('y')
def stage():
    keyboard.press(Key.space)
def warp_up():
    keyboard.press('.')
    keyboard.release('.')
def warp_down():
    keyboard.press(',')
    keyboard.release(',')
def iva():
    keyboard.press('c')
def loop_one():

    time.sleep(5)
    random_throttle()
    time.sleep(10)
    random_dethrottle()
def loop_two():
    iva()
    throttle()
def loop_three():
    throttle()
    map()
def loop_four():
    keyboard.press('u')
    keyboard.press('g')
    keyboard.press('m')
def loop_five():
    warp_up()
    warp_up()
    warp_up()
def loop_six():
    warp_down()
    time.sleep(0.3)
    warp_down()
    time.sleep(0.3)
    warp_down()
def tab_out():
    with keyboard.pressed(Key.alt_l):
        keyboard.press(Key.tab)

def check_num():
    pass
def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == KeyCode.from_char('w'):
        time.sleep(2)
        if key == KeyCode.from_char('w'):
            num = random.randrange(0,10,1)
            if num > 7:
                keyboard.press('a')
            if num < 3:
                keyboard.press('d')

def on_release(key):
    print('{0} release'.format(
        key))
    # Checks for gradual throttle up
    if key == Key.shift:
        time.sleep(2)
        num = random.randrange(0,10,1)
        print(num)
        if num > 6:
            throttle()
        if num < 2:
            loop_five()
            time.sleep(2)
            loop_six()
    # Checks for quicksave
    if key == Key.f5:
        time.sleep(5)
        num = random.randrange(0,10,1)
        print(num)
        if num > 5:
            loop_one()
            loop_three()
        if num < 2:
            loop_two()
        if num > 4:
            loop_four()
        if num > 6:
            map()
            tab_out()

    # This checks for sideways movement to the right (direction to orbit in
    if key == KeyCode.from_char('d'):
        time.sleep(random.randrange(0,5,1))
        num = random.randrange(0,10,1)
        print(num)
        if num > 7:
            map()
        if num == 4 or 5:
            loop_four()
        if num == 6:
            loop_one()
            stage()
            tab_out()
    # I have literally no idea what this is checking for ## I found out. Its translate forward
    if key == KeyCode.from_char('h'):
        time.sleep(random.randrange(0, 5, 1))
        keyboard.press('r')
        iva()
    # Checking for directional movement
    if key == KeyCode.from_char('w'):
        pass
    # Check for time warping
    if key == KeyCode.from_char('.'):
        time.sleep(random.randrange(0, 5, 1))
        num = random.randrange(0,5,1)
        print(num)
        if num > 2:
            loop_five()
            iva()
    if key == KeyCode.from_char(','):
        time.sleep(random.randrange(0, 5, 1))
        num = random.randrange(0,5,1)
        if num > 2:
            loop_five()
            loop_six()
    # Checking for staging
    if key == Key.space:
        time.sleep(random.randrange(0, 5, 1))
        num = random.randrange(0,10,1)
        print(num)
        if num > 7:
            map()
        if num < 6:
            tab_out()
    # Checking for braking probably
    if key == KeyCode.from_char('b'):
        time.sleep(random.randrange(0, 5, 1))
        num = random.randrange(0,10,1)
        if num > 6:
            keyboard.press('a')
            iva()
        if num < 3:
            keyboard.press('d')
        if num == 4:
            tab_out()
    if key == KeyCode.from_char('x'):
        num = random.randrange(0,10,1)
        if num > 3:
            throttle()
            iva()
    if key == KeyCode.from_char('z'):
        time.sleep(random.randrange(0, 5, 1))
        num = random.randrange(0,10,1)
        if num > 3:
            dethrottle()
        if num == 4:
            tab_out()
    # This stops the thingy from checking for key presses
    if key == KeyCode.from_char('0'):
        # Stop listener
        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
