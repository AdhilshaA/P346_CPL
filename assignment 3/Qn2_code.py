# Solving The given set of euations using Gauss-Jordon elimination and LU decomposition.

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 3/qn2_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# matA     :  matrix A
# matB     :  matrix B
# matAcopy : copy of matrix A for extended use
# x     : solution in Gauss seidel solve
# steps : steps taken in Gauss-Seidel solve


print('These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:')
lib.print_mat(matA)
print('and B is')
lib.print_mat(matB)

#taking a copy of matA (changes will be linked if simply assigned)
matAcopy = lib.mat_copy(matA)

print('\nUsing Cholesky decomposition method to solve this, we get the solution:')
lib.print_mat(lib.solve_Cholesky(matAcopy,matB))

X,steps = lib.solve_GS(matA, matB, 0.000001)
print('\n Using the Gauss-Seidel method with precision 10^(-6), we get the solution in',steps,'steps as:\n(To see the precision I have display upto 8 decimal points)')
lib.print_mat2(X) #change of matA is fine as we dont have any more use; moreover LU works like that to save space.

######-----  OUTPUT  -----######
'''
These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:
[    4.0000    -1.0000     0.0000    -1.0000     0.0000     0.0000   ]
[   -1.0000     4.0000    -1.0000     0.0000    -1.0000     0.0000   ]
[    0.0000    -1.0000     4.0000     0.0000     0.0000    -1.0000   ]
[   -1.0000     0.0000     0.0000     4.0000    -1.0000     0.0000   ]
[    0.0000    -1.0000     0.0000    -1.0000     4.0000    -1.0000   ]
[    0.0000     0.0000    -1.0000     0.0000    -1.0000     4.0000   ]

and B is
[   2.0000   ]
[   1.0000   ]
[   2.0000   ]
[   2.0000   ]
[   1.0000   ]
[   2.0000   ]


Using Cholesky decomposition method to solve this, we get the solution:
[   1.0000   ]
[   1.0000   ]
[   1.0000   ]
[   1.0000   ]
[   1.0000   ]
[   1.0000   ]


 Using the Gauss-Seidel method with precision 10^(-6), we the solution in 16 steps as:
(To see the precision I have display upto 8 decimal points)
[   0.99999975   ]
[   0.99999979   ]
[   0.99999991   ]
[   0.99999985   ]
[   0.99999987   ]
[   0.99999995   ]

'''