import mylibrary as lib
import math as m

def integrate_trapezoidal(f,a,b,N):
    step = (b-a)/N
    sum = (f(a)+f(b))/2
    b -= (step/2)
    a += step
    while a < b:
        sum += f(a)
        a += step
    sum *= step
    return sum

def f1(x):
    return (1/x)
a1 = 1
b1 = 2

def f2(x):
    return (x*m.cos(x))
a2 = 0
b2 = (m.pi)/2

print("Using trapezoidal method")
N = 4
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f1,a1,b1,N)))
N = 8
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f1,a1,b1,N)))
N = 12
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f1,a1,b1,N)))
N = 20
print('for f1 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f1,a1,b1,N)))

N = 4
print('\nfor f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f2,a2,b2,N)))
N = 8
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f2,a2,b2,N)))
N = 12
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f2,a2,b2,N)))
N = 20
print('for f2 from {} to {}, N ={}, we get {}'.format(a1,b1,N,integrate_trapezoidal(f2,a2,b2,N)))

