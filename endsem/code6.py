import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input6.txt'))  #getting those variables into this code

#finding the eigenvectors and eigenvalues using rayleigh method
eval,evec,steps = lib.eigen_rayleigh(A,guess,tolerance)

#printing results
print("The guess vector was taken as:")
guess.table(decimals = 2)
print("The result was achieved within the {} steps.\nThe dominant eigen value is {:.4f}.\nThe dominant normalized eigen-vector is:".format(steps,eval))
evec.table(decimals = 4)
######-----  OUTPUT  -----######
'''
The guess vector was taken as:
[   1.00   ]
[   1.00   ]
[   1.00   ]
[   1.00   ]

The result was achieved within the 9 steps.
The dominant eigen value is 8.0004.
The dominant normalized eigen-vector is:
[   -0.1981  ]
[   0.6932   ]
[   0.6930   ]
[   0.0000   ]
'''