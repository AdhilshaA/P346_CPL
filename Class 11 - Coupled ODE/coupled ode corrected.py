from tkinter.messagebox import YESNOCANCEL
import mylibrary as lib
import matplotlib.pyplot as plt
import math as m

def RK4_coupled(dydxlist,x0,y0list,x1,dx):

    if len(dydxlist) != len(y0list):
        return None
    x1 -= dx/2
    n = len(y0list)
    k1 = [0]*n
    k2 = [0]*n
    k3 = [0]*n
    k4 = [0]*n
    tempy0list = [0]*n

    datY = []
    for i in range(n):
        datY.append([y0list[i]])
    datX = [x0]

    while x0 < x1:
        for i in range(n):
            k1[i] = dx*dydxlist[i](y0list,x0)
        
        for i in range(n):
            tempy0list[i] = y0list[i] + (k1[i] / 2)
        for i in range(n):
            k2[i] = dx*dydxlist[i](tempy0list, (x0 + (dx/2)))

        for i in range(n):
            tempy0list[i] = y0list[i] + (k2[i] / 2)
        for i in range(n):
            k3[i] = dx*dydxlist[i](tempy0list, (x0 + (dx/2)))
            
        for i in range(n):
            tempy0list[i] = y0list[i] + k3[i]
        for i in range(n):
            k4[i] = dx*dydxlist[i](tempy0list, (x0 + dx))
        # print(k1,k2,k3,k4,'\n\n')

        for i in range(n):
            y0list[i] += ((k1[i] + (2 * k2[i]) + (2 * k3[i]) + (k4[i])) / 6)
        x0 += dx
        
        # print(y0list,x0,'\n\n')

        for i in range(n):
            datY[i].append(y0list[i])
        datX.append(x0)
    # print(datX,datY)
    return datX, datY


def f1(xvlist,t):
    return xvlist[1]

def f2(xvlist,t):
    return ((-0.1*xvlist[1]) - (1*xvlist[0]))

dydx = [f1,f2]

def dydx (y,x):
    return (y[0] - (x**2) + 1)

def y(x):
    return ((x**2) + (2*x) + 1 + (-0.5*m.exp(x)))

x1 = 4
x0 = 0
y0 = [0.5]
X,Y = RK4_coupled([dydx],x0,y0,x1,0.1)
X1,Y1 = lib.fx_graphdata(y,x0,x1,20)

plt.plot(X1,Y1,'b-') 
plt.plot(X,Y[0],'ro',ms=2)
plt.vlines(X,min(Y[0]),max(Y[0]))
plt.show()

# print(Y,'n')
# Y1 = []
# Y2 = []
# for i in range(len(Y)):
#     Y1.append(Y[i][0])
#     Y2.append(Y[i][1])
# print('red',Y1,'\n')
# print('blue',Y2,'\n')
# plt.plot(X,Y2,'bo',ms=2)
# plt.xlabel('red x, blue v')


def f1(xyzlist,t):
    return (10*(xyzlist[1]-xyzlist[0]))
def f2(xyzlist,t):
    return ((xyzlist[0] * (28 - xyzlist[2])) - xyzlist[1])
def f3(xyzlist,t):
    return ((xyzlist[0] * xyzlist[1]) - ((8/3)*xyzlist[2]))

flist = [f1,f2,f3]

fig = plt.figure()
ax = plt.axes(projection = "3d")
X,Y = RK4_coupled(flist,0,[1,0,1],25,0.03)
# print(Y)

# print(Y1,'\n')
# print(Y2,'\n')
# print(Y3,'\n')


ax.plot3D(Y[0],Y[1],Y[2],'-')

plt.show()

    




