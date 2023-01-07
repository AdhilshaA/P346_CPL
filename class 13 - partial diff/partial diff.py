import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

def f0(x):
    return 20*abs(m.sin((m.pi)*x))


def partialdiff_heatdiffusion(f0,xi,xf,ti,tf,nx,nt,times = []):

    hx = (xf-xi)/nx
    ht = (tf-ti)/nt
    alpha = ht/(hx**2)
    # print(alpha)
    # alpha = 0.008

    V0 = [f0(xi)]
    X = [xi]
    x = xi + hx
    for i in range(nx):
        X.append(x)
        V0.append(f0(x))
        x += hx
    # print(len(V0))
    # plt.plot(X,V0)
    Vlist = [V0[:]]

    for i in range(1,nt+1):
        V1 = [(alpha*V0[1] + ((1-(2*alpha))*V0[0]))]
        for j in range(1,nx):
            V1.append((alpha*(V0[j+1]+V0[j-1]) + ((1-(2*alpha))*V0[j])))
        V1.append(alpha*V0[nx-1] + ((1-(2*alpha))*V0[nx]))

        # offset = V1[0] - V0[0]
        # for j in range(nx+1):
        #     V1[j] -= offset

        V0 = V1[:]

        if i in times:
            print('adding to')
            Vlist.append(V0[:])
            
    if bool(times) is False:
        return X,V0
    return X,Vlist

X,Y = partialdiff_heatdiffusion(f0,0,2,0,4,20,5000,times = [10,20,50,100,200,500,1000])
print(Y)
for i in range(len(Y)):
    plt.plot(X,Y[i])
plt.show()
