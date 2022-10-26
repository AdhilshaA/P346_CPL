import mylibrary as lib
import matplotlib.pyplot as plt
def linearfit_leastsquare(dataX,dataY,datasigma=None):
    #returns the linear equation in polynomial form where the line is a0+a1x

    n = len(dataX) #no. of datasets

    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None
    Sxx = 0
    Syy = 0 #for pearson R square calc.
    Sxy = 0
    Sx = 0
    Sy = 0

    if datasigma is None:
        S = n
        for i in range(n):
            Sxx += dataX[i]**2
            Syy += dataY[i]**2
            Sxy += dataX[i] * dataY[i]
            Sx += dataX[i]
            Sy += dataY[i]

    else:
        S = 0
        for i in range(n):
            S += 1/(datasigma[i]**2)
            Sxx += (dataX[i]**2)/(datasigma[i]**2)
            Syy += (dataY[i]**2)/(datasigma[i]**2)
            Sxy += (dataX[i] * dataY[i])/(datasigma[i]**2)
            Sx += dataX[i]/(datasigma[i]**2)
            Sy += dataY[i]/(datasigma[i]**2)

    delta = (S*Sxx)-(Sx**2)
    a0 = ((Sxx*Sy) - (Sx*Sxy)) / delta
    a1 = ((Sxy*S) - (Sx*Sy)) / delta

    R2 = (((n*Sxy) - (Sx*Sy))**2)/(((n*Sxx)-(Sx**2)) * ((n*Syy)-(Sy**2)))

    return [a0,a1],R2

px,r2 = linearfit_leastsquare([1,2,3,4],[2,6,10,12])
print(r2)
datax,datay = lib.px_graphdata(px,0,5,20)
plt.plot(datax,datay)
plt.plot([1,2,3,4],[3,6,9,12],'ro')
plt.show()
