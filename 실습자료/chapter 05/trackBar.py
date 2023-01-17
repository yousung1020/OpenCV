import cv2

def update(value):
    dest = cv2.add(src, value)  # add 함수는 포화 기능이 내장
    cv2.imshow('result', dest)

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('result')
cv2.createTrackbar('Brightness', 'result', 0, 100, update)
update(0)

cv2.waitKey()
cv2.destroyAllWindows()
