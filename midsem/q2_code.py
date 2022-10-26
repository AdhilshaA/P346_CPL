# question 2 code and output

import mylibrary as lib
import math as m

###--  INPUTS and meaning  --###
# f  : LHS of the equation to be solved in RHS = 0 form
# df : derivative of f hardwired
# x  : x is the solution of the equation
# steps : steps taken to solve newton_raphson
# b  : Wein's constant calculated

def f(x):
    return (((x-5)*m.exp(x)) + 5)

def df(x):
    return ((x-4)*m.exp(x))

x,steps = lib.root_newtonraphson(f,df,10,0.0001,0.0001) #here 10 is the guess , the last 2 are tolerances for f to zero approach and root approach

# print('for f1, {:.6f} is a root within {} steps'.format(x,steps))

b = (6.626*3*0.001)/(x*1.381) #here 0.001 is the culmination 10 powers from different constant

print("The value of Wein's constant, b, is {:.4f} * 10^(-3) mK".format(b*1000))

######-----  OUTPUT  -----######
'''
The value of Wein's constant, b, is 2.8990 * 10^(-3) mK
'''