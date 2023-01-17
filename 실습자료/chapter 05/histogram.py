import cv2
# import matplotlib.pyplot as plt
import numpy as np

def calcGrayHist(img):# 히스토그램을 만들어주는 사용자 정의 함수
    channels = [0]
    histsize = [256]  # bin의 갯수 (x축)
    histRange = [0, 256]  # 256 미만

    h = cv2.calcHist([img], channels, None, histsize, histRange)

    return h

def getGrayHistImage(h):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    for x in range(256):
        p1 = (x, 100)  # point의 첫 글자
        p2 = (x, 100 - int((h[x, 0] / np.max(h)) * 100))
        cv2.line(imgHist, p1, p2, 0)

    return imgHist

def histogram_stretching(src):
    G_min = float(np.min(src))  # uint8 자료형을 실수형으로 변환
    G_max = float(np.max(src))

    dest = ((src - G_min) / (G_max - G_min) * 255.).astype(np.uint8)

    return dest

src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)
dest = histogram_stretching(src)
dest2 = cv2.equalizeHist(src)

h1 = calcGrayHist(src)
h2 = calcGrayHist(dest)
h3 = calcGrayHist(dest2)

cv2.imshow('Org', src)
cv2.imshow('Org. Histogram', getGrayHistImage(h1))
cv2.imshow('Result', dest)
cv2.imshow('Result Hist', getGrayHistImage(h2))
cv2.imshow('Eq', dest2)
cv2.imshow('Eq Hist', getGrayHistImage(h3))
cv2.waitKey()
cv2.destroyAllWindows()

# plt.bar(range(256), np.transpose(h)[0])
# plt.grid(True)
# plt.show()