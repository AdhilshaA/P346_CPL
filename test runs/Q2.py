import Library as lib



def diff_shooting(fns,x0,y0,x1,y1,guess1,epsilon,h):    
    X,Y = lib.gen_RK4_coupled(fns,x0,[y0,guess1],x1,h)
    yend1 = Y[0][-1]
    if abs(yend1 - y1) < epsilon:
        return X,Y
    if yend1 < y1:
        guess1side = -1
    else :
        guess1side = 1

    guess2 = guess1 + 2   
    X,Y = lib.gen_RK4_coupled(fns,x0,[y0,guess2],x1,h)
    yend2 = Y[0][-1]
    print(yend2)
    if yend2 < y1:
        guess2side = -1
    else :
        guess2side = 1
    while guess1side * guess2side != -1:
        # print(ye)
        if abs(y1-yend2) > abs(y1-yend1):
            guess2 = guess1 - abs(guess2-guess1)
        else:
            guess2 += abs(guess2-guess1)
            print(guess2)

        
        X,Y = lib.gen_RK4_coupled(fns,x0,[y0,guess2],x1,h)
        yend2 = Y[0][-1]
        print(yend2)
        if yend2 < y1:
            guess2side = -1
        else :
            guess2side = 1


    i = 0
    while True:
        newguess = guess1 + (((guess2 - guess1)/(yend1 - yend2))*(y1 - yend2))
        i += 1
        X,Y = lib.gen_RK4_coupled(fns,x0,[y0,newguess],x1,h)
        yvalnew = Y[0][-1]

        if abs(yvalnew - y1) < epsilon:
            break
        if yvalnew < y1:
            guess1 = newguess
            yend1 = yvalnew
        else:
            guess2 = newguess
            yend2 = yvalnew
    return X,Y

def f1(ilist,x): #ilist=[T,g]
    return 0.01*(ilist[0]-20)    

def f2(ilist,x):
    return ilist[1]

flist=[f2,f1]

a,b=diff_shooting(flist,0,40,10,200,0,0.01,0.5)

import matplotlib.pyplot as plt
plt.plot(a,b[0])
plt.show()
