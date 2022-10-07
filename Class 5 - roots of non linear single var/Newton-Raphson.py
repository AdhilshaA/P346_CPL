import math as m
import mylibrary as lib

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

def df1(x):
    return (1 + m.sin(x))

def df2(x):
    return (-1*m.sin(x) - 3*(x**2))
def df3(x):
    return (3 + m.cos(x) - (m.exp(x)))
def df4(x):
    return ((x+1)*m.exp(x))

def root_newtonraphson(f,df,x0,epsilon,delta):
    steps = 0
    while steps < 100:
        x1 = x0 - (f(x0)/df(x0))
        if abs(x1 - x0) < epsilon and f(x1) < delta:
            return x1,steps
        x0 = x1
        steps += 1
    print('Not converging after 100 steps, terminated')
    return None


r,steps = root_newtonraphson(f1,df1,1.0,epsilon,delta)
print('for f1, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_newtonraphson(f2,df2,1.0,epsilon,delta)
print('for f1, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_newtonraphson(f3,df3,1.0,epsilon,delta)
print('for f1, {:.5f} is a root within {} steps'.format(r,steps))
r,steps = root_newtonraphson(f4,df4,1.0,epsilon,delta)
print('for f1, {:.5f} is a root within {} steps'.format(r,steps))
