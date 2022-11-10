import mylibrary as lib
import matplotlib.pyplot as plt
import math as m

#write interpolation

def shooting(f1,f2,x0,y0,x1,y1,dy0guess1,tolerance,step):
    datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,dy0guess1],x1,step)
    dyval1 = datY[0][-1]
    print(dyval1)
    if abs(dyval1 - y1) < tolerance:
        return datX,datY
    if dyval1 < y1:
        guess1side = -1
    else :
        guess1side = 1
    dy0guess2 = dy0guess1 + 1
    datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,dy0guess2],x1,step)
    dyval2 = datY[0][-1]
    print(dyval2)
    if dyval2 < y1:
        guess2side = -1
    else :
        guess2side = 1
    # if guess1side * guess2side != -1:
    #     pass
    newguess = dy0guess1 + (((dy0guess2 - dy0guess1)/(dyval1 - dyval2))*(y1 - dyval2))
    print('new g',newguess)
    datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,newguess],x1,step)
    plt.plot(datX,datY[0],'ro',ms=2)
    dyval1 = datY[0][-1]
    print('diff is',abs(dyval1-y1))
    print('the y val',dyval1)

    

    


def f1(l,x):
    return l[1]

def f2(l,x):
    return 2 * l[0]

def f_data(f,start,stop,number):
    # gives the graph data for y = a*x^b between start and stop with "number" no. of points
    step = (stop - start) / (number - 1)
    Xvalues = []
    Yvalues = []
    stop += step
    while start < stop:
        Xvalues.append(start)
        Yvalues.append(f(start))
        start += step
    return Xvalues, Yvalues

x0 = 0
y0 = 1.2
x1 = 1
y1 = 0.899
dy0guess1 = -1.5
tolerance = 0.0001
step = 0.1

def f(x):
    return ((0.157*m.exp((m.sqrt(2)*x))) + (1.043*m.exp((-1*m.sqrt(2)*x))))

shooting(f1,f2,x0,y0,x1,y1,dy0guess1,tolerance,step)
X,Y = f_data(f,0,1,100)
plt.plot(X,Y)
plt.show()
