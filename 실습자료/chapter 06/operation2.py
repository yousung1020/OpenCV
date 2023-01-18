import cv2

src1 = cv2.imread('diff1.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('diff2.bmp', cv2.IMREAD_GRAYSCALE)

dest1 = cv2.add(src1, src2)
dest2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dest3 = cv2.subtract(src1, src2)
dest4 = cv2.absdiff(src1, src2)


cv2.imshow('add', src1)
cv2.imshow('add weighted', src2)
cv2.imshow('subtract', dest3)
cv2.imshow('Abs Diff', dest4)

cv2.waitKey()
cv2.destroyAllWindows()
