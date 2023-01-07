import mylibrary as lib
import math as m
import matplotlib.pyplot as plt
def radioactivity(Nlist,tlist,step,tf,seed1):
    n = len(Nlist)
    Nlist.append(0)
    # print(n)
    result = Nlist[:]
    for i in range(len(result)):
        result[i] = [result[i]]
    for i in range(n):
        tlist[i] = ((m.log(2)/tlist[i]) * step)
    # print(tlist)
    ran = lib.randgen(seed = seed1)
    t = step
    times = [0]
    decays = [[] for i in range(n)]
    while t <= tf:
        for i in range(n):
            trials = Nlist[i]
            decay = 0
            for j in range(trials):
                if ran.gen() <= tlist[i]:
                    # print("decayed")
                    decay += 1
            Nlist[i] -= decay
            Nlist[i+1] += decay
            decays[i].append(decay)
        times.append(t)
        for i in range(len(result)):
            result[i].append(Nlist[i])
        t += step
    return times,result,decays

def poissons(D):
    dist = [[] for i in range(len(D))]
    maxim = 0
    for i in range(len(D)):
        maxim = max(maxim,max(D[i]))
    X2 = [i for i in range(maxim + 1)]
    # print(dist,maxim,X2)
    for i in range(len(D)):
        dist[i] = [0]*(maxim + 1)
        for j in range(len(D[i])):
            dist[i][D[i][j]] += 1
            # print("1 added to ",D[i][j], dist)
    return X2, dist

N = [500,0]
t = [20,35]
h = 2
tend = 100
seed1 = 1234

X,Y,D = radioactivity(N,t,h,tend,seed1)
print(D)
# X2, dist = poissons(D)
# print(dist,len(X2),len(dist[0]),len(dist[1]))


plt.plot(X,Y[0],'ro',label = "N(A)",ms = 4)
plt.plot(X,Y[1],'bo',label = "N(B)",ms = 4)
plt.plot(X,Y[2],'go',label = "N(C)",ms = 4)
plt.legend()
plt.show()

plt.hist(D[0],bins = max(D[0]),rwidth = 0.9,color = 'red', align = 'mid')
plt.ylabel("times")
plt.xlabel("decayed N(A) per time step")
plt.show()


plt.hist(D[1],bins = max(D[1]), rwidth = 0.9, color = 'blue', align = 'mid')
plt.ylabel("times")
plt.xlabel("decayed N(B) per time step")
plt.show()
        
        
