import cv2
import numpy as np

img = cv2.imread(r'/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/2D_image_converted_rotated.jpg', 0)
print(img.shape)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] >= 225 and img[i, j] <= 255:
            img[i, j] = 255
        else:
            img[i, j] = 0
# cv2.imshow('test', img)
cv2.imwrite('outputs/mask2-n.jpg', img)
cv2.waitKey(0)

