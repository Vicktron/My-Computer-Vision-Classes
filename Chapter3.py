import cv2 as cv
import numpy as np

img = cv.imread('Resources/Ex.jpg')
print(img.shape)

imgResize = cv.resize(img, (400, 400))
cv.imshow('image', img)

imgCropped = img[0:200, 200:500]

cv.imshow('image Resize', imgResize)
cv.imshow('image Cropped', imgCropped)



cv.waitKey(0)