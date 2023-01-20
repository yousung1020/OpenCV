import cv2
import numpy as np

img = cv2.imread('circuit.bmp', cv2.IMREAD_COLOR)

tmp = cv2.imread('crystal.bmp', cv2.IMREAD_COLOR)

img = img + (50, 50, 50)  # blue, green, red

noise = np.zeros(img.shape, np.int32)
cv2.randn(noise, 0, 10)  # 평균이 0, 표준편차가 10

img = cv2.add(img, noise, dtype=cv2.CV_8UC3)

# SQ DIFF = Squared Difference
# Nomerd = Normalized
result = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)

# Loc = Location
maxv, minv, minLoc, maxLoc = cv2.minMaxLoc(result)

# th = template height, th = template width
(th, tw) = tmp.shape[:2]

print(img.shape)
print(tmp.shape)
print(maxLoc)
print(th, tw)

# (0, 0, 255): (B, G, R) --> 빨간색, 2: 직사각형을 그릴 때 선의 두께
cv2.rectangle(img, maxLoc, (maxLoc[0] + tw, maxLoc[1] + th), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('template', tmp)
cv2.waitKey()
cv2.destroyAllWindows()