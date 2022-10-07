import mylibrary as lib
import math as m

epsilon = 0.0001
delta = 0.0001

def f1(x):
    def __str__(self):
        return 'x - 2cos(x)'
    return (x - 2*m.cos(x))

def f2(x):
    return ((m.cos(x))-(x**3))

def f3(x):
    return ((3*x) + (m.sin(x)) - (m.exp(x)))

def f4(x):
    return ((x*(m.exp(x)))-2)

def f5(x):
    return (x**4 - 4*(x**3) - (x**2) + (10*x))

def root_bracketing(f,a,b):
    for i in range(12):

        if f(a) * f(b) < 0:
            return a,b
        if abs(f(a)) < abs(f(b)):
            temp = a
            a = a - (1.5*(b-a))
            b = temp
        else:
            temp = b
            b = b + (1.5*(b-a))
            a = b
    if abs(f(a)) < abs(f(b)):
        return root_bracketing(a - (1.5*(b-a)),b)
    else:
        return root_bracketing(a,b + 1.5*(abs(b-a)))

def root_bisection(f,a,b,epsilon,delta):
    a,b = root_bracketing(f,a,b)
    steps = 1
    while steps<100:
        # print('difference is {} giving {} and {}'.format(abs(a-b),f(a),f(b)))
        if (a-b) < epsilon:
            if abs(f(a)) < delta or abs(f(b)) < delta:
                return a,b,steps
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1
    print('Not converging after 100 steps, terminated')
    return None
    
r1,r2,steps = lib.root_bisection(f1,-1.5,1.5,epsilon,delta)
print('for f1, {:.5f} ~ {:.5f} are roots within {} steps'.format(r1,r2,steps))
r1,r2,steps = lib.root_bisection(f2,-1.5,1.5,epsilon,delta)
print('for f2, {:.5f} ~ {:.5f} are roots within {} steps'.format(r1,r2,steps))
r1,r2,steps = lib.root_bisection(f3,-1.5,1.5,epsilon,delta)
print('for f3, {:.5f} ~ {:.5f} are roots within {} steps'.format(r1,r2,steps))
r1,r2,steps = lib.root_bisection(f4,-1.5,1.5,epsilon,delta)
print('for f4, {:.5f} ~ {:.5f} are roots within {} steps'.format(r1,r2,steps))
r1,r2,steps = lib.root_bisection(f5,-1.3,3.5,epsilon,delta)
print('for f4, {:.5f} ~ {:.5f} are roots within {} steps'.format(r1,r2,steps))
