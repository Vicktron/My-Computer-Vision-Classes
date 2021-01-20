import cv2
import numpy as np

print('Success')

# Reading Image files
# img = cv2.imread('Resources/Dream.jpg')
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# Reading Video Files
# vid = cv2.VideoCapture('Resources/Daddy.mp4')
# while True:
#     success, img = vid.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(10000) & 0xFF == ord('q'):
#         break

# Camera/WebCam
vid = cv2.VideoCapture(0)
vidGray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
vid.set(3, 640)  # Width
vid.set(4, 480)  # Height
vid.set(10, 100)
while True:
    success, img = vid.read()
    cv2.imshow('Video', img)
    cv2.imshow("Video Gray", vidGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
