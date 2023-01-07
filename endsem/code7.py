import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input7.txt'))  #getting those variables into this code


# The data X and Y has been checked while parsing to be matching size , therefore not checked again

px = lib.fit_polyleastsq(X,Y,order) #fitting to a polynomial
graphx,graphy = lib.px_graphdata(px,X[0],X[-1],20) #getting graph data for the said polynomial

print('The coefficients of the polynomial fit of order 4 using least square fitting are:')
print('{} in the order [a0,a1,a2,a3,a4]'.format(['{:.4f}'.format(a) for a in px]))

#plotting the data
plt.plot(X,Y,'ro',ms=4) 
plt.plot(graphx,graphy,'b-')
plt.title('Polynomial fit of order 4')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
print("<The output graph is attached as output7.png>")
######-----  OUTPUT  -----######
'''
The coefficients of the polynomial fit of order 4 using least square fitting are:
['0.2546', '-1.1938', '-0.4573', '-0.8026', '0.0132'] in the order [a0,a1,a2,a3,a4]
<The output graph is attached as output7.png>
'''