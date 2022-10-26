# question 4 code and output

import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 4/qn 4_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
#  X    : list of x-values from data
#  Y    : list of y-values from data
#  order: The intended order of polynomial to be fit
#  px   : the polynomial resulted from the fit function
#  graphx   : list of x-values for polynomial fit graph
#  graphy   : list of y-values for polynomial fit graph


# The data X and Y has been checked while parsing to be matching size , therefore not checked again

px = lib.fit_polyleastsq(X,Y,order) #fitting to a polynomial of order 3
graphx,graphy = lib.px_graphdata(px,X[0],X[-1],20) #getting graph data for the said polynomial

print('The coefficients of the polynomial fit of order 3 using least square fitting are:')
print('{} in the order [a0,a1,a2,a3]'.format(['{:.4f}'.format(a) for a in px]))

#plotting the data
plt.plot(X,Y,'ro',ms=4) 
plt.plot(graphx,graphy,'b-')
plt.title('Polynomial fit of order 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
######-----  OUTPUT  -----######
'''
The coefficients of the polynomial fit of order 3 using least square fitting are:
['0.5747', '4.7259', '-11.1282', '7.6687'] in the order [a0,a1,a2,a3]

<The output graph is attached as qn 4_polynomialfit.png>
'''