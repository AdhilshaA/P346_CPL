# question 2 code and output

import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 4/qn 2_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# guess = -1 for newton raphson
# a = -1 (a,b) is the root bracketing 
# b = 0   THe interval (-1,0) is the intial guess interval analyzed numerically
# tolerance = 1e-6 for the methods
# f is the functions
# df is the derivative of the functions
# listi are the lists containing respective methods iteration data


def f(x):
    return (-x-m.cos(x))

def df(x):
    return (m.sin(x)-1)



list1 = lib.root_bisection(f,a,b,tolerance,tolerance,details = True)
list2 = lib.root_regulafalsi(f,a,b,tolerance,tolerance,details = True)
list3 = lib.root_newtonraphson(f,df,guess,tolerance,tolerance,details = True)

#own function for printing tables like this
lib.print_coltable({'iteration':[i+1 for i in range(max(len(list1),len(list2),len(list3)))],'bisection method':list1,'Regula Falsi method':list2,'newton raphson method':list3})

print('We used the interval {} and guess {} for the methods'.format((a,b),guess))
print('Using Bisection method, we arrived at root x = {} within {} steps'.format(list1[-1],len(list1)))
print('Using Regula Falsi method, we arrived at root x = {} within {} steps'.format(list2[-1],len(list2)))
print('Using Newton Rpah son method, we arrived at root x = {} within {} steps'.format(list3[-1],len(list3)))

######-----  OUTPUT  -----######
'''
  iteration    bisection method    Regula Falsi method    newton raphson method  
      1           -0.500000           -0.685073             -0.750364
      2           -0.750000           -0.736299             -0.739113
      3           -0.625000           -0.738945             -0.739085
      4           -0.687500           -0.739078             -0.739085
      5           -0.718750           -0.739085                  -
      6           -0.734375           -0.739085                  -
      7           -0.742188                -                        -
      8           -0.738281                -                        -
      9           -0.740234                -                        -
     10           -0.739258                -                        -
     11           -0.738770                -                        -
     12           -0.739014                -                        -
     13           -0.739136                -                        -
     14           -0.739075                -                        -
     15           -0.739105                -                        -
     16           -0.739090                -                        -
     17           -0.739082                -                        -
     18           -0.739086                -                        -
     19           -0.739084                -                        -
     20           -0.739085                -                        -
We used the interval (-1, 0) and guess -1 for the methods
Using Bisection method, we arrived at root x = -0.7390851974487305 within 20 steps
Using Regula Falsi method, we arrived at root x = -0.7390851156443783 within 6 steps
Using Newton Rpahson method, we arrived at root x = -0.7390851332151607 within 4 steps
'''