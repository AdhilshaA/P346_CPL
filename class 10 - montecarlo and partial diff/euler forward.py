import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

def diff_eulerforward(dydx,x0,y0,x1,dx):
    # integrates and give data points between x0 and x1 for the solution of a given dydx
    # x0 y0 is the given intial solution, dx is the delta X  used in each iteration 

    datX = [x0]
    datY = [y0]
    while x0 < x1:
        y0 = y0 + dx*(dydx(y0,x0))
        x0 += dx
        datX.append(x0)
        datY.append(y0)

    return datX, datY

def dydx (y,x):
    return (m.sin(x) + (x**2))

def y(x):
    return (-m.cos(x)+((x**3)/3))
x1 = 1
x0 = 0
y0 = -1

X,Y = diff_eulerforward(dydx,x0,y0,x1,0.05)
X1,Y1 = lib.fx_graphdata(y,x0,x1,100)
plt.plot(X,Y,'ro',ms=2)
plt.plot(X1,Y1,'b-')
plt.show()