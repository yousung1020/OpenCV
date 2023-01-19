import cv2
import numpy as np

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

# split: 쪼개다
bgr_planes = cv2.split(src)

cv2.imshow('blue', bgr_planes[0])
cv2.imshow('green', bgr_planes[1])
cv2.imshow('red', bgr_planes[2])
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()