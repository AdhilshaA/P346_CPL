# Question 2 code and output

import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 5/qn2_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# f       : the function to be integrated
# a and b : the integral goes from a to b
# N       : number of random numbers to be used for Monte Carlo integral


def f(x):
    return ((m.sin(x))**2)


print('Using Monte-Carlo method, we got the solution as {:.6f} while using {} random numbers'.format(lib.integrate_montecarlo(f,a,b,N),N))

######-----  OUTPUT  -----######
'''
Using Monte-Carlo method, we got the solution as 0.545276 while using 9000 random numbers
'''