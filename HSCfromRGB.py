import os, sys
import cv2
import numpy as np

if len(sys.argv) == 4:
    rgb_color = np.uint8([[[int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]]])
    hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_BGR2HSV)
    print("HSV COLOR =====>", hsv_color)
else:
    print("Usage:", sys.argv[0], "red green blue")