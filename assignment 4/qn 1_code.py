# Question 1 code and output

import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 4/qn 1_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# a = 1.5 (a,b) is the intiial root bracketing 
# b = 2.5   THe interval (-1,0) is the intial guess interval analyzed numerically
# tolerance = 1e-6 for the methods
# f is the functions
# listi are the lists containing respective methods iteration data

def f(x):
    return (m.log(x/2) - m.sin(5*(x/2)))

a,b = lib.root_bracketing(f,a,b)
print('By appropriate bracketing extension, we have reached the interval [{},{}] having one or more root\n\n'.format(a,b))

list1 = lib.root_bisection(f,a,b,tolerance,tolerance,details = True)
list2 = lib.root_regulafalsi(f,a,b,tolerance,tolerance,details = True)

#own function for printing tables like this

lib.print_coltable({'iteration':[i+1 for i in range(max(len(list1),len(list2)))],'bisection method':list1,'Regula Falsi method':list2})

print('Using Bisection method, we arrived at root x = {} within {} steps'.format(list1[-1],len(list1)))
print('Using Regula Falsi method, we arrived at root x = {} within {} steps'.format(list2[-1],len(list2)))


######-----  OUTPUT  -----######
'''
By appropriate bracketing extension, we have reached the interval [0.25,2.5] having one or more root
 
 
 iteration  bisection method  Regula Falsi method
     1          1.375000         2.302549
     2          1.937500         1.903200
     3          1.656250         1.468913
     4          1.515625         1.384798
     5          1.445312         1.402500
     6          1.410156         1.401934
     7          1.392578         1.401930
     8          1.401367         1.401930
     9          1.405762              -
    10          1.403564              -
    11          1.402466              -
    12          1.401917              -
    13          1.402191              -
    14          1.402054              -
    15          1.401985              -
    16          1.401951              -
    17          1.401934              -
    18          1.401925              -
    19          1.401929              -
    20          1.401932              -
    21          1.401930              -
    22          1.401930              -
Using Bisection method, we arrived at root x = 1.4019299149513245 within 22 steps
Using Regula Falsi method, we arrived at root x = 1.4019299318447522 within 8 steps
'''