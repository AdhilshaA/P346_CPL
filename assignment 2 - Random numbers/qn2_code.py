# FInding volume of a sphere in first quadrant and total using throwing method

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 2 - Random numbers/qn2_input.txt'))  #getting those variables into this code

###----  VARIABLES and meaning  ----###
# seed :    for LCG Random generator
# num  :    No. of random points considered
# inside :  points landing inside sphere
# Randoms:  list of random numbers
# part_vol : volume of sphere in first quadrant
# total_vol: total volume of sphere

inside = 0 #points landing inside sphere

Randoms = lib.LCG(seed, 3 * num) #need three coordinates

i = 0
while i < (3 * num):
    if ((Randoms[i] ** 2) + (Randoms[i+1] ** 2) + (Randoms[i+2] ** 2)) <= 1: #insied sphere condition
        inside += 1
    i += 3
part_vol = (inside / num)
total_vol = 8 * part_vol

print('Using seed = {} and {} points in throwing method,\n The volume of sphere in first Qudrant is: {:.4f}\nThe total volume of sphere is : {:.4f}'.format(seed,num,part_vol,total_vol))


######-----  OUTPUT  -----######
'''
Using seed = 403.0 and 5000 points in throwing method,
 The volume of sphere in first Qudrant is: 0.5152
The total volume of sphere is : 4.1216
'''


