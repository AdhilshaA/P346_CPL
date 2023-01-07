# question 2 code and output

import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 6/qn2_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# Ta       : The constant for the coupled ODE
# alpha    : another constant for the coupled ODE
# x0       : 0
# y0       : 40
# x1       : 10
# y1       : 200
# dy0guess1: 0
# tolerance: 0.01
# step     : 0.5
# dTdx     : one of the coupled function
# dUdx     : second function where U is taken as dT/dx
# Tlist    : The T, dT values in list
# x        : The variable x denoting position
# datX     : X values for the graph
# datY     : Y values for the graph


#The coupled ODE functions, where U id dT/dx taken for making it coupled ODE
def dTdx(Tlist,x):
    return Tlist[1]

def dUdx(Tlist,x):
    return (-1*alpha*(Ta - Tlist[0]))

#RK4 shooting method applied
datX,datY = lib.diff_shooting([dTdx,dUdx],x0,y0,x1,y1,dy0guess1,tolerance,step)

# Finding x for which T = 100
x = lib.graphsearch(datX, datY, y0 = 100)

#graph plotting and printing results
plt.plot(datX,datY,'ro',ms=2, label = 'solution data points')
plt.axhline(100,c = 'k',ls = '--',lw = 0.5)
plt.axvline(x,c = 'k',ls = '--',lw = 0.5)
plt.annotate('({:.2f},{:.2f})'.format(x,100), (x,100), textcoords="offset points",  xytext=(-30,7),  ha='center', fontsize = 8)
plt.plot([x],[100],'bo',ms=2)
plt.xlabel("Position, x")
plt.ylabel("Temperature, T (degree Celcius)")
plt.title("T vs x graph")
plt.legend(fontsize = 8)
plt.show()
print("<The output graph is attached as 'qn2_outputgraph.png'>")
print("The temperature is 100 degree celcius at x = {:.4f} m on rod.".format(x))

######-----  OUTPUT  -----######
'''
<The output graph is attached as 'qn2_outputgraph.png'>
The temperature is 100 degree celcius at x = 4.4242 m on rod.
'''