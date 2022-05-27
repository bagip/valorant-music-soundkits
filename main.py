import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from playsound import playsound


path = os.path.dirname(__file__)


def won_round():
    if won == None:
        print(won)
    else:
        playsound(path +"/res/Bruh.wav")

def lost_round():
    if lost == None:
        print(lost)
    else:
        playsound(path +"/res/wow.wav")


while True:
    won = pg.locateOnScreen(path + "/res/won3.png",grayscale = True, confidence = 0.65)
    lost = pg.locateOnScreen(path +"/res/lost2.png",grayscale = True, confidence = 0.65)
    won_round()
    lost_round()







    