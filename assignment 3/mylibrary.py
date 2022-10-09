# A library updated to all functions till the current assignment
from math import sqrt
import matplotlib.pyplot as plt

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

def mat_copy(A):
    #returns a copy of the matrix without any links in memory
    A1 = []
    for i in range(len(A)):
        A1.append(A[i][:]) #splicing done to avoid changes linking
    return A1

def print_mat(A):
    #prints matrix with floats upto 4 decimal points
    if A is None:
        print('None')
        return
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
            print(' ' * start,'{:.4f}'.format(A[i][j]),' ' * stop, end = '')
        print(' ]')
    print('')

def print_mat2(A):
    #prints matrix with floats upto 8 decimal points

    if A is None:
        print('None')
        return
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
            print(' ' * start,'{:.8f}'.format(A[i][j]),' ' * stop, end = '')
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

def check_symmetry(A):
    #Function to check symmetry of A, return True or False
    if len(A) != len(A[0]): #not square matix
        return False

    for i in range(len(A)):
        for j in range(i + 1, len(A[0])): #checking only off-diagonal elements

            if A[i][j] != A[j][i]: #symmetry condition False
                return False
    return True 


class myComplex:

  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def __str__(self): #for printing complex no. in (a + bi) format when called print on any class instance
    return '{} + ({})i'.format(self.real, self.imag)

  def __add__(self,z2): # Method to add it with z2 of same class by using + between the instances
    add_real = self.real + z2.real
    add_imag = self.imag + z2.imag
    z3 = myComplex(add_real, add_imag)
    return z3
  
  def __mul__(self,z2): # Method to multiply it with z2 of same class using * between instances
    mult_real = (self.real * z2.real) - (self.imag * z2.imag)
    mult_imag = (self.real * z2.imag) + (self.imag * z2.real)
    z3 = myComplex(mult_real, mult_imag)
    return z3
  
  def __abs__(self):  #method to find modulus by using abs() on the instance
    val = sqrt((self.real ** 2) + (self.imag ** 2))
    return val

def parse(file_name):
    # A function to parse data in a specific format. Read README file in the repository for more details
    with open(file_name) as file:
        lines = file.readlines()
    inputs = {}
    numlines = len(lines)
    line_index = 3
    while line_index < numlines:
        line_index += 2
        type_name = lines[line_index - 1].split()
        if type_name[0] == 'int':
            inputs[type_name[1]] = int(lines[line_index].split()[0])
            line_index += 1
            continue
        
        elif type_name[0] == 'float':
            inputs[type_name[1]] = float(lines[line_index].split()[0])
            line_index += 1
            continue

        elif type_name[0] == 'str':
            inputs[type_name[1]] = lines[line_index][:-1]
            line_index += 1
            continue
        
        elif type_name[0] == 'complex':
            real_imag = list(map(float,lines[line_index].split()))
            inputs[type_name[1]] = myComplex(real_imag[0], real_imag[1])
            line_index += 1
            continue

        elif type_name[0] == 'int_list':
            inputs[type_name[1]] = list(map(int,lines[line_index].split()))
            line_index += 1
            continue

        elif type_name[0] == 'float_list':
            inputs[type_name[1]] = list(map(float,lines[line_index].split()))
            line_index += 1
            continue

        elif type_name[0] == 'str_list':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(lines[line_index][:-1])
                line_index += 1

        elif type_name[0] == 'int_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(list(map(int,lines[line_index].split())))
                line_index += 1
        
        elif type_name[0] == 'float_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(list(map(float,lines[line_index].split())))
                line_index += 1

        elif type_name[0] == 'str_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(lines[line_index].split())
                line_index += 1
    
        else:
            return inputs

class randgen():
    def __init__(self,seed, a = 1103515245, c = 12345 ,m = 32768):
        self.term = seed
        self.a = a
        self.c = c
        self.m = m
    def gen(self):
        self.term = (((self.a * self.term) + self.c) % self.m)
        return self.term / self.m

def LCG(seed, length, a = 1103515245, c = 12345 ,m = 32768):
    # function for LCG that generates random numbers in range (0,1)
    #default a, c, m value set. can change in case specified.

    term = seed
    RNs = []

    for i in range(0,length):
        term = (((a * term) + c) % m) #applying eqn.
        RNs.append((term / m)) #scaling to the range(1)
    return RNs

def Randomwalk2D_sim(seed,steps,start = (0,0)):
    #simulates Random walk, return list of coordinates and prints a Random walk plot.

    Random_numbers = LCG(seed,steps * 2) #need two coordinates
    points = [start] #list of coordinates visited, stored as tuples
    for i in range(steps):
        x = points[i][0] + (2 * Random_numbers[i]) - 1
        y = points[i][1] + (2 * Random_numbers[(steps + i)]) - 1
        points.append((x,y))
    
    #graph formatting
    plt.title('Random walk with {} steps'.format(steps))
    plt.axhline(0,lw = 1,c = 'k')
    plt.axvline(0,lw = 1,c = 'k') 
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.plot([start[0]],[start[1]],'go',ms = 4) #plotting thte start point as green
    plt.plot([points[i][0] for i in range(steps+1)],[points[i][1] for i in range(steps+1)],'-bo',lw = '1',ms = 1, mec = 'k', mfc = 'b' )
    #points[i][0] is the (i)th x cordinate and points[i][1] is the (i)th y cordinate, then a list of each
    plt.plot([points[-1][0]],[points[-1][1]],'ro',ms = 3) #plotting the end point as red
    plt.show()
    return points


