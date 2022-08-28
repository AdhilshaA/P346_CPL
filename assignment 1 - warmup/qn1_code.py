#program to calculate sum of first N odd numbers and N factorial

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 1 - warmup/qn1_input.txt'))  #getting those variables into this code

#INPUTS
# n1 is the no. of terms of sumof term
# n2 n whose factorial is calculated

print('Sum of',n1,'odd numbers is',lib.sum_odd(n1))
print(n2,'factorial is',lib.fact(n2))

#  OUTPUT
'''
Sum of 5 odd numbers is 25
3 factorial is 6
'''
