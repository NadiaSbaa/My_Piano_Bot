import pyautogui
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con

#Title 1 Position: X:  496 Y:  820 RGB: (125, 130, 178) 496, 820
#Title 2 Position: X:  613 Y:  816 RGB: (253,  18,   1) 613, 816 
#Title 3 Position: X:  733 Y:  817 RGB: (163, 169, 232) 733, 817
#Title 4 Position: X:  850 Y:  817 RGB: (166, 170, 233) 850, 817


def click(x, y):
    print("click")
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("starting")
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(496, 820)[0] == 0:
        click(496, 820)
    if pyautogui.pixel(615, 816)[0]  == 0:
        click(615, 816)
    if pyautogui.pixel(733, 817)[0]  == 0:
        click(733, 817)
    if pyautogui.pixel(850, 817)[0]  == 0:
        click(850,817)


