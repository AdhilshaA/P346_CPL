#class myComplex and its add multiply functions

from math import sqrt

class myComplex:

  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def printz(self): #for printing complex no. in (a + bi) format
    print(self.real,' + (',self.imag,')i',sep='')

  def add(z1,z2):
    add_real = z1.real + z2.real
    add_imag = z1.imag + z2.imag
    z3 = myComplex(add_real, add_imag)
    return z3
  
  def mult(z1,z2):
    mult_real = (z1.real * z2.real) - (z1.imag * z2.imag)
    mult_imag = (z1.real * z2.imag) + (z1.imag * z2.real)
    z3 = myComplex(mult_real, mult_imag)
    return z3
  
  def modulus(self):
    val = sqrt((self.real ** 2) + (self.imag ** 2))
    return val


#Given
z1 = myComplex(3,-2)
z2 = myComplex(1,2)


print('The complex numbers given are :')
z1.printz()
z2.printz()

z3 = myComplex.add(z1,z2)
print('\nThe sum is :',end='')
z3.printz()

z3 = myComplex.mult(z1,z2)
print('The product is :',end='')
z3.printz()

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