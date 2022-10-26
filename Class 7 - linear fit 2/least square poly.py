import mylibrary as lib
import math
import matplotlib.pyplot as plt

def fit_leastsq_polynomial(dataX,dataY,order):

    n = len(dataX) #no. of datasets

    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None

    matX = [[0]*(order+1) for i in range(order+1)]

    #completing matX
    matX[0][0] = n
    for i in range(1,(2 * order) + 1):
        sum = 0
        for j in range(n):
            sum += math.pow(dataX[j],i)
        if i <= order:
            startX = 0
            startY = i
            while startY >= 0:
                # print('p',startX,startY)

                matX[startX][startY] = sum
                startY -= 1
                startX += 1
        else:
            
            startX = i - order
            startY = order
            while startX <= order:
                # print('p',startX,startY)
                matX[startX][startY] = sum
                startY -= 1
                startX += 1

    matY = []
    sum = 0
    for i in range(n):
        sum += dataY[i]
    matY.append([sum])
    for i in range(1,order+1):
        sum = 0
        for j in range(n):
            sum += math.pow(dataX[j],i)*dataY[j]
        matY.append([sum])


    px = lib.solve_GJ(matX,matY)
    for j in range(len(px)):
        px[j] = px[j][0]

    return px

def px_graphdata(px,start,stop,number):
    step = (stop - start) / (number - 1)
    Xvalues = []
    Yvalues = []
    stop += step
    while start < stop:
        Xvalues.append(start)
        Yvalues.append(lib.px_value(px,start))
        start += step
    return Xvalues, Yvalues



with open("Class 7 - linear fit 2/fit2.dat",'r') as datafile:
    dataX = []
    dataY = []
    for data in datafile:
        dataX.append(float(data.split()[0]))
        dataY.append(float(data.split()[1]))

order = 2 #intended polynomial order
coefficients = fit_leastsq_polynomial(dataX,dataY,2,21,15)

Xforpx,Yforpx = px_graphdata(coefficients,dataX[0],dataX[-1],25)
plt.scatter(dataX,dataY,marker='o')
plt.plot(Xforpx,Yforpx,'r-')
plt.show()

