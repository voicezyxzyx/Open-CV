import cv2
import numpy as np
img1=cv2.imread('D:\\26\\jing1.jpg')
img2=cv2.imread('D:\\26\\jing2.jpg')#两张图片大小、格式、像素必须一样，名字必须为中文
img_mix = cv2.addWeighted(img1, 0.6, img2, 0.4,0)#设置两张图片的清晰度，并混合
cv2.imshow('img_mix', img_mix)
cv2.waitKey(0)
# cv2.destroyAllWindow()