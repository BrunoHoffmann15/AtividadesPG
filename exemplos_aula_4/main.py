import numpy as np
import cv2 as cv

img = cv.imread('blue_tiles.jpg')

cv.imshow('Hello OpenCV', img)

k = cv.waitKey(0)