import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Noisedata\\testing.png')
b,g,r = cv2.split(img)           # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb

# Denoising
dst = cv2.fastNlMeansDenoising(img,None,10,7,21)

b,g,r = cv2.split(dst)           # get b,g,r
rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

#plt.subplot(211),plt.imsave('Denoise\\seg1.png',rgb_img)
plt.subplot(212),plt.imsave('Denoise\\seg2.png',rgb_dst)
#plt.save()
