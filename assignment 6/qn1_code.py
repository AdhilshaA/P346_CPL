# question 1 code and output

import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 6/qn1_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# dy    : The dy function from coupled ODE
# ddy   : The ddy function from coupled ODE
# omega : The omega value for the coupled ODE
# gamma : THe gamma value for coupled ODE
# t0    : Initial times
# tf    : final time till which the solution is required
# y0    : Initial y(t) at t = 0
# dy0   : Initial dy(t) at t = 0
# h     : step size for RK4
# ylist : The list of variables for the RK4 (y and dy)
# t     : time variable

# required coupled eqn.s
def ddy(ylist,t):
    return (m.cos(omega * t) - ylist[0] - ((gamma/2) * ylist[1]))

def dy(ylist,t):
    return ylist[1]

# solution and plotting
print("<The output for 80 time units is attached as 'qn1_outputgraph.png'>")
print("<The detailed output first 20 time units is attached as 'qn1_outputgraphdetailed.png'>")
X,Y = lib.RK4_coupled([dy,ddy],t0,[y0,dy0],tf,h)
plt.plot(X,Y[0],'-',ms=2,label="y(t)")
# plt.plot(X,Y[1],'-',ms=2,label="y'(t)")
plt.legend()
plt.xlabel("time, t")
plt.ylabel("y(t)")
plt.title("y(t) vs t graph for 80 sec")
plt.show()
plt.plot(X[:len(X)//4],Y[0][:len(X)//4],'-',ms=2,label="y(t)")
plt.plot(X[:len(X)//4],Y[1][:len(X)//4],'-',ms=2,label="y'(t)")
plt.legend()
plt.xlabel("time, t")
plt.ylabel("y(t),y'(t)")
plt.title("detailed y(t),y'(t) vs t graph for 20 sec")
plt.show()

######-----  OUTPUT  -----######
'''
<The output for 80 time units is attached as 'qn1_outputgraph.png'>
<The detailed output first 20 time units is attached as 'qn1_outputgraphdetailed.png'>
'''