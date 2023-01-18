import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

#  and, or, xor, not

dest1 = cv2.bitwise_and(src1, src2)
dest2 = cv2.bitwise_or(src1, src2)
dest3 = cv2.bitwise_xor(src1, src2)
dest4 = cv2.bitwise_not(src1)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dest1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dest2, 'gray'), plt.title('or')
plt.subplot(235), plt.axis('off'), plt.imshow(dest3, 'gray'), plt.title('xor')
plt.subplot(236), plt.axis('off'), plt.imshow(dest4, 'gray'), plt.title('not')

plt.show()