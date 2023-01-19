import cv2

# B-G-R 색상 모델
src = cv2.imread('pepper.bmp', cv2.IMREAD_COLOR)

# YCrCb 색상 모델로 변환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

rgb_planes = cv2.split(src)
blue_plane = rgb_planes[0]

ycrcb_planes = cv2.split(src_ycrcb)
ycrcb_planes = list(ycrcb_planes) # tuple -> list

ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])  # y채널 정보

dest_ycrcb = cv2.merge(ycrcb_planes)

dest_rgb = cv2.cvtColor(dest_ycrcb, cv2.COLOR_YCrCb2BGR)
blue_plane2 = cv2.split(dest_rgb)[0]

cv2.imshow('src', src)
cv2.imshow('blue 1', blue_plane)
cv2.imshow('blue 2', blue_plane2)
cv2.imshow('dest', dest_rgb)
cv2.waitKey()
cv2.destroyAllWindows()