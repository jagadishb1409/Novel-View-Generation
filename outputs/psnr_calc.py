from math import log10, sqrt
import cv2
import numpy as np

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20+log10(max_pixel / sqrt(mse))
    return psnr

original = cv2.imread('left2.jpg')
compressed = cv2.imread('inpaint_NS.jpg',1)
compressed = cv2.resize(compressed,(472,631))
val = PSNR(original,compressed)
print(f"PSNR Value is {val} dB")



