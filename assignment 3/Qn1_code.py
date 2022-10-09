# Solving The given set of euations using Gauss-Jordon elimination and LU decomposition.

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 3/qn1_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# matA     :  matrix A
# matB     :  matrix B
# matAcopy : copy of matrix A for extended use


print('These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:')
lib.print_mat(matA)
print('and B is')
lib.print_mat(matB)

#taking a copy of matA (changes will be linked if simply assigned)
matAcopy = lib.mat_copy(matA)

print('\nUsing Gauss Jordon to solve this, we get the solution:')
lib.print_mat(lib.solve_GJ(matAcopy,matB))

print('\n Using the LU decomposition method we get the solution:')
lib.print_mat(lib.LU_solve(matA,matB)) #change of matA is fine as we dont have any more use; moreover LU works like that to save space.

######-----  OUTPUT  -----######
'''
These equations are taken in the form matA.X = matB where X will be the solution matrix and A is:
[    1.0000    -1.0000     4.0000    0.0000     2.0000     9.0000   ]
[    0.0000     5.0000    -2.0000    7.0000     8.0000     4.0000   ]
[    1.0000     0.0000     5.0000    7.0000     3.0000    -2.0000   ]
[    6.0000    -1.0000     2.0000    3.0000     0.0000     8.0000   ]
[   -4.0000     2.0000     0.0000    5.0000    -5.0000     3.0000   ]
[    0.0000     7.0000    -1.0000    5.0000     4.0000    -2.0000   ]

and B is
[   19.0000   ]
[    2.0000   ]
[   13.0000   ]
[   -7.0000   ]
[   -9.0000   ]
[    2.0000   ]


Using Gauss Jordon to solve this, we get the solution:
[   -1.7618   ]
[    0.8962   ]
[    4.0519   ]
[   -1.6171   ]
[    2.0419   ]
[    0.1518   ]

 Using the LU decomposition method we get the solution:
[   -1.7618   ]
[    0.8962   ]
[    4.0519   ]
[   -1.6171   ]
[    2.0419   ]
[    0.1518   ]
'''