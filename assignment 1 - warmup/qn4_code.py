# Matrix multiplication and Dot product of Column vectors

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 1 - warmup/qn4_input.txt'))  #getting those variables into this code


print('AB is')
lib.print_mat(lib.mat_mult(A,B))       #  printmat is a function I wrote for printing nested list matrix.
print('BC is')                    #  It positions the matrix elements neatly in rows and columns. See mylibrary.py for details
lib.print_mat(lib.mat_mult(B,C))
print('D.C is')
print(lib.mat_dot(D,C))


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