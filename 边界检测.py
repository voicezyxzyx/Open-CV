#Canny 边缘检测
import cv2
import numpy as np
from matplotlib import pyplot as plt#matplotlib为python的一个2D绘图库
img = cv2.imread('D:\\26\\cp.jpg',0)
edges = cv2.Canny(img,100,200)#第二个参数为最小阈值，第三个参数为最大阈值（即为线条的复杂度）

plt.subplot(121),plt.imshow(img,cmap = 'gray')#选颜色

#在matplotlib下，一个Figure对象可以包含多个子图（Axes），可以使用subplot()快速绘制    subplot(numRows, numCols, plotNum)
#图表的整个绘图区域被分成numRows行和numCols列，plotNum参数指定创建的Axes对象所在的区域，如何理
#解呢？如果numRows ＝ 3，numCols ＝ 2，那整个绘制图表样式为3X2的图片区域，用坐标表示为（1，1）
#，（1，2），（1，3），（2，1），（2，2），（2，3）。这时，当plotNum ＝ 1时，表示的坐标为（1，
#3），即第一行第一列的子图；看代码:
#import numpy as np
#import matplotlib.pyplot as plt
#plt.subplot(221) //分成2x2，占用第一个，即第一行第一列的子图
#plt.subplot(222)//分成2x2，占用第二个，即第一行第二列的子图
#plt.subplot(212)//分成2x1，占用第二个，即第二行
#plt.show()

plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
