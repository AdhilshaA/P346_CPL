import mylibrary as lib
import matplotlib.pyplot as plt
import math as m

#write interpolation

def shooting(f1,f2,x0,y0,x1,y1,dy0guess1,tolerance,step):
    datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,dy0guess1],x1,step)
    yval1 = datY[0][-1]
    print(yval1)
    if abs(yval1 - y1) < tolerance:
        return datX,datY
    if yval1 < y1:
        guess1side = -1
    else :
        guess1side = 1

    dy0guess2 = dy0guess1 + 0.5   
    datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,dy0guess2],x1,step)
    yval2 = datY[0][-1]
    print(yval2)
    if yval2 < y1:
        guess2side = -1
    else :
        guess2side = 1

    while guess1side * guess2side != -1:
        if abs(y1-yval2) > abs(y1-yval1):
            dy0guess2 = dy0guess1 - 1.5*abs(dy0guess2-dy0guess1)
        else:
            dy0guess2 += abs(dy0guess2-dy0guess1)
        datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,dy0guess2],x1,step)
        yval2 = datY[0][-1]
        print(yval2)
        if yval2 < y1:
            guess2side = -1
        else :
            guess2side = 1
    print('guesses are {} and {} and yvals {} and {}'.format(dy0guess1,dy0guess2,yval1,yval2))

    # if guess1side * guess2side != -1:
    #     pass
    i = 0
    while True:
        newguess = dy0guess1 + (((dy0guess2 - dy0guess1)/(yval1 - yval2))*(y1 - yval2))
        i+=1
        datX,datY = lib.RK4_coupled([f1,f2],x0,[y0,newguess],x1,step)
        yvalnew = datY[0][-1]

        # print('the guesses {} and {}, the new guess is {} and yvalue is {}'.format(dy0guess1, dy0guess2, newguess,yvalnew))
        if abs(yvalnew - y1) < tolerance:
            break
        if yvalnew < y1:
            if guess1side == -1:
                dy0guess1 = newguess
                yval1 = yvalnew
            else:
                dy0guess2 = newguess
                yval2 = yvalnew
        else:
            if guess1side == 1:
                dy0guess1 = newguess
                yval1 = yvalnew
            else:
                dy0guess2 = newguess
                yval2 = yvalnew
        
    print('{} steps'.format(i))
    plt.plot(datX,datY[0],'ro',ms=2)
    yval1 = datY[0][-1]
    print('final yval',yval1)
    

    


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
tolerance = 0.01
step = 0.1

def f(x):
    return ((0.157*m.exp((m.sqrt(2)*x))) + (1.043*m.exp((-1*m.sqrt(2)*x))))

shooting(f1,f2,x0,y0,x1,y1,dy0guess1,tolerance,step)
X,Y = f_data(f,0,1,100)
plt.plot(X,Y)
plt.show()