def rms_walk(walk):
    #calculating rms distance from a 2D walk

    steps = len(walk) - 1  #n steps = n + 1 coordinates
    sumof_dsquared = 0
    for i in range(1,steps):
        sumof_dsquared += (((walk[i][0] - walk[i-1][0]) ** 2) + ((walk[i][1] - walk[i-1][1]) ** 2))
        # eqn.                  (  x2   -   x1  ) ^ 2         +      (  y2   -   y1  ) ^ 2 
    rms = sqrt(sumof_dsquared / steps)
    return rms


def netdisplace_walk(walk):
    #caluculate the net displacement of walk

    netdis = sqrt(((walk[-1][0] - walk[0][0]) ** 2) + ((walk[-1][1] - walk[0][1]) ** 2))
    #  eqn.          (last x    -   first x) ^ 2    +    (last y    -   first y) ^ 2
    return netdis

def inv_mat_GJ(A):

    if len(A) != len(A[0]): #if not square matrix, exit
        return None

    n = len(A) #the dimension of matrix will be n*n
    I = []
    for row in range(n):
        I.append(list())
        for col in range(n):
            if col == row:
                I[row].append(1)
            else:
                I[row].append(0)
    
    
    for curr in range(n): #curr takes the index of each column we are processing
        #row swap if zero
        if A[curr][curr] == 0:
            max_row = curr
            for row in range(curr + 1,n):

                if abs(A[row][curr]) > abs(A[max_row][curr]):
                    max_row = row
            if max_row == curr: #if max elemnt is still zero, max_row is not changed; no unique solution
                return None
            A[curr],A[max_row] = A[max_row], A[curr]
            I[curr],I[max_row] = I[max_row], I[curr]
        #making the pivot element 1
        if A[curr][curr] != 1:
            pivot = A[curr][curr]
            for i in range(n):
                A[curr][i] = A[curr][i] / pivot
                I[curr][i] = I[curr][i] / pivot

        #making others zero
        for i in range(0,n):
            if i == curr: #skipping the pivot point
                continue
            if A[i][curr] != 0:
                lead = A[i][curr]
                for j in range(0,n):
                    A[i][j] = A[i][j] - (A[curr][j] * lead)
                    I[i][j] = I[i][j] - (I[curr][j] * lead)

    return I

def solve_GJ(A,B):
    #solves linear equations using Gauss-Jordon elimination method
    #takes the A and B matrix as input from the form A.X = B where X is the unknown matrix
    #returns solved X 
    
    n = len(A) #the dimension is a frequently used value, therefore stored.
    
    #convering matrix A into augmented matrix 
    for row in range(n):
        A[row].append(B[row][0])
    
    for curr in range(n): #curr takes the index of each column we are processing
        #row swap if zero
        if A[curr][curr] == 0:
            max_row = curr
            for row in range(curr + 1,n):

                if abs(A[row][curr]) > abs(A[max_row][curr]):
                    max_row = row
            if max_row == curr: #if max elemnt is still zero, max_row is not changed; no unique solution
                return None
            A[curr],A[max_row] = A[max_row], A[curr]


        #making the pivot element 1
        if A[curr][curr] != 1:
            pivot_term = A[curr][curr]
            for i in range(n + 1):
                A[curr][i] = A[curr][i] / pivot_term
     
        #making others zero
        for i in range(0,n):
            if i == curr: #skipping the pivot point
                continue
            if A[i][curr] != 0:
                main_term = A[i][curr] 
                for j in range(curr,n + 1): #A[curr][j] is zero for j<curr, so no changes to the elements to the left in this row.
                    A[i][j] = A[i][j] - (A[curr][j] * main_term)

    solution = []
    for i in range(n):
        solution.append([A[i][-1]]) #Taking last elements into a list to form column matrix
    return solution

def mat_det(A):
    #matrix determinant using row echelon form
    n = len(A)
    rowswaps = 0 #no. of row swaps done
    if n != len(A[0]):
        print('Not a square matrix')
        return None
    for curr in range(n): #curr takes the index of each column we are processing
        #row swap if zero
        if A[curr][curr] == 0:
            max_row = curr
            for row in range(curr + 1,n):

                if abs(A[row][curr]) > abs(A[max_row][curr]):
                    max_row = row
            if max_row == curr: #if max elemnt is still zero, max_row is not changed; no unique solution
                print('The matrix is singular!')
                return None
            A[curr],A[max_row] = A[max_row], A[curr]
            rowswaps += 1

        #making others elements below lead term zero
        for i in range(curr + 1,n):
            if A[i][curr] != 0:
                main_term = A[i][curr] / A[curr][curr]
                for j in range(curr,len(A[i])): #A[curr][j] is zero for j<curr, so no changes to the elements to the left of curr in this row.
                    A[i][j] = A[i][j] - (A[curr][j] * main_term) 
    prdct = 1
    if rowswaps % 2 == 1:
        prdct = -1
    for i in range(n):
        prdct *= A[i][i]
    return prdct
    
