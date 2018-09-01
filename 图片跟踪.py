import cv2
import numpy as np
a="D:\\26\\video.avi"
cap = cv2.VideoCapture(a)
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    # 转换到 HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
    lower_white=np.array([255,255,255])
    upper_white=np.array([255,255,255])
    # 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_white,upper_white)
    # 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关闭窗口
cv2.destroyAllWindows()



