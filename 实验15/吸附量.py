import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'SimHei'  #显示中文

T = 298.15         #温度
R = 8.314
Avogadro = 6.02E23      #阿伏伽德罗常熟
grad_gamma = [-0.00526, -0.00363, -0.00286, -0.00221, -0.00192, -0.00174, -0.0016, -0.00128]
c = [1.111,2.876,4.408,6.544,7.9372,9.098,10.119,13.370]
tao = []
c_tao = []

for i in range(len(c)):     #计算吸附量和c/tao
    ans = -(c[i] / (R * T) * grad_gamma[i] )
    tao.append(ans)
    c_tao.append(c[i]/ans)
    
z =  np.polyfit(c,c_tao,1)         #拟合参数，返回值为kx+b中的k与b。
zz = np.poly1d(z)           #形成多项式
c_tao_new = zz(c)

print("吸附量为:",tao)
print("直线方程为:",zz)
print("饱和吸附量为:",1/z[0])
print("面积为:",1/(z[0]*Avogadro))

plt.plot(c,c_tao,".")
plt.plot(c,c_tao_new)
plt.show()

