# Matrix multiplication and Dot product of Column vectors

import mylibrary as lib

#Variables
A = [[2,-3,1.4],[2.5,1,-2],[-0.8,0,3.1]]
B = [[0,-1,1],[1.5,0.5,-2],[3,0,-2]]
C = [[-2],[0.5],[1.5]]
D = [[1],[0],[-1]]


def mat_mult(A,B): #finding AB matrix

  #verifiying matrix multiplication is possible (cols of A ?= rows of B)
  if len(A[0]) != len(B):
    return None

  #creating the sum matrix with zeroes
  sum = []
  for i in range(len(A)): #no. of row in sum is row of A
    sum.append(list()) 
    for j in range(len(B[0])):
      sum[i].append(0) #no. of col in sum is col of B, that many zeroes added

  #filling the sum matrix
  for row in range(len(sum)):
    for col in range(len(sum[0])):
      #finding each term in sum matrix
      temp_sum = 0
      for i in range(len(B)):
        temp_sum += A[row][i] * B[i][col]
      sum[row][col]=temp_sum

  return sum
      
def mat_dot(A,B):
  #returns the dot product of two column matrices
  if len(A) != len(B) or len(A[0]) != 1 or len(B[0]) != 1:
    return None
  dotprdct = 0
  for row in range(len(A)):
    dotprdct += (A[row][0] * B[row][0])
  return dotprdct


print('AB is')
lib.printmat(mat_mult(A,B))       #  printmat is a function I wrote for printing nested list matrix.
print('BC is')                    #  It positions the matrix elements neatly in rows and columns. See mylibrary.py for details
lib.printmat(mat_mult(B,C))
print('D.C is')
print(mat_dot(D,C))


#  OUTPUT
"""

AB is
[   -0.30    -3.50     5.20   ]
[   -4.50    -2.00     4.50   ]
[    9.30     0.80    -7.00   ]

BC is
[    1.00   ]
[   -5.75   ]
[   -9.00   ]

D.C is
-3.5 

"""