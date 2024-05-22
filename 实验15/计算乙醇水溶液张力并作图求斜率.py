import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
plt.rcParams['font.family'] = 'SimHei'  #显示中文

Delta_p = [0.692,0.529,0.461,0.416,0.365,0.331,0.314,0.290,0.261]    #测定的最大压力差数据，修改为你的数据
water_p = 0.0728                    #水的表面张力，需要根据实验温度进行修改，数据网上可查询
c = [1.111,2.876,4.408,6.544,7.9372,9.098,10.119,13.370]  #此为上一步所计算出的乙醇水溶液浓度，修改为你的数据
gamma = []
grad_gamma = []

for i in range(1,len(Delta_p)):                   #计算乙醇溶液的表面张力
    gamma.append(((Delta_p[i] / Delta_p[0]) * water_p))

def fun1(x,a,k,b):          #拟合函数模型,最好不要修改。
    return  a*np.log(1+k*x) + b

def grad(x,a,k,b,function):                   #使用数值解法求出斜率
    return (function(x + 0.0001,a,k,b) - function(x,a,k,b)) / 0.0001

c_new = np.arange(0,20,0.1)

popt,pcov = scipy.optimize.curve_fit(fun1,c,gamma)          #拟合参数a,k,b

for i in c:                                 #计算斜率
    grad_gamma.append(grad(i,*popt,fun1))

#输出结果
print("斜率为:",grad_gamma)         
print("a,k,b的值为:",popt)
print("乙醇表面张力为:",gamma)

plt.plot(c,gamma,".")
plt.plot(c_new,fun1(c_new,*popt))
plt.title("张力-浓度关系图")
plt.xlabel("浓度")
plt.ylabel("张力")
plt.show()
