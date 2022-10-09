# Solving The given set of euations using Gauss-Jordon elimination and LU decomposition.

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 3/qn3_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# matA      :  matrix A
# matB      :  matrix B
# matAcopy1 : copy of matrix A for extended use
# matBcopy1 : copy of matrix B for extended use
# matAcopy2 : another copy of matrix A for extended use
# X1     : solution in Gauss-seidel solve
# steps1 : steps taken in Gauss-Seidel solve
# X2     : solution in Jacobi solve
# steps2 : steps taken in Jacobi solve

print('These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:')
lib.print_mat(matA)
print('and B is')
lib.print_mat(matB)

#taking a copy of matA (changes will be linked if simply assigned)
matAcopy1 = lib.mat_copy(matA)
matAcopy2 = lib.mat_copy(matA)
matBcopy1 = lib.mat_copy(matB)


print('\n Using the LU decomposition method we get the solution:')
lib.print_mat(lib.LU_solve(matAcopy1,matB)) #change of matA is fine as we dont have any more use; moreover LU works like that to save space.

X1,steps1 = lib.solve_GS(matAcopy2, matBcopy1, 0.000001)
print('\n Using the Gauss-Seidel method with precision 10^(-6), we get the solution in',steps1,'steps as:\n(To see the precision I have display upto 8 decimal points)')
lib.print_mat2(X1)

X2,steps2 = lib.solve_Jacobi(matA, matB, 0.000001)
print('\n Using the Jacobi method with precision 10^(-6), we get the solution in',steps2,'steps as:\n(To see the precision I have display upto 8 decimal points)')
lib.print_mat2(X2)

######-----  OUTPUT  -----######
'''
These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:
[    4.0000    0.0000    4.0000    10.0000     1.0000   ]
[    0.0000    4.0000    2.0000     0.0000     1.0000   ]
[    2.0000    5.0000    1.0000     3.0000    13.0000   ]
[   11.0000    3.0000    0.0000     1.0000     2.0000   ]
[    3.0000    2.0000    7.0000     1.0000     0.0000   ]

and B is
[   20.0000   ]
[   15.0000   ]
[   92.0000   ]
[   51.0000   ]
[   15.0000   ]


 Using the LU decomposition method we get the solution:
[   2.9792   ]
[   2.2156   ]
[   0.2113   ]
[   0.1523   ]
[   5.7150   ]


 Using the Gauss-Seidel method with precision 10^(-6), we get the solution in 12 steps as:
(To see the precision I have display upto 8 decimal points)
[   2.97916509   ]
[   2.21559968   ]
[   0.21128403   ]
[   0.15231701   ]
[   5.71503357   ]


 Using the Jacobi method with precision 10^(-6), we get the solution in 57 steps as:
(To see the precision I have display upto 8 decimal points)
[   2.97916496   ]
[   2.21559926   ]
[   0.21128373   ]
[   0.15231661   ]
[   5.71503326   ]
'''