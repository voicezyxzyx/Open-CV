#图像保存，复制
#保存图像很简单，直接用cv2.imwrite即可。
#cv2.imwrite("D:\\cat2.jpg", img)
#第一个参数是保存的路径及文件名，第二个是图像矩阵。其中，imwrite()有个可选的第三个参数，如下：
#cv2.imwrite("D:\\cat2.jpg", img，[int(cv2.IMWRITE_JPEG_QUALITY), 5])
#第三个参数针对特定的格式： 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。
#对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3：
import cv2
import numpy as np

img = cv2.imread("D:\\26\\cp.jpg")#读入图像
emptyImage = np.zeros(img.shape, np.uint8)
emptyImage2 = img.copy()
emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#设置为灰色图像

cv2.imshow("EmptyImage", emptyImage)
cv2.imshow("Image", img)
cv2.imshow("EmptyImage2", emptyImage2)
cv2.imshow("EmptyImage3", emptyImage3)
cv2.imwrite("cp.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("cp.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite("cp.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite("cp.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.waitKey(0)
cv2.destroyAllWindows()