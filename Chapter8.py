import cv2 as cv
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailble = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailble:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                               None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageblank = np.zeros((height, width, 3), np.uint8)
        hor = [imageblank] * rows
        hor_con = [imageblank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours, heirachy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if objCor == 3: objectType = 'Triangle'
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = 'Sqaure'
                else: objectType = 'Rectangle'
            elif objCor >= 8: objectType = 'Circle'
            else: objectType = 'None'

            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, objectType, (x+(w//2) - 10, y + (h//2)-10),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


# path = 'Resources/shapes.png'
# img = cv.VideoCapture(0)
# imgContour = img.copy()
#
# imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv.Canny(imgBlur, 50, 50)
#
# getContours(imgCanny)
#
# imgBlank = np.zeros_like(img)
# imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
#                              [imgCanny, imgContour, imgBlank]))
#
# cv.imshow('Image Stacked', imgStack)

cam = cv.VideoCapture(0)
camGray = cv.cvtColor(cam, cv.COLOR_BGR2GRAY)



cv.waitKey(0)