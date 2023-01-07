import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input1.txt'))  #getting those variables into this code


matA2 = matA.copy() #taking a copy for safety

inv = lib.invmat_LU(matA2.data) #taking the matrix data in primal form to function. See class mat
print("The inverse of the matrix is:")
lib.print_mat2(inv)

######-----  OUTPUT  -----######
'''
The inverse of the matrix is:
[   -0.71    2.53     2.43    0.97    -3.90   ]
[   -0.19    0.31     0.28    0.06    -0.29   ]
[   0.02     0.37     0.29    0.05    -0.29   ]
[   0.27    -0.13     0.13    -0.14    0.45   ]
[   0.78    -2.88    -2.68    -0.70    4.23   ]
'''