import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

def integrate_montecarlo(f,a,b,N):
    if a < b:
        rand = lib.randgen(seed = 12,interval = (a,b))
    else:
        rand = lib.randgen(seed = 12,interval = (b,a))
    sum = 0
    for i in range(N):
        sum += f(rand.gen())
    return sum*((b-a)/N)

def f(x):
    return 4/(1+(x**2))

pis = []
N = 10
for i in range(500):
    
    pis.append(integrate_montecarlo(f,0,1,N))
    N += 10

plt.plot([10*i for i in range(1,501)],pis,'ro',ms=2)
plt.axhline(m.pi)
plt.show()
