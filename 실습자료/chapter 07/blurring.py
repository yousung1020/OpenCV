import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

for ksize in (3, 5, 7):
    dest = cv2.blur(src, (ksize, ksize))

    txt = "Mean: (%d x %d)" % (ksize, ksize)

    cv2.putText(dest, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 2, cv2.LINE_AA)
    #  1.0: 폰트 스케일, 255: 폰트 색, 2: 선 타입

    cv2.imshow('result', dest)
    cv2.waitKey()

cv2.destroyAllWindows()