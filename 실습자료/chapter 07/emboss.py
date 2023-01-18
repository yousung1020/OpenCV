import cv2
import numpy as np

src = cv2.imread("rose.bmp", cv2.IMREAD_GRAYSCALE)
# src2 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

emboss = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]], np.float32)

dest = cv2.filter2D(src, -1, emboss, delta=128)

cv2.imshow('src', src)
cv2.imshow('dest', dest)

cv2.waitKey()
cv2.destroyAllWindows()