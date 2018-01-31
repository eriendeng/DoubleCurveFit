# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

class show_img():

    def __init__(self):
        global point
        self.pic = plt.figure()
        point = []

    def show(self,dir):
        img = plt.imread(dir)
        plt.imshow(img)
        self.pic.canvas.mpl_connect('button_press_event', self.onClick)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title('点击选择曲线上的点，完成后关闭窗口')

        return plt.show()


    def onClick(self,event):
        global ix, iy
        ix, iy = event.xdata, event.ydata
        if (ix!=None and iy!=None):
            point.append((ix, iy))
            print('now = (%s,%s)\n' % (ix, iy), point)
            plt.scatter(ix, iy, s=10,edgecolors='white')
        else:
            print('point not exist!')

        return plt.show()


class solution():
    def __init__(self,x,y,title):
        self.xarray = x
        self.yarray = y
        self.pic = plt.figure()
        self.title = title


    def show(self,dir):
        img = plt.imread(dir)
        plt.imshow(img)
        for array in point:
            plt.scatter(array[0],array[1],s=10)
        plt.plot(self.xarray,self.yarray)
        plt.title(self.title)

        return plt.show()



def f_2(x, A, B, C):
    return A*x*x + B*x + C


def figure():
    _x = []
    _y = []
    for array in point:
        _x.append(array[0])
        _y.append(array[1])
    A, B, C = optimize.curve_fit(f=f_2, xdata=_x, ydata=_y)[0]
    print(optimize.curve_fit(f=f_2, xdata=_x, ydata=_y))
    x2 = np.arange(np.min(_x), np.max(_x), 0.01)
    y2 = A * x2 * x2 + B * x2 + C
    title = str(A)+'x^2+'+str(B)+'x+'+str(C)
    return solution(x2,y2,title)



if __name__ == "__main__":
    dir = input('请输入图片绝对路径:')
    show_img().show(dir)
    figure().show(dir)


#r'C:\Users\Administrator\Desktop\222.jpg'