import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# dest1 = src + 100
dest1 = cv2.add(src, 100)
# dest2 = src - 100
dest2 = cv2.subtract(src, 100)

cv2.imshow('source', src)
cv2.imshow('add', dest1)
cv2.imshow('subtract', dest2)
cv2.waitKey()
cv2.destroyAllWindows()