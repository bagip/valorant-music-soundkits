import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from playsound import playsound

def won_round():
    if won == None:
        print(won)
    else:
        playsound("C:/blagoje/opencv project/res/gluh.wav")

def lost_round():
    if lost == None:
        print(lost)
    else:
        playsound("C:/blagoje/opencv project/res/wow.wav")


def team_ace():
    if teamace == None:
        print(teamace)
    else:
        playsound("C:/blagoje/opencv project/res/wow.wav")
        

while True:
    won = pg.locateOnScreen("C:/blagoje/opencv project/res/won3.png",grayscale = True, confidence = 0.65)
    lost = pg.locateOnScreen("C:/blagoje/opencv project/res/lost2.png",grayscale = True, confidence = 0.65)
    teamace = pg.locateOnScreen("C:/blagoje/opencv project/res/TeamAce.png",grayscale = True, confidence = 0.65)
    won_round()
    lost_round()






    
