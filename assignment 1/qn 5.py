#class myComplex and its add multiply functions

from math import sqrt

class myComplex:

  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def __str__(self): #for printing complex no. in (a + bi) format when called print on any class instance
    return '{} + ({})i'.format(self.real, self.imag)

  def add(self,z2): # Method to add it with z2 of same class
    add_real = self.real + z2.real
    add_imag = self.imag + z2.imag
    z3 = myComplex(add_real, add_imag)
    return z3
  
  def mult(self,z2): # Method to multiply it with z2 of same class
    mult_real = (self.real * z2.real) - (self.imag * z2.imag)
    mult_imag = (self.real * z2.imag) + (self.imag * z2.real)
    z3 = myComplex(mult_real, mult_imag)
    return z3
  
  def modulus(self):
    val = sqrt((self.real ** 2) + (self.imag ** 2))
    return val


#Given
z1 = myComplex(3,-2)
z2 = myComplex(1,2)


print('The complex numbers given are :')
print(z1)
print(z2)

z3 = z1.add(z2)
print('\nThe sum is : ',z3)

z3 = z1.mult(z2)
print('The product is : ',z3)

print('The modulus of z1 is : {:.2f}'.format(z1.modulus()))
print('The modulus of z1 is : {:.2f}'.format(z2.modulus()))

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