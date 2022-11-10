# Question 3 code and output

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 5/qn3_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# f       : the linear density function
# xf      : the linear density function weighted with positions
# a and b : the integral goes from a to b (total length 2, thus 0 to 2)
# COM     : center of mass

######-----  THEORY  -----######
# # For finding the centre of mass, we need to find 
# ( integral(x*f(x)) on total length ) / ( integral(f(x)) on total length )
# here f(x) is the mass denisty function
# the numerator is the mass density function wighted with positions and denominator is the total mass of rod

def f(x):
    return (x**2)
def xf(x):
    return (x**3)

COM = (lib.integrate_simpson(xf,a,b,N)/lib.integrate_simpson(f,a,b,N))
print("The centre of mass turned out to be at x = {}".format(COM))

######-----  OUTPUT  -----######
'''
The centre of mass turned out to be at x = 1.5
'''