# DIY code and output

import mylibrary as lib
import library as diy
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('DIY project/input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
#

# required coupled eqn.s
# def ddy(ylist,t):
#     return (m.cos(omega * t) - ylist[0] - ((gamma/2) * ylist[1]))

# def dy(ylist,t):
#     return ylist[1]

def ddy(ylist,t):
    return (-1*m.sin(ylist[0]))

def dy(ylist,t):
    return ylist[1]
tf = 20
h = 0.001
t0 = 0
y0 = 3.1
dy0 = 0
tolerance = 1e-5

# anomaly!!
# g = 9.8
# m1 = 2
# m2 = 2
# L1 = 1
# L2 = 1
# t1i = m.pi-0.01
# t2i = 0
# w1i = 0
# w2i = 0
# ti = 0
# tf = 10
# hi  = 0.001
# tolerance = 1e-6

# A normal case
g = 9.8
m1 = 2
m2 = 2
L1 = 1
L2 = 1
t1i = m.pi/2
t2i = 0
w1i = 0
w2i = 0
ti = 0
tf = 15
hi  = 0.025
tolerance = 1e-3

# g = 9.7803253359
# g = 9.8
# m1 = 2
# m2 = 2
# L1 = 1
# L2 = 1
# t1i = 2.486720
# t2i = -0.283516
# w1i = 2.895948
# w2i = 2.142171
# ti = 7
# tf = 10
# hi  = 0.001
# tolerance = 1e-6

# twlist is in format [t1, t2, w1, w2]
def dt1(twlist,t):
    return twlist[1]

def dt2(twlist,t):
    return twlist[3]

def dw1(twlist,t):
    return ((-1*g*((2*m1) + m2)*m.sin(twlist[0])) - (m2*g*m.sin(twlist[0] - (2*twlist[2]))) - (2*m.sin(twlist[0]-twlist[2])*m2*(((twlist[3]**2)*L2) + ((twlist[1]**2)*L1*m.cos(twlist[0]-twlist[2])))))/(L1*((2*m1)+m2-(m2*m.cos((2*twlist[0]) - (2*twlist[2])))))

def dw2(twlist,t):
    return (2*m.sin(twlist[0]-twlist[2])* (((twlist[1]**2)*L1*(m1+m2)) + (g*(m1 + m2)*m.cos(twlist[0])) + ((twlist[3]**2)*L2*m2*m.cos(twlist[0]-twlist[2]))))/(L2*((2*m1)+m2-(m2*m.cos((2*twlist[0]) - (2*twlist[2])))))


# solution and plotting
# print("<The output for 80 time units is attached as 'qn1_outputgraph.png'>")
# print("<The detailed output first 20 time units is attached as 'qn1_outputgraphdetailed.png'>")
# X,Y = lib.RK4_coupled([dy,ddy],t0,[y0,dy0],tf,h)
# plt.plot(X,Y[0],'-',ms=2,label="y(t)")
# # plt.plot(X,Y[1],'-',ms=2,label="y'(t)")
# plt.legend()
# plt.xlabel("time, t")
# plt.ylabel("y(t)")
# plt.title("y(t) vs t graph for 80 sec")
# plt.show()
# plt.plot(X[:len(X)//4],Y[0][:len(X)//4],'-',ms=2,label="y(t)")
# plt.plot(X[:len(X)//4],Y[1][:len(X)//4],'-',ms=2,label="y'(t)")
# plt.legend()
# plt.xlabel("time, t")
# plt.ylabel("y(t),y'(t)")
# plt.title("detailed y(t),y'(t) vs t graph for 20 sec")
# plt.show()

# X,Y,counts = diy.RK4_adaptivestep([dy,ddy],t0,[y0,dy0],tf,h,tolerance)
# plt.plot(X,Y[0],'-',ms=2,label="y(t)")
# plt.vlines(X,min(Y[0]),max(Y[0]),color = 'k')
# # plt.plot(X,Y[1],'-',ms=2,label="y'(t)")
# plt.legend()
# plt.xlabel("time, t")
# plt.ylabel("y(t)")
# plt.title("y(t) vs t graph for 20 sec")
# plt.show()

#RK4
X1,Y1 = lib.RK4([dt1,dw1,dt2,dw2],ti,[t1i,w1i,t2i,w2i],tf,0.025)
plt.plot(X,Y[0],'-',label="t1")
plt.plot(X,Y[1],'-',label="w1")
plt.plot(X,Y[3],'-',label="w2")
plt.plot(X,Y[2],'-',label="t2")
# # plt.legend()
# # plt.show()

X2,Y2,counts = diy.ASRK4([dt1,dw1,dt2,dw2],ti,[t1i,w1i,t2i,w2i],tf,h,tolerance,errprioirity=[0,2])
# # lib.print_coltable({"Sl. NO.":[i for i in range(len(X))],"t":X,"t1":Y[0],"w1":Y[1],"t2":Y[2],"w2":Y[3],})


# print(len(X2))
# plt.plot(X,Y[0],'-',ms=2,label="t1(t)")
# plt.plot(X,Y[1],'-',ms=2,label="w1(t)")

# plt.plot(X,Y[3],'-',ms=2,label="w2(t)")
# plt.plot(X,Y[2],'-',ms=2,label="t2(t)")
# # plt.vlines(X,min(Y[0]),max(Y[0]),color = 'k')
# # plt.plot(X,Y[1],'-',ms=2,label="y'(t)")
# plt.legend()
# plt.xlabel("time, t")
# plt.ylabel("y(t)")
# plt.title("y(t) vs t graph for 20 sec")
# plt.show()



# sum = 0
# for i in range(len(counts)):
#     sum += counts[i] + 1
# eff = (tf-t0) / (sum * 3)
# print("effective step =",eff)
# plt.show()

def get_coords(t1,t2):
    return L1 * m.sin(t1), -L1 * m.cos(t1), ((L1 * m.sin(t1)) + (L2 * m.sin(t2))), (-L1 * m.cos(t1) + -L2 * m.cos(t2))

fig = plt.figure()
ax = fig.add_subplot(aspect='equal')
# The pendulum rod, in its initial position.
x1i, y1i,x2i,y2i = get_coords(t1i,t2i)
line1, = ax.plot([0, x1i], [0, y1i], lw=3, c='k')
line2, = ax.plot([x1i, x2i], [y1i, y2i], lw=3, c='k')
# The pendulum bob: set zorder so that it is drawn over the pendulum rod.
bob_radius = 0.08
circle1 = ax.add_patch(plt.Circle((x1i,y1i), bob_radius,
                      fc='r', zorder=3))
circle2 = ax.add_patch(plt.Circle((x2i,y2i), bob_radius,
                      fc='r', zorder=3))
# Set the plot limits so that the pendulum has room to swing!
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)

def animate(i):
    """Update the animation at frame i."""
    x1,y1,x2,y2 = get_coords(Y1[0][i],Y1[2][i])
    line1.set_data([0, x1], [0, y1])
    circle1.set_center((x1, y1))
    line2.set_data([x1, x2], [y1, y2])
    circle2.set_center((x2, y2))

nframes = len(Y[0])
interval = 138
ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True,
                              interval=interval)

# ani.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)
plt.show()
######-----  OUTPUT  -----######
'''

'''