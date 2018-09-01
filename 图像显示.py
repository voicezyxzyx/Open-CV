import cv2
img = cv2.imread("D:\\26\\cp.jpg")#读入图片
cv2.imshow("Image", img)#显示图像，Image是窗口的名字，Img是图像的名字
cv2.waitKey(0)#cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果按下任意键，这个函数会返回按键的 ASCII 码值，程序将会继续运行。如果没有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限期的等待键盘输入。
cv2.destroyAllWindows()#cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口。如果你想删除特定的窗口可以使用 cv2.destroyWindow()，在括号内输入你想删除的窗口名。