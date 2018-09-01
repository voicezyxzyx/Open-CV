import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# 定义编解码器并创建videowriter对象
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        # 写翻转帧
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 如果工作完成，发布一切
cap.release()
out.release()
cv2.destroyAllWindows