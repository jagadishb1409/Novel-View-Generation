# import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/2D_image_converted_rotated.jpg')     # input
mask = cv2.imread('/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/mask2-n.jpg', 0)  # mask

dst_TELEA = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA) # for Alexandru Telea's Algorithm
dst_NS = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS) # for Navier-Stokes's Algorithm

plt.subplot(221), plt.imshow(img)
plt.title('degraded image')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('mask image')
plt.subplot(223), plt.imshow(dst_TELEA)
plt.title('TELEA Method')
plt.subplot(224), plt.imshow(dst_NS)
plt.title('NS Method')

cv2.imwrite('/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/Inpaint_telea-h.jpg', dst_TELEA)
cv2.imwrite('/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/Inpaint_NS-h.jpg', dst_NS)
plt.tight_layout()
plt.show()
