import mylibrary as lib
import math as m

def f1(x):
    return (x - 2*m.cos(x))

def f2(x):
    return ((m.cos(x))-(x**3))

def f3(x):
    return ((3*x) + (m.sin(x)) - (m.exp(x)))

def f4(x):
    return ((x*(m.exp(x)))-2)

def f5(x):
    return (x**4 - 4*(x**3) - (x**2) + (10*x))

delta = 0.0001
epsilon = 0.0001

def root_regulafalsi(f,a,b,epsilon,delta):
    a,b = lib.root_bracketing(f,a,b)

    c = b - (((b-a)*f(b))/(f(b) - f(a)))
    if f(c)*f(a) < 0:
        b = c
    else:
        a = c

    steps = 2
    while steps < 100:
        oldc = c
        c = b - (((b-a)*f(b))/(f(b) - f(a)))
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
        if abs(c-oldc) < epsilon and f(c) < delta:
            return c,steps
        oldc = c
        steps += 1
    print('Not converging after 100 steps, terminated')
    return None

r,steps = root_regulafalsi(f1,-1.5,1.5,epsilon,delta)
print('for f1, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_regulafalsi(f2,-1.5,1.5,epsilon,delta)
print('for f2, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_regulafalsi(f3,-1.5,1.5,epsilon,delta)
print('for f3, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_regulafalsi(f4,-1.5,1.5,epsilon,delta)
print('for f4, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_regulafalsi(f5,-0.5,3.5,epsilon,delta)
print('for f5, {:.5f} is a root within {} steps'.format(r,steps))
