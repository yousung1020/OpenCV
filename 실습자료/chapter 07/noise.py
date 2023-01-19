import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# cv2.randn()

stddev = 10  # 표준편차
n = np.zeros(src.shape, np.int32)
cv2.randn(n, 0, stddev)

dest = cv2.add(src, n, dtype=cv2.CV_8UC1)

result1 = cv2.GaussianBlur(dest, (0, 0), 5)

# bilateralFilter: 양방향 필터
result2 = cv2.bilateralFilter(dest, -1, 10, 5)

cv2.imshow('gaussian', result1)
cv2.imshow('bileteral', result2)
cv2.imshow('original', src)
cv2.imshow('+noise', dest)
cv2.waitKey()
cv2.destroyAllWindows()