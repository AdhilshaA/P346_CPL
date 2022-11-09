# numerical integration using the simpson method

import mylibrary as lib
import math as m

###--  INPUTS and meaning  --###
#

def integrate_simpson(f,a,b,N):
    h = (b-a)/N
    step = h/2
    sum = f(a)+f(b)+(4*f(a+(step)))
    b -= step
    a += h
    while a < b:
        sum += ((2*f(a)) + (4*f(a + step)))
        a += h
    sum *= (step/3)
    return sum

def f1(x):
    return (1/x)
a1 = 1
b1 = 2

def f2(x):
    return (x*m.cos(x))
a2 = 0
b2 = (m.pi)/2

print("Using simpson method")
N = 4
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f1,a1,b1,N)))
N = 7
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f1,a1,b1,N)))
N = 12
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f1,a1,b1,N)))
N = 20
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f1,a1,b1,N)))
N = 200
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f1,a1,b1,N)))

N = 4
print('\nfor f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f2,a2,b2,N)))
N = 8
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f2,a2,b2,N)))
N = 12
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f2,a2,b2,N)))
N = 20
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f2,a2,b2,N)))
N = 200
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_simpson(f2,a2,b2,N)))

######-----  OUTPUT  -----######
'''

'''