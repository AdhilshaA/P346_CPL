# question 1 code and input

import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

###--  INPUTS and meaning  --###
#

n = 2500 #no of points considered

random = lib.randgen(21) #initiating random generator with seed 21

countin = 0 #no. of points inside

for i in range(n):
    x = (2*random.gen())-1 #random number in the range -1 to 1
    y = (4*random.gen())-2 #random number in the range -2 to 2

    if ((4*(x**2))+(y**2)) <= 4: #counting if inside ellipse
        countin += 1


truearea = m.pi*2
area = 8*(countin/n) #finding area by (ratio of points in to all)*total area of rectangle 

print("The area found by LCG pRNG is {:.4f} whereas the true area is {:.4f} within {:.2f} percent error".format(area,truearea,abs(area-truearea)/(truearea/100)) )
######-----  OUTPUT  -----######
'''
The area found by LCG pRNG is 6.1536 whereas the true area is 6.2832 within 2.06 percent error
'''