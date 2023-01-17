import cv2

src1 = cv2.imread('aero2.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('camera.bmp', cv2.IMREAD_GRAYSCALE)

#  add(), addWeighted()

dest = cv2.add(src1, src2)
dest1 = cv2.addWeighted(src1, 0.1, src2, 0.9, 0.0)
dest2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dest3 = cv2.addWeighted(src1, 0.9, src2, 0.1, 0.0)

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('dest', dest)
cv2.imshow('dest1', dest1)
cv2.imshow('dest2', dest2)
cv2.imshow('dest3', dest3)

cv2.waitKey()
cv2.destroyAllWindows()