import mylibrary as lib
import math as m

def eigen_rayleigh(A,x0,tolerance):
    Akx0 = (A*x0)
    # Akx0.table()
    # A.table()
    # x0.table()
    denom = (Akx0.dot(x0))
    Akx0 = (A*Akx0)
    num = (Akx0.dot(x0))
    k = 0
    lamk = num/denom
    
    while k<50:
        denom = num
        evec = Akx0.copy()
        Akx0 = (A*Akx0)
        num = (Akx0.dot(x0))
        k += 1
        lamk2 = num / denom
        if abs(lamk - lamk2) < tolerance:
            evec *= (1/abs(evec))
            return lamk2,evec,k
        lamk = lamk2
        # print(lamk2)

A = lib.mat([[1,-1,0],[-2,4,-2],[0,-1,2]])
x0 = lib.mat([[1],[2],[3]])

eval,evec,steps = eigen_rayleigh(A,x0,0.001)
print(eval)
print(steps)
evec.table()
