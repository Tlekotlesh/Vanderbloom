import math
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import seaborn as sns
sns.set_style('whitegrid')

csfont = {'fontname':'Times New Roman'}
hfont = {'fontname':'Helvetica'}
shift = 273.15

xdata = [0, 220, 404, 591, 711, 1381, 1683, 1786, 1968, 2104, 2310, 2599, 2918, 3073, 3171, 3300, 3412, 3707, 3805, 4225, 4547, 4650, 4797, 5188] #[0.2233, 0.2916, 0.4064, 0.4973, 0.6, 0.6945, 0.7863, 0.8934, 0.9852, 1.0721, 1.1634, 1.269, 1.3708]
Xdata = np.array(xdata)
ydata = [60, 61, 63, 64, 65, 69, 72, 72, 74, 75, 77, 79, 81, 82, 83, 84, 85, 87, 88, 92, 94, 95, 96, 100]

Ydata = np.array(ydata) - 60

eydata = [0, 3, 4, 7, 7, 16, 18, 20, 22, 23, 25, 27, 31, 33, 34, 36, 37, 40, 41, 45, 49, 50, 51, 54]

eYdata = np.array(eydata)


#plt.title('График зависимости силы тока от продольного напряжения', size=15, **csfont)
plt.xlabel('t, мин', size=20, **csfont)  # тут
plt.ylabel('V, мл', size=20, **csfont)






plt.errorbar(Xdata, Ydata, color='orange', yerr= 0.5, fmt='.', capsize = 2, label='сахар')
L = np.linspace(0, 5200, 100)


def func(x, a):
    return a * x


popt, covt = curve_fit(func, Xdata, Ydata, maxfev = 1000)

print(popt[0])
print(np.sqrt(np.diag(covt))[0])
#plt.plot(L,(72-69)/(1684-1381)*L , color='green')
plt.plot(L, func(L, *popt), linestyle='dashed', color='red', label='аппроксимация точек для сахара')

#popt2, covt2 = curve_fit(func, Xdata, eYdata, maxfev = 1000)
#plt.errorbar(Xdata, eydata, color='blue', yerr= 0.5, fmt='.', capsize = 2, label='вода')
#plt.plot(L, func(L, *popt2), linestyle='dashed', color='green', label='аппроксимация точек для воды')

#popt3, covt3 = curve_fit(func, Xdata, abs(eYdata-Ydata), maxfev = 1000)


#plt.errorbar(list(Xdata), list(abs(eYdata-Ydata)), color='blue', yerr= 0.5*(2**(0.5)), fmt='.', capsize = 2, label='точки дивергенции объемов' )
#plt.plot(L, func(L, *popt3), linestyle='dashed', color='purple', label='line 8')
#Второй фит:

#X2 = xdata[l:r]
#Y2 = ydata[l:r]
#X2 = np.array(X2)
#Y2 = np.array(Y2) + shift

#popt, covt = curve_fit(func, X2, Y2, maxfev = 1000)


'''L2 = np.linspace(Xdata[l], Xdata[r], 100)
print(popt[0])
print(np.sqrt(np.diag(covt))[0])
plt.plot(L2, func(L2, *popt), linestyle='dashed', color='black')

X3 = xdata[r:]

Y3 = ydata[r:]
X3 = np.array(X3)
Y3 = np.array(Y3) + shift

popt, covt = curve_fit(func, X3, Y3, maxfev = 1000)

L3 = np.linspace(Xdata[r], 1470, 100)'''
print(popt*10**(-6)/(60*1.647*10**(-2)))
print(np.sqrt(np.diag(covt))*10**(-6)/(60*1.647*10**(-2)))
plt.plot(L, func(L, *popt), linestyle='dashed')


plt.axhline(y=0, xmin = -0.2, xmax = 0.4, color='black')
plt.axhline(y=0, xmin = 0.05, color='black')
plt.axvline(x=0, ymin = 1, ymax = -1, color='black')

for i in range(len(Ydata)):
    print(Xdata[i], eYdata[i])
plt.legend(fontsize=13
           )
plt.show()

#EXSTRA DATA
eydata = [0, 3, 4, 7, 7, 16, 18, 20, 22, 23, 25, 27, 31, 33, 34, 36, 37, 40, 41, 45, 49, 50, 51, 54]

