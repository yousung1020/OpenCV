import cv2

print(cv2.__version__)

img = cv2.imread('lenna.bmp') # image read 함수

cv2.namedWindow('image') # 이름 붙여진 창
cv2.imshow('image', img) # image show
cv2.waitKey() # 사용자로부터 키보드 입력 기다림
# cv2.destroyAllWindows()
cv2.destroyWindow("image")