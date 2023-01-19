import cv2
import numpy as np
import random

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

for j in range(0, int(src.size / 10)):  # 전체 픽셀의 10%에 해당하는 값
    x = random.randint(0, src.shape[1] - 1)  # 가로축 좌푯값
    y = random.randint(0, src.shape[0] - 1)  # 세로축 좌푯값

    src[x, y] = (j % 2) * 255  # 잡음을 검정색 또는 흰색으로

print(type(src))
dest1 = cv2.GaussianBlur(src, (0, 0), 1)
dest2 = cv2.medianBlur(src, 3)  # (3, 3)

cv2.imshow('gaussian', dest1)
cv2.imshow('median', dest2)
cv2.imshow('src + noise', src)
cv2.waitKey()
cv2.destroyAllWindows()