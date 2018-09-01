import cv2
import numpy as np
img=cv2.imread('D:\\26\\cp.jpg')
print (img.shape)#行数，列数，通道元组数
print (img.size)#图像像素数目
print (img.dtype)#图像数据类型