def Chol_dec(A):
    #function that performs the Cholesky decomposition on A and returns (L and T_transpose superimposed matrix where the diagonal of both are same).


    #IF NOT SYMMETRIC, EXIT.
    if check_symmetry(A) == False:
        print('Non symmetric!')
        return None

    n = len(A)

    for row in range(n):
        for col in range(row,n):
            
            if row == col:
                sum = 0
                for i in range(row):
                    sum += (A[row][i] ** 2)
                A[row][row] = sqrt(A[row][row] - sum)
            else:
                sum = 0
                for i in range(row):
                    sum += (A[row][i] * A[i][col])
                A[row][col] = (A[row][col] - sum) / A[row][row]
                A[col][row] = A[row][col]

    return A

def forward_backward_cholesky(A,B):
    if A is None:
        print('Cholesky decomposition failed!')
        return None
    
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append((B[i][0]-sum) / A[i][i])

    X = Y
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]

    for i in range(n):
        X[i] = [X[i]]
    
    return X

def solve_Cholesky(A,B): 
    #solves AX = B using cholesky Decomposition

    A = Chol_dec(A)
    if A is None:
        print('Cholesky Solve not possible!')
        return None

    
    return forward_backward_cholesky(A,B)

def LU_dec(A):
    # performs doolittle method LU decompostition of A and return a (L and U superimposed matrix where L_ii = 1 is understood).

    n = len(A) #matrix dimension
    if n != len(A[0]): #checking if the given matrix is a square matrix
        print('Not square!')
        return None
    
    # checking if the determinant of A matrix is 0, if so no unique solution exist
    A1 = mat_copy(A)
    if mat_det(A1) == 0:
        print('Singular matrix!')
        return None
    
    #making leading submatrices non-zero by pivoting
    for i in range(n-1): #last sub matrix is the matarix itself, so avoided.
        
        #constructing submatrix
        submat = []
        for j in range(i+1):
            submat.append(A[j][:i+1])
        
        if mat_det(submat) == 0: #if submat determinant is zero, the last row is replaced with the next rows until the det is non zero. 
            curr = i + 1
            flag = 0
            while curr != n:
                submat[i] = A[curr][:i+1]
                if mat_det(submat) != 0:
                    flag = 1
                    break
                else:
                    curr += 1
            if flag == 0:
                print('Reordering incomplete! submat of order',i+1,'has determinant zero while the matrix itself is non singular.') #this is not supposed to happen, still added in case of any unexpected exception.
                return None
            A[i],A[curr] = A[curr],A[i] #then the original A matrix is changed as per the non-singular submatrix swap.

    for j in range(n):
        for i in range(1,n):
            if i <= j:
                sum = 0
                for k in range(0,i):
                    sum += (A[i][k] * A[k][j])
                A[i][j] = A[i][j] - sum
            else:
                sum = 0
                for k in range(0,j):
                    sum += (A[i][k] * A[k][j])
                A[i][j] = (A[i][j] - sum) / A[j][j]
    return A

    
def forward_backward_LU(A,B):

    if A is None: #checking if LU decomposition failed
        print('LU decomposition failed!')
        return None

    Y = [] # the intermidiate Y matrix where Y = U.X .thus Y is also be in equation L.Y = B, we solve this first
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append(B[i][0]-sum)
    
    #now we solve U.X = Y
    X = Y[:]
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]

    #making X into column matrix
    for i in range(n):
        X[i] = [X[i]]

    return X

def LU_solve(A,B):
    return forward_backward_LU(LU_dec(A),B) #Calling forward backward substitution of LU on LU decomposed A and B




def solve_GS(A,B,tolerance):
    #solving linear equations (A.X=B) using Gauss-seidel method with tolerace, where X is the solution. return solution X and number of steps in which it is done
    n = len(A)

    #checking if its symmetric
    if check_symmetry(A) == False:
        print('matrix not symmetric')
        return None

    #diagonally dominant
    

    X = list([0] for i in range(n)) #guess
    
    for steps in range(100):
        flag = 1
        for i in range(n):
            sum = 0
            for j in range(i):
                sum += (A[i][j] * X[j][0])
            for j in range(i+1,n):
                sum += (A[i][j] * X[j][0])
            temp = (B[i][0] - sum) / (A[i][i])
            if abs(abs(temp) - abs(X[i][0])) > tolerance:
                flag = 0
            X[i][0] = temp
        if flag == 1:
            return X,steps + 1
    print('Eqn not solved after 100 steps')
    return None,100