import cv2
import numpy as np

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

print(digits.shape)  # height: 1000, width: 2000
h, w = digits.shape[:2]

cells = []
for row in np.vsplit(digits, h // 20):
    # print(row.shape): (20, 2000)
    # 열: Column
    for col in np.hsplit(row, w // 20):
        # col.shape: (20, 20)
        cells.append(col)

cells = np.array(cells)  # list -> ndarray

print(cells.shape)
# 5000: 사진 갯수, (20, 20): 가로 세로 픽셀 갯수

train_images = cells.reshape(5000, 400).astype(np.float32)  # 1차원의 벡터로 변환
train_labels = np.repeat(np.arange(0, 10), len(train_images) / 10)

# Training K-NN

model = cv2.ml.KNearest_create()  # k-nn 객체 생성
model.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

# 마우스로 숫자 적는 기능 구현

oldX, oldY = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldX, oldY  # 지역 변수 -> 전역 변수

    # L: Left, B: Botton
    if event == cv2.EVENT_LBUTTONDOWN:
        oldX, oldY = x, y

    elif event == cv2.EVENT_LBUTTONUP:  # 마우스를 떼었을 때
        oldX, oldY = -1, -1  # 초기화

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldX, oldY), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldX, oldY = x, y
            cv2.imshow('Window', img)

# 도화지 준비

img = np.zeros((400, 400), np.uint8)
cv2.imshow('Window', img)
cv2.setMouseCallback('Window', on_mouse)

# 필기체 숫자 인식하기

while True:
    c = cv2.waitKey()
    if c == 27:  # esc키를 눌렀을 때
        break

    elif c == 32:  # space bar를 눌렀을 때
        img_resize = cv2.resize(img, (20, 20), interpolation=(cv2.INTER_AREA))

        img_flatten = img_resize.reshape(-1, 400).astype(np.float32)

        # res: 예측한 숫자값

        ret, res, _, _ = model.findNearest(img_flatten, 3)
        print(int(res[0, 0]))

        img.fill(0)  # 숫자 인식이 끝났으면,, 검정색으로 초기화

        cv2.imshow('Window', img)
cv2.destroyAllWindows()