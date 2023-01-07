import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input5.txt'))  #getting those variables into this code

#required functions
def dy(ylist, t):
    return ylist[1]
def ddy(ylist, t):
    return ((-1*gamma*ylist[1]) - g)

#finding solution using RK4
X,Y = lib.RK4_coupled([dy,ddy],t0,[y0,v0],tf,dt)

#finding max height acheived
maxh = 0
for i in range(len(Y[0])):
    if Y[0][i] > maxh:
        maxh = Y[0][i]
        t4max = X[i]

print("The maximum height got as h = {:.4f} m at t = {:.4f}".format(maxh,t4max))
print("The height vs time graph is attached as <output5hvstgraph.png>\nThe velocity vs height graph is attached as <output5Vvshgraph.png>")

#data plottings
plt.plot(X,Y[0],'--',color="k",ms=2,label="y(t)")
plt.plot(X,Y[0],"ro",ms=4)
plt.legend()
plt.xlabel("time, t")
plt.ylabel("y(t)")
plt.title("y(t) vs t graph")
plt.annotate('({:.2f},{:.2f})'.format(t4max,maxh), (t4max,maxh), textcoords="offset points",  xytext=(0,5),  ha='center', fontsize = 8)
plt.show()
plt.plot(Y[0],Y[1],'--',color="k",ms=2)
plt.plot(Y[0],Y[1],'go',ms=4)
plt.xlabel("height, y(t)")
plt.ylabel("velocity, y'(t)")
plt.title("velocity vs height graph")
plt.show()

######-----  OUTPUT  -----######
'''
The maximum height got as h = 4.9338 m at t = 1.0000
The height vs time graph is attached as <output5hvstgraph.png>
The velocity vs height graph is attached as <output5Vvshgraph.png>
'''