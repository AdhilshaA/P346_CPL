# Question 1 code and output

import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

#parsing the inputs 
with open("midsem/msem_fit.txt",'r') as datafile:
    dataX = []
    dataY = []
    for data in datafile:
        dataX.append(float(data.split()[0]))
        dataY.append(float(data.split()[1]))
    datafile.close()

###--  INPUTS and meaning  --###
#   dataX and dataY : data points from the given data
#   dataX1 and dataY1 : powerlaw graph data for the linear fit
#   data21 and dataY2 : exponentiallaw graph data for the linear fit
#   a1,b1 : coefficients in the powerlaw fit
#   a2,b2 : coefficients in the exponentiallaw fit
#   prs1 and prs2 : pearson's R square coeffcient for powerlaw and exponentiallaw


a1,b1,prs1 = lib.fit_powerlaw(dataX,dataY)
a2,b2,prs2 = lib.fit_exponential(dataX,dataY)

dataX1,dataY1 = lib.powerlaw_data(a1,b1,2,21,25)
dataX2, dataY2 = lib.exp_graphdata(a2,b2,2,21,25)

print("For power law, the coefficients are a = {:.4f} and b = {:.4f} with fit of Pearson's R square is {:.4f}.\nFor exponential law,the coefficients are a = {:.4f} and b = {:.4f} with fit of Pearson's R square is {:.4f}.\nTherefore power law model is better as the value of pearson R square is closer to 1".format(a1,b1,prs1,a2,b2,prs2))

plt.plot(dataX1,dataY1)
plt.plot(dataX,dataY,'ro')
plt.title('power law model')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(dataX2,dataY2)
plt.plot(dataX,dataY,'ro')
plt.title('exponential law model')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
######-----  OUTPUT  -----######
'''
For power law, the coefficients are a = 21.0464 and b = -0.5374 with fit of Pearson's R square is 0.9945.
For exponential law,the coefficients are a = 12.2130 and b = -0.0585 with fit of Pearson's R square is 0.9018.
Therefore power law model is better as the value of pearson R square is closer to 1

(Output graphs are attached as q4_powerlawgraph.png and q4_exponentialgraph.png in the same folder)
'''