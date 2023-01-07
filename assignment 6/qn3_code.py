# question 3 code and output

import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 6/qn3_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# f0 : The function of temperature for x at time t = 0
# xi : initial value of position x
# xf : final value of position x
# ti : initial value of time t
# tf : final value of time t
# nx : no. of divisions on position
# nt : no. of divisions on time
# ts : time steps to be in the graph
# x  : the position variable
# X  : X values for the graph
# Y  : list of lists of temperature at different time steps

# The initial temperatures over x
def f0(x):
    if abs(x - 1) < 1e-2:
        return 300
    else:
        return 0

# finding the solution and plotting
print("The del(t)/del(x)^2 is",((tf-ti)/((xf-xi)**2))*((nx**2)/nt))
X,Y = lib.partialdiff_heatdiffusion(f0,xi,xf,ti,tf,nx,nt,times = ts)
for i in range(len(Y)):
    plt.plot(X,Y[i],label = "time step = {}".format(ts[i]))
plt.legend(fontsize = 6)
plt.xlabel("position, x (m)")
plt.ylabel("Temperature, T (degree celcius)")
plt.title("T vs x graph for different time steps")
plt.show()
print("<The output graph is attached as 'qn3_outputgraph.png'>")
# the graph is drawn as lines as otherwise would be confusing to look at
######-----  OUTPUT  -----######
'''
The del(t)/del(x)^2 is 0.08 << 0.5
<The output graph is attached as 'qn3_outputgraph.png'>
'''