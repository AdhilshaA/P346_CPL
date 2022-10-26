# Question 3 and code

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 4/qn 3_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# px  : is the polynomial in list format of coefficients a0,a1,a2.. where ai is the coefficient of ith power of x.
# tolerance : the tolerance value that decided how close you want to get
# roots  : array that stores all the roots of the polynomial

roots = lib.root_laguire(px,0,tolerance) #calling laguire method on polynomial that finds all roots (uses sythetic division)
                                         # returns a list of roots (also prints the roots and steps taken)

print('Thus, the roots are ',end='',sep='')
for i in roots:
    print(', {:.4f}'.format(i),end='',sep='')
print('.')

######-----  OUTPUT  -----######
'''
1th root, -1.0000, is found in 4 steps.
2th root, 1.0000, is found in 3 steps.
3th root, -2.0000, is found in 1 steps.
4th root, 2.0000, is found in 1 steps.
Thus, the roots are , -1.0000, 1.0000, -2.0000, 2.0000.
'''