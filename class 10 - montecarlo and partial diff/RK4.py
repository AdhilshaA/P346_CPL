import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

# MODIFY this when sir mentions this again



def diff_RK4(dydx,x0,y0,x1,dx):
    # integrates and give data points between x0 and x1 for the solution of a given dydx
    # x0 y0 is the given intial solution, step is the delta X  used in each iteration 

    datX = [x0]
    datY = [y0]
    while x0 < x1:
        k1 = dx * dydx(y0,x0)
        k2 = dx * dydx((y0 + (k1/2)),(x0 + (dx/2)))
        k3 = dx * dydx((y0 + (k2/2)),(x0 + (dx/2)))
        k4 = dx * dydx((y0 + k3),(x0 + dx))
        y0 = y0 + ((k1 + k4 + (2*(k2 + k3)))/6)
        x0 += dx
        datX.append(x0)
        datY.append(y0)
        
    return datX, datY

def dydx (y,x):
    return (y - (x**2) + 1)

def y(x):
    return ((x**2) + (2*x) + 1 + (-0.5*m.exp(x)))

x1 = 4
x0 = 0
y0 = 0.5
X,Y = diff_RK4(dydx,x0,y0,x1,0.5)
X1,Y1 = lib.fx_graphdata(y,x0,x1,20)

plt.plot(X1,Y1,'b-')
plt.plot(X,Y,'ro',ms=2)

plt.show()