import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

# MODIFY this when sir mentions this again

# MOST PROBABLY WONT EVEN HAVE TO

def diff_eulerbackward(dydx,x0,y0,x1,step):
    # integrates and give data points between x0 and x1 for the solution of a given dydx
    # x0 y0 is the given intial solution, step is the delta X  used in each iteration 
    return

def dydx (x):
    return (m.sin(x) + (x**2))

def y(x):
    return (-m.cos(x)+((x**3)/3))
a = 0
b = 1
x0 = 0
y0 = -1

X,Y = diff_eulerbackward(dydx,a,b,x0,y0,0.05)
X1,Y1 = lib.fx_graphdata(y,a,b,100)
plt.plot(X,Y,'r-')
plt.plot(X1,Y1,'b-')
plt.show()