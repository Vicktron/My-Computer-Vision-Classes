import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img)
# img[:] = 255, 0, 0  # Changes the color from black  to Blue

cv.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv.putText(img, 'OPENCV ', (300, 200), cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv.imshow('image', img)

cv.waitKey(0)