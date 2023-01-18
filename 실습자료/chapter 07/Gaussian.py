import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

for sigma in range(1, 5):
    dest = cv2.GaussianBlur(src, (0, 0), sigma, )

    txt = "Sigma = %d" % (sigma)
    cv2.putText(dest, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('Result', dest)
    cv2.waitKey()

cv2.destroyAllWindows()