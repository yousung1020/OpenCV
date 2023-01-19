import cv2

# 원본 영상
src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

sigma = 1

# 언샤프 영상(=부드러워진 영상)

blurred = cv2.GaussianBlur(src, (0, 0), sigma)  # 원본 영상, 마스크 위치, 시그마
alpha = 5.0

# 샤프닝된 영상(=날카로워진 영상)

dest = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)

cv2.imshow('Original', src)
cv2.imshow('unsharp', blurred)
cv2.imshow('sharp', dest)
cv2.waitKey()
cv2.destroyAllWindows()