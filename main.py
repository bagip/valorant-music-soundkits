from re import I
import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from playsound import playsound
import time

path = os.path.dirname(__file__)
won_image = path + "/res/won2.png"
lost_image = path + "/res/lost2.png"
won_sound = ''
lost_sound = ''

if not won_sound:
    with open(path + "/res/sounds.txt") as won_text:
        lines = won_text.read().splitlines()
        won_sound = lines[0]

if not lost_sound:
    with open(path + "/res/sounds.txt") as lost_text:
        lines = lost_text.read().splitlines()
        lost_sound = lines[1]

def won_round():
    if won == None:
        print(won)
        time.sleep(0.1)
    else:
        playsound(path +"/res/" + won_sound)

 
def lost_round():
    if lost == None:
        print(lost)
        time.sleep(0.1)
    else:
        playsound(path +"/res/" + lost_sound)

won_text.close()
lost_text.close()

if __name__ == "__main__":
    while True:
        won = pg.locateOnScreen(won_image,grayscale = True, confidence = 0.65, region=(700,155,300,200))
        lost = pg.locateOnScreen(lost_image,grayscale = True, confidence = 0.65, region=(700,155,300,200))
        won_round()
        lost_round()
    







    