import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'SimHei'  #显示中文

c = [0,0.91,1.70,2.62,3.55,4.10,5.21,8.58,12.00,13.59,17.17]
n = [1.3325,1.3358,1.3380,1.3410,1.3440,1.3462,1.3492,1.3578,1.3621,1.3639,1.3696]
n_data = [1.3379,1.3417,1.3450,1.3496,1.3526,1.3551,1.3573,1.3643]               #你所测得的折光率数据，需要填入自己的数据，这里的数据是瞎编的

z =  np.polyfit(c,n,1)         #拟合参数，返回值为kx+b中的k与b。
n_c = np.poly1d(z)           #形成多项式
n_new = n_c(c)

print(n_c)                     #输出kx+b数值

for i in n_data:                     #根据拟合曲线计算浓度
    print( (i - z[1]) / z[0] )


plt.plot(c,n,".")              #绘制散点图
plt.plot(c,n_new)              #绘制直线
plt.xlabel("浓度")             #设置坐标轴标签
plt.ylabel("折光率")
plt.show()

