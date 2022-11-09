import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

def g(x):
    return 20*abs(m.sin((m.pi)*x))

hx = 2/20
ht = 4/5000
nt = 5000
nx = 20
alpha = ht/(hx**2)
print(alpha)
# alpha = 0.008
V0 = [0]
x = hx
for i in range(nx):
    V0.append(g(x))
    x += hx
# print(len(V0))

X = [i*hx for i in range(nx+1)]
plt.plot(X,V0)

for i in range(1,1001):
    V1 = [(alpha*V0[1] + ((1-(2*alpha))*V0[0]))]
    for j in range(1,nx):
        # print(i)
        V1.append((alpha*(V0[j+1]+V0[j-1]) + ((1-(2*alpha))*V0[j])))
    V1.append(alpha*V0[nx-1] + ((1-(2*alpha))*V0[nx]))


    # offset = V1[0] - V0[0]
    # for j in range(nx+1):
    #     V1[j] -= offset

    
    V0 = V1[:]
    if i in [10,20,50,100,200,500,1000]:
        plt.plot(X,V0)
        
        # wrong try ig
        # V = []
        # for j in range(nx+1):
        #     V.append(V1[j] - V1[0])
        # plt.plot(X,V)


plt.show()