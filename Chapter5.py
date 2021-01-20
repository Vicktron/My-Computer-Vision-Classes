import cv2 as cv
import numpy as np

img = cv.imread('Resources/wallpaper245.jpg')
img = cv.resize(img, (500, 720))

width, height = 50, 50

pts1 = np.float32([[271, 408], [415, 408], [425, 644], [271, 647]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('Image', img)
cv.imshow('Image2', imgOutput)


cv.waitKey(0)