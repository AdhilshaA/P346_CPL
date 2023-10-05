#class myComplex and its add multiply functions

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('Assignment 1/qn5_input.txt'))  #getting those variables into this code


print('The complex numbers given are :')
print(z1)
print(z2)


print('\nThe sum is : ',z1 + z2)


print('The product is : ',z1 * z2)

print('The modulus of z1 is : {:.2f}'.format(abs(z1)))
print('The modulus of z1 is : {:.2f}'.format(abs(z2)))

#   OUTPUT
'''
The complex numbers given are :
3 + (-2)i
1 + (2)i

The sum is :4 + (0)i
The product is :7 + (4)i
The modulus of z1 is : 3.61
The modulus of z1 is : 2.24
'''