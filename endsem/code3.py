import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input3.txt'))  #getting those variables into this code

# the functions needed
def F(x):
    return (F0 - (x*(m.exp(x))))

def dF(x):
    return -1*(x*(m.exp(x)) + (m.exp(x)))

#trying to find x at which F0 = x.exp(x)
x1,steps = lib.root_newtonraphson(F,dF,x0,epsilon,delta,details = False)

print("Till x = {:.2f}, the spring gets stretched".format(x1))

######-----  OUTPUT  -----######
'''
Till x = 0.96, the spring gets stretched.
'''