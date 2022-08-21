# A library updated to all functions till the current assignment

def sum_odd(n):
    #returns sum of n odd numbers
    sum = 0
    for i in range(1,2 * n,2):
        sum += i
    return sum

def fact(n):
    #returns n factorial
    factorial = 1
    for i in range(n,1,-1):
        factorial = factorial * i
    return factorial
    
def sum_ap(start,cd,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an AP specified by first term and common difference
    for i in range(n):
        sum += term
        term += cd
    return sum

def sum_hp(start,cd,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an HP specified by first term and common difference of its corresponding AP
    for i in range(n):
        sum += 1 / term
        term += cd
    return sum

def sum_gp(start,cr,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an GP specified by first term and common ratio
    for i in range(n):
        sum += term
        term = term * cr
    return sum

def mat_mult(A,B): 
    #finding AB matrix

    #verifiying matrix multiplication is possible (cols of A ?= rows of B)
    if len(A[0]) != len(B):
        return None

    #creating the sum matrix with zeroes
    sum = []
    for i in range(len(A)): #no. of row in sum is row of A
        sum.append(list(0 for i in range( len(B[0]) ))) #no. of col in sum is col of B

    #filling the sum matrix
    for row in range(len(sum)):
        for col in range(len(sum[0])):
            #finding each term in sum matrix
            temp_sum = 0
            for i in range(len(B)):
                temp_sum += A[row][i] * B[i][col]
                sum[row][col]=temp_sum

    return sum

def printmat(A):
    #printing a given matrix A
    maxs = []
    for j in range(len(A[0])):  #finding maximum integer length in each column and saving to maxs list
        max = 0
        for i in range(len(A)):
            length = len(str(int(A[i][j])))
            if max < length:
                max = length
        maxs.append(max + 2)   #adding 2 for equal space left and right to the maximum long term
    
    #printing
    for i in range(len(A)):
        print('[ ',end='')
        for j in range(len(A[0])):
            val = A[i][j]
            length = len(str(int(val))) 
            if int(val) == 0 and val < 0: length += 1
            spaces = maxs[j] - length
            stop = (spaces) // 2       #finding how many spaces before and after each term to align centrally in each column
            start = spaces - stop
            print(' ' * start,'{:.2f}'.format(A[i][j]),' ' * stop, end = '')
        print(' ]')
    print('')
      
def mat_dot(A,B):
    #returns the dot product of two column matrices
    if len(A) != len(B) or len(A[0]) != 1 or len(B[0]) != 1: #works only if column matrice sof same length
        return None
    dotprdct = 0
    for row in range(len(A)):
        dotprdct += (A[row][0] * B[row][0])
    return dotprdct

