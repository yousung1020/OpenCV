import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

dest = cv2.add(src, 100)

cv2.imshow('source', src)
cv2.imshow('destination', dest)
cv2.waitKey()
cv2.destroyAllWindows()