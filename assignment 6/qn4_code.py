# question 4 code and output

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 6/qn4_input.txt'))  #getting those variables into this code

###--  INPUTS and meaning  --###
# A      : The matrix in question
# x0     : The initial guess for the eigen-vector
# eval   : eigen value result
# evec   : eigen vector result
# steps  : no. of steps taken

#finding the eigenvectors and eigenvalues using rayleigh method
eval,evec,steps = lib.eigen_rayleigh(A,x0,0.0001)

#printing results
print("The guess vector was taken as:")
x0.table(decimals = 2)
print("The result was acheived within the {} steps.\nThe dominant eigen value is {:.4f}.\nThe dominant eigen-vector is:".format(steps,eval))
evec.table(decimals = 4)

######-----  OUTPUT  -----######
'''
The guess vector was taken as:
[   2.00   ]
[   1.00   ]
[   2.00   ]

The result was acheived within the 10 steps.
The dominant eigen value is 4.0001.
The dominant eigen-vector is:
[   0.7071   ]
[   0.0001   ]
[   0.7071   ]
'''