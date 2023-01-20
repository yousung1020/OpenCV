import cv2

cap = cv2.VideoCapture('vtest.avi')

hog = cv2.HOGDescriptor()  # 클래스 호출을 통해 객체 생성

# SVM: 머신러닝 기술 이름
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()  # 프레임을 읽어서 반환
    # ret: true / false, true: 동영상 frame을 정상적으로 읽었을 때, false: 비정상적으로 읽었을 때
    if not ret:
        break

    detected, _ = hog.detectMultiScale(frame)
    for (x, y, w, h) in detected:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

    cv2.imshow('CCTV', frame)
    if cv2.waitKey(10) == 27:  # 10: ascii 코드로 esc키를 의미, esc키를 누르면 waitKey 함수는 27 반환
        break

cv2.destroyAllWindows()