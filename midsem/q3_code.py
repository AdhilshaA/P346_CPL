# Question 3 code and output

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('midsem/msem_gs.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# A      :  matrix A
# B      :  matrix B
# X     : solution in Gauss-seidel solve
# steps : steps taken in Gauss-Seidel solve


X,steps = lib.solve_GS(A, B, 0.000001) #solving the given equation
print('\n Using the Gauss-Seidel method with precision 10^(-6), we get the solution in',steps,'steps as:\n(To see the precision I have display upto 8 decimal points)')
lib.print_mat2(X)

######-----  OUTPUT  -----######
'''
Using the Gauss-Seidel method with precision 10^(-6), we get the solution in 13 steps as:
(To see the precision at work, I have display upto 8 decimal points)
[    1.49999983   ]
[   -0.50000000   ]
[    2.00000000   ]
[   -2.49999991   ]
[    1.00000000   ]
[   -1.00000000   ]
'''