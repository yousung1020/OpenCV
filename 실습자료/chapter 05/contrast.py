import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# s = 2.0
# dest = cv2.multiply(src, s)  # 모든 픽셀 값에 s만큼 곱함

alpha = 1.0
# (수식) dest = src + ( src(x, y) - 128 ) * alpha
dest = np.clip(src + (src -128.) * alpha, 0, 255).astype(np.uint8) # uint <-- unsigned integer

cv2.imshow('src', src)
cv2.imshow('destination', dest)
cv2.waitKey()
cv2.destroyAllWindows()