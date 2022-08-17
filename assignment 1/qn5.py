#class

class myComplex:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def printz(self):
    print(self.real,' + ',self.imag,'i',sep='')

  def add2(self,z1,z2):
    self.real = z1.real + z2.real
    self.imag = z1.imag + z2.imag

  def add(z1,z2):
    add_real = z1.real + z2.real
    add_imag = z1.imag + z2.imag
    z3 = myComplex(add_real, add_imag)
    return z3

z1 = myComplex(3,1)
z2 = myComplex(3,-2)
z3 = myComplex(0,0)
z3.add2(z1,z2)
z3.printz()

z4 = myComplex.add(z1,z2)
z4.printz()