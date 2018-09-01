import numpy as np
import cv2
a="D:\\python\\pycharm文件\\人脸识别\\cv2\\video.avi"
cap = cv2.VideoCapture(a)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    cv2.imshow('frame',gray)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
