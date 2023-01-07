import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input4.txt'))  #getting those variables into this code

#these constants contain m.pi which cannot be read unless I compromise accuracy, therefore written here
tm = m.pi/4
a = m.sin(tm/2)
xf = m.pi/2

#the function under integration
def f(x):
    return 1/(m.sqrt(1-((a*m.sin(x))**2)))

# finding T using the given equation, the integration is also in here.
T = 4*(m.sqrt(L/g))*(lib.integrate_simpson(f,xi,xf,N))

print("The final T found is {:.4f} s.".format(T))

######-----  OUTPUT  -----######
'''
The final T found is 2.0873 s.
'''