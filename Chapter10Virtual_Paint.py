import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

vid = cv.VideoCapture(0)
vid.set(3, frameWidth)  # Width
vid.set(4, frameHeight)  # Height
vid.set(10, 150)

myColors = [[13, 32, 90, 255, 0, 255]]

def findColor(img):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    cv.imshow('img', mask)

while True:
    success, img = vid.read()
    cv.imshow('Result', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break