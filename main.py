import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from playsound import playsound


path = os.path.dirname(__file__)
won_image = path + "/res/won2.png"
lost_image = path + "/res/lost2.png"


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

if __name__ == "__main__":
    while True:
        won = pg.locateOnScreen(won_image,grayscale = True, confidence = 0.65, region=(800,120,300,200))
        lost = pg.locateOnScreen(lost_image,grayscale = True, confidence = 0.65, region=(800,120,300,200))
        won_round()
        lost_round()
    







    
