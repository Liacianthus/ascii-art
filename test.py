# GrayScale 로 변환
# ★ NEED ★
#   * opencv-python
#   * numpy

import cv2

img = cv2.imread("img\ROKMC_dog.jpg", cv2.IMREAD_GRAYSCALE)  # GrayScale 로 이미지 파일 읽어오기
# print(type(img))

# 픽셀 접근 ( grayScale 은 0~255 까지의 값을 가짐)
pixel_value = []

(height, width) = img.shape  # 전체 사진의 크기를 가져옴
# print(img[0,0]) # 사진의 첫 픽셀값
# print(img[height - 1, width - 1])  # 사진의 마지막 픽셀값

for y in range(height):  # 모든 픽셀에 대한 grayScale을 가져옴
    t = []
    for x in range(width):
        t.append(img[y, x])
    pixel_value.append(t)

# for y in range(height):  # pixel_value 출력
#     for x in range(width):
#         print(pixel_value[y][x], end=" ")
#     print()


cv2.imshow("ROKMC_DOG", img)  # 사진 보여주기
cv2.waitKey()
cv2.destroyAllWindows()
