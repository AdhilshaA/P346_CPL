# Question 1 code and output

import mylibrary as lib
import math as m

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 5/qn1_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# f       : the function to be integrated
# a and b : the integral goes from a to b
# data    : a dictionary that has table titles as key and columns as value

def f(x):
    return m.sqrt(1+(1/x))

# Adding the N in the respective order
data = {'N':[10,20,30]}

# Adding titles and the respective values by calling the respective functions from library
data['Midpoint method']=[lib.integrate_midpoint(f,a,b,10),lib.integrate_midpoint(f,a,b,20),lib.integrate_midpoint(f,a,b,30)]
data['Trapezoidal method']=[lib.integrate_trapezoidal(f,a,b,10),lib.integrate_trapezoidal(f,a,b,20),lib.integrate_trapezoidal(f,a,b,30)]
data['Simpson method']=[lib.integrate_simpson(f,a,b,10),lib.integrate_simpson(f,a,b,20),lib.integrate_simpson(f,a,b,30)]

print('The following table shows the results of the integration in question')
lib.print_coltable(data) #function for printing tables

######-----  OUTPUT  -----######
'''
The following table shows the results of the integration in question
|----|-----------------|--------------------|----------------|
| N  | Midpoint method | Trapezoidal method | Simpson method |
|----|-----------------|--------------------|----------------|
| 10 |    3.618979     |      3.622608      |    3.620189    |
| 20 |    3.619880     |      3.620794      |    3.620185    |
| 30 |    3.620049     |      3.620455      |    3.620184    |
|----|-----------------|--------------------|----------------|
'''