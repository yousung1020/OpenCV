import cv2

img1 = cv2.imread('lenna.bmp')

img2 = img1[200:400, 200:400, 0:3]  # 공유
img3 = img1[200:400, 200:400, 0:3].copy()  # 복사

img2 += 50  # 모든 픽셀값을 50만큼 증가

cv2.imshow('girl', img1)
cv2.imshow('face1', img2)
cv2.imshow('face2', img3)

cv2.waitKey()
cv2.destroyAllWindows()

print(img2)
print(img1)