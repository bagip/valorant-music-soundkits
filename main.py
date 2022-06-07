from re import I
import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from playsound import playsound
import time
import sys

if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)

won_image = path + "/res/won2.png"
lost_image = path + "/res/lost2.png"
breach_image = path + "/res/breach.png"
breach_ult_ready = path + "/res/breach_yellow.png"
won_sound = ''
lost_sound = ''

if not won_sound:
    with open(path + "/res/sounds.cfg") as won_text:
        lines = won_text.read().splitlines()
        won_sound = lines[0]

if not lost_sound:
    with open(path + "/res/sounds.cfg") as lost_text:
        lines = lost_text.read().splitlines()
        lost_sound = lines[1]

def won_round():
    if won == None:
        print(won)
        time.sleep(0.05)
    else:
        playsound(path +"/res/" + won_sound)

 
def lost_round():
    if lost == None:
        print(lost)
        time.sleep(0.05)
    else:
        playsound(path +"/res/" + lost_sound)


def breach_ult():
    if breach_yellow == None:
        print(breach_yellow)
        time.sleep(0.05)
    else:
        print("Ide gas")
        breach = pg.locateOnScreen(breach_image, confidence = 0.65)
        if breach == None:
            print(breach)
            time.sleep(0.05)
        else:
            playsound(path + "/res/" + won_sound)
            time.sleep(10)

won_text.close()
lost_text.close()

if __name__ == "__main__":
    while True:
        won = pg.locateOnScreen(won_image,grayscale = True, confidence = 0.65, region=(700,155,300,200))
        lost = pg.locateOnScreen(lost_image,grayscale = True, confidence = 0.65, region=(700,155,300,200))
        breach_yellow = pg.locateOnScreen(breach_ult_ready, confidence = 0.9, region=(370,67,300,51))
        won_round()
        lost_round()
        breach_ult()
    







    