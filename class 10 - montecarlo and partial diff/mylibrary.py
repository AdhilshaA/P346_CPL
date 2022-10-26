# A library updated to all functions till the current assignment
from math import sqrt
import math as m
import matplotlib.pyplot as plt
from numpy import square
    
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

def print_mat(A):
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

def mat_copy(A):
    #returns a copy of the matrix without any links in memory
    A1 = []
    for i in range(len(A)):
        A1.append(A[i][:]) #splicing done to avoid changes linking
    return A1

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
        file.close()
    inputs = {}
    numlines = len(lines)
    line_index = 3
    while bool(lines[line_index].split()) is False:
        line_index += 1
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

        elif type_name[0] == 'xydata':
            inputs[type_name[1]] = []
            inputs[type_name[2]] = []
            while lines[line_index][0] != '#':
                lines[line_index] = lines[line_index].split()
                try:
                    inputs[type_name[1]].append(float(lines[line_index][0]))
                    inputs[type_name[2]].append(float(lines[line_index][1]))
                except:
                    print('{} input inproper! check {}'.format(type_name[0],file_name))
                line_index += 1

        elif type_name[0] == 'xysigdata':
            inputs[type_name[1]] = []
            inputs[type_name[2]] = []
            inputs[type_name[3]] = []
            while lines[line_index][0] != '#':
                lines[line_index] = lines[line_index].split()
                try:
                    inputs[type_name[1]].append(float(lines[line_index][0]))
                    inputs[type_name[2]].append(float(lines[line_index][1]))
                    inputs[type_name[3]].append(float(lines[line_index][2]))
                except:
                    print('{} input inproper! check {}'.format(type_name[0],file_name))
                line_index += 1

        else:
            return inputs

class randgen():
    def __init__(self,seed, a = 1103515245, c = 12345 ,m = 32768, interval=(0,1)):
        #initiation of data input
        self.term = seed
        self.a = a
        self.c = c
        self.m = m
        self.interval = interval

    def gen(self):
        #generates a random number in the interval (0,1)
        self.term = (((self.a * self.term) + self.c) % self.m)
        return (self.interval[0] + (self.term * ((self.interval[1]-self.interval[0])/ self.m)))

    def genlist(self,length):
        # returns a list of 'n' random numbers in the interval (0,1) where 'n' is 'length'.
        RNs = []
        for i in range(length):
            self.term = (((self.a * self.term) + self.c) % self.m)
            RNs.append(self.interval[0] + (self.term * ((self.interval[1]-self.interval[0]) / self.m)))
        return RNs

def Randomwalk2D_sim(seed,steps,start = (0,0)):
    #REWRITE
    #simulates Random walk, return list of coordinates and prints a Random walk plot.

    random = randgen(seed)
    # Random_numbers = random.genlist(steps * 2) #need two coordinates
    points = [start] #list of coordinates visited, stored as tuples
    for i in range(steps):
        x = points[i][0] + (2 * random.gen()) - 1
        y = points[i][1] + (2 * random.gen()) - 1
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

def solve_checklinearform(A,B):

    #checking if A is square matrix
    if len(A[0]) != len(A):
        print('A is not square matrix')
        return False

    #checking B is a column matrix
    for i in range(len(B)):
        if len(B[i]) != 1:
            print('B is not a column matrix')
            return False

    #checking if B has same number of elements as rows of A
    if len(A) != len(B):
        print('B is not compatible with A dimensions') 
        return False
    return True

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

    #checking if matA and matB properly represent linear equation form
    if solve_checklinearform(A,B) == False:
        print('The matrices doesnt properly represent linear eqns form')
        return None
    
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

    #Performing the decomposition
    for row in range(n):
        for col in range(row,n): #I am finding the L_transpose and copying elements to the lower part to complete the decomposition
            
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
                A[col][row] = A[row][col] #As the matrix isresultant L-L_transpose matrix is symmetric

    return A

def forward_backward_cholesky(A,B): 
    # Performs forward substitution and backward substitution given an (L-Ltranspose superimposed) matrix A and and matrix B. returns X.
    if A is None:
        print('Cholesky decomposition failed!')
        return None
    
    #forward substition
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append((B[i][0]-sum) / A[i][i])

    #backward substitution
    X = Y # Here X and Y can be stored in the same matrix due to the way of calculation, for the sake understanding I have made a name X.
          # By assigning a matrix like this, only a another name for the same list is created.
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]

    for i in range(n):
        X[i] = [X[i]]
    
    return X

def solve_Cholesky(A,B): 
    #solves AX = B using cholesky Decomposition. Returns X.

    #checking if matA and matB properly represent linear equation form
    if solve_checklinearform(A,B) == False:
        print('The matrices doesnt properly represent linear eqns form')
        return None
    
    A = Chol_dec(A)
    if A is None:
        print('Cholesky Solve not possible!')
        return None

    return forward_backward_cholesky(A,B) #Calling forward backward substitution on Cholesky decomposed A and B and returning the solution

def LU_dec(A,B):
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
            B[i],B[curr] = B[curr],B[i] #then the original B matrix is changed as per the non-singular submatrix swap.

    #performing LU decompostion
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
    return A,B

    
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
    X = Y
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
    #solves the set of linear eqn.s in the form of AX = B using LU decomposition method

    #checking if matA and matB properly represent linear equation form
    if solve_checklinearform(A,B) == False:
        print('The matrices doesnt properly represent linear eqns form')
        return None

    #PErforming the LU decomposition
    A,B = LU_dec(A,B)

    return forward_backward_LU(A,B) #Calling forward backward substitution of LU on LU decomposed A and B and returning the solution

def mat_makeSDD(A,B):
    #makes a strictly diagonally dominant matrix A after row swaps on A and the same row operations on B. returns both.

    n = len(A)
    

    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i:
                sum += abs(A[i][j])
        if abs(A[i][i]) > sum: #checkis if leading element is strictly dominant over others in the row. if so, continue to the next row.
            # print('row',i,'is fine')
            continue
        else: #else, check for the same position dominance in next rows.
            curr = i + 1
            flag = 0
            while curr < n:
                sum = 0
                for j in range(n):
                    if j != i:
                        sum += abs(A[curr][j])
                # print('sum is',sum)
                if abs(A[curr][i]) > sum:
                    flag = 1
                    break
                else:
                    curr += 1
            if flag == 0: #if no dominant term was found in the rows below, it cannot be made strictly diagonally dominant matrix.
                # print('failed at',i)          #it is so, from the fact that a row/column cannot have 2 diagonally dominant terms, no row/column swap can separate those.
                return None,None
            else:
                A[i],A[curr] = A[curr],A[i]
                B[i],B[curr] = B[curr],B[i]
    return A,B

def solve_GS(A,B,tolerance):
    #solving linear equations (A.X=B) using Gauss-seidel method with tolerace, where X is the solution. return solution X and number of steps in which it is done
    
    #checking if matA and matB properly represent linear equation form
    if solve_checklinearform(A,B) == False:
        print('The matrices doesnt properly represent linear eqns form')
        return None    
    
    n = len(A)

    #trying to make strictly diagonally dominant , now DISABLED
    # A,B= mat_makeSDD(A,B)   
    # if A is None:
    #     print('matrix cannot be made strictly diagonally dominant\nGauss-Seidel method exited!')
    

    X = list([0] for i in range(n)) # initial guess
    
    for steps in range(100):
        flag = 1
        for i in range(n):
            sum = 0
            for j in range(i):
                sum += (A[i][j] * X[j][0])
            for j in range(i+1,n):
                sum += (A[i][j] * X[j][0])
            temp = (B[i][0] - sum) / (A[i][i])
            if abs((temp) - (X[i][0])) > tolerance: #checks the tolerance at each new value
                flag = 0
            X[i][0] = temp
        if flag == 1:
            return X,steps + 1
    print('Eqn not solved after 100 steps')
    return None,100

def solve_Jacobi(A,B,tolerance):

    #checking if matA and matB properly represent linear equation form
    if solve_checklinearform(A,B) == False:
        print('The matrices doesnt properly represent linear eqns form')
        return None

    #trying to make strictly diagonally dominant
    A,B= mat_makeSDD(A,B)
    if A is None:
        print('matrix cannot be made strictly diagonally dominant\nJacobi method exited!')

    n = len(A)

    currX = [0] * n # initial guess
    newX = currX[:] # new guess, to be processed

    steps = 0
    while steps < 150: #max steps kept high for 10^-6 precision
        
        #finding new X
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j: sum += (A[i][j] * currX[j])
            newX[i] = (B[i][0] - sum) / A[i][i]

        #comparing newX and currentX against tolerance
        flag = 1 #assumed true
        for i in range(n):
            if abs(newX[i]-currX[i]) > tolerance:
                flag = 0 #looking for exception
                steps += 1
                currX = newX[:]
                break
        
        if flag == 1:
            #converting the answer to column matrix
            for i in range(n):
                newX[i] = [newX[i]]
            return newX, steps
    #if not done in 150 steps, return None
    print('After more than 150 iterations, it is not solved!')
    return None, steps

def root_bracketing(f,a,b):
    for i in range(12):
        if f(a) * f(b) < 0:
            return a,b
        if abs(f(a)) < abs(f(b)):
            # print("left")
            temp = a
            a = a - (1.5*(b-a))
            b = temp
            # print('a={},b={}'.format(a,b))
        else:
            # print("right")
            temp = b
            b = b + (1.5*(b-a))
            a = temp
            # print('a={},b={}'.format(a,b))
    if abs(f(a)) < abs(f(b)):
        return root_bracketing(a - (1.5*(b-a)),b)
    else:
        return root_bracketing(a,b + 1.5*(abs(b-a)))

def root_bisection(f,a,b,epsilon,delta,details = False):

    # bracketing the root if not already done
    a,b = root_bracketing(f,a,b)

    steps = 1

    #if details kept true, it will return a list of the values converging to the required root
    if details is True: 
        tables = []
        while steps<100:
            if (a-b) < epsilon:
                if abs(f(a)) < delta or abs(f(b)) < delta:
                    return tables
            c = (a + b) / 2
            tables.append(c)
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            steps += 1
        print('Not converging after 100 steps, terminated')
        return None

    #if details kept False (default), it will return the root and the number of steps taken
    else: 
        while steps<100:
            if (a-b) < epsilon:
                if abs(f(a)) < delta or abs(f(b)) < delta:
                    return (a+b)/2,steps
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            steps += 1
        print('Not converging after 100 steps, terminated')
        return None,None

def root_newtonraphson(f,df,x0,epsilon,delta,details = False):
    #returns the root for function f from guess x0 with epsilon tolerance for closeness to root and delta tolerance for f's closeness to zero at that root
    if details is True:
        tables = []
        steps = 1
        while steps < 151: #100 steps as max. limit

            #new guess
            x1 = x0 - (f(x0)/df(x0))
            tables.append(x1)
            #checking is guess is good enough
            if abs(x1 - x0) < epsilon and f(x1) < delta:
                return x1,steps

            #preparing for next iteration
            x0 = x1
            steps += 1
        
        print('Not converging after 151 steps, terminated')
        return None
    else:
        steps = 1
        while steps < 151: #100 steps as max. limit

            #new guess
            x1 = x0 - (f(x0)/df(x0))

            #checking is guess is good enough
            if abs(x1 - x0) < epsilon and f(x1) < delta:
                return x1,steps

            #preparing for next iteration
            x0 = x1
            steps += 1
        
        print('Not converging after 151 steps, terminated')
        return None,None

def root_regulafalsi(f,a,b,epsilon,delta,details = False):
    
    #bracketing the root if not done
    a,b = root_bracketing(f,a,b)

    # doing the first run, as no comparison is done here
    c = b - (((b-a)*f(b))/(f(b) - f(a)))
    if f(c)*f(a) < 0:
        b = c
    else:
        a = c

    #if details kept true, it will return a list of the values converging to the required root
    if details is True:
        #adding the c from first step
        tables = []
        tables.append(c)

        steps = 2
        while steps < 100:
            oldc = c
            c = b - (((b-a)*f(b))/(f(b) - f(a)))
            tables.append(c)
            if f(c)*f(a) < 0:
                b = c
            else:
                a = c
            if abs(c-oldc) < epsilon and f(c) < delta:
                return tables
            oldc = c
            steps += 1
        print('Not converging after 100 steps, terminated')
        return None,None
    
    #if details kept False (default), it will return the root and the number of steps taken
    else:
        steps = 2
        while steps < 100:
            oldc = c
            c = b - (((b-a)*f(b))/(f(b) - f(a)))
            if f(c)*f(a) < 0:
                b = c
            else:
                a = c
            if abs(c-oldc) < epsilon and f(c) < delta:
                return c,steps
            oldc = c
            steps += 1
        print('Not converging after 100 steps, terminated')
        return None,None


def lagrange_intrapolate(X,Y,x1):
    N = len(X)
    if N != len(Y):
        print('data mismatch')
        return None
    sum = 0
    for i in range(N):
        prdct = 1
        for k in range(N):
            if k == i:
                continue
            prdct = prdct * ((x1 - X[k])/(X[i]-X[k]))
        sum += prdct * Y[i]
    return sum


def px_deflate(px, root):
    # here px is in the format a0,a1,a2,..an where n is the polynomial power.
    n = len(px)
    #Here, the passed 'root' is a verified root from main body with a certain tolerance, therefore checking not done.
    if n == 1:
        print('P(x) doesnt contain any x: deflation exited!')
        return None
    n -= 1
    if px[n] != 1:
        lead = px[n]
        for i in range(len(px)):
            px[i] = px[i] / lead
    n -= 1
    while n >= 0:
        px[n] = (px[n+1] * root) + px[n]
        n -= 1
    return px[1:]



def px_derivative(px):
        # here px is in the format a0,a1,a2,..an where n is the polynomial power.

    n = len(px)
    i = 1
    while i != n:
        px[i] = px[i] * (i)
        i += 1
    return px[1:]

def px_value(px,x):
        # here px is in the format a0,a1,a2,..an where n is the polynomial power.

    sum = 0
    i = 0
    n = len(px)
    while i != n:
        sum+= (px[i] * (x**i))
        i += 1
    return sum

def root_laguire(px,guess,tolerance):
        # here px is in the format a0,a1,a2,..an where n is the polynomial power.

    roots = []
    steps = 1
    N = len(px) - 1
    n = N
    while steps <= N:
        if abs(px_value(px,guess)) < tolerance:
            print('{}th root, {:.4f}, is found in 0 steps.'.format(steps,guess))
            steps += 1
            roots.append(guess)
            px = px_deflate(px,guess)
            n -= 1
            continue
        # print('Finding the {}th root for {}'.format(steps,px))
        dpx = px_derivative(px[:])
        ddpx = px_derivative(dpx[:])
        i = 1
        theguess = guess
        while True:
            g = px_value(dpx,theguess)/px_value(px,theguess)
            h = (g**2) - (px_value(ddpx,theguess)/px_value(px,theguess))
            if g < 0:
                a = (n / (g - m.sqrt((n-1)*((n*h)-(g**2)))))
            else:
                a = (n / (g + m.sqrt((n-1)*((n*h)-(g**2)))))
            # print('a is',a)
            newguess = theguess - a
            # print(px_value(px,theguess),'and',px_value(px, newguess))
            
            if i < 26 :
                # if abs(a) < tolerance and px_value(px,newguess) < tolerance:
                if px_value(px,newguess) < tolerance:
                    print('{}th root, {:.4f}, is found in {} steps.'.format(steps,newguess,i))
                    steps += 1
                    roots.append(newguess)
                    px = px_deflate(px,newguess)
                    n -= 1
                    break
                # else:
                #     print('Guess discarded.\n')

            else:
                print('The guess for {} th root was not found in 25 steps'.format(steps))
                return None
            theguess = newguess
            i += 1
    return roots

def fit_polyleastsq(dataX,dataY,order,datasigma=None):


    n = len(dataX) #no. of datasets

    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None

    matX = [[0]*(order+1) for i in range(order+1)]

    #completing matX
    matX[0][0] = n
    for i in range(1,(2 * order) + 1):
        sum = 0
        for j in range(n):
            sum += (dataX[j]**i)
        if i <= order:
            startX = 0
            startY = i
            while startY >= 0:
                # print('p',startX,startY)

                matX[startX][startY] = sum
                startY -= 1
                startX += 1
        else:
            
            startX = i - order
            startY = order
            while startX <= order:
                # print('p',startX,startY)
                matX[startX][startY] = sum
                startY -= 1
                startX += 1

    matY = []
    sum = 0
    for i in range(n):
        sum += dataY[i]
    matY.append([sum])
    for i in range(1,order+1):
        sum = 0
        for j in range(n):
            sum += (dataX[j]**i)*dataY[j]
        matY.append([sum])

    # print(matX,matY)
    px = solve_GJ(matX,matY)
    for j in range(len(px)):
        px[j] = px[j][0]

    return px

def fit_linearleastsq(dataX,dataY,datasigma=None):
    #returns the linear equation in polynomial form where the line is a0+a1x

    n = len(dataX) #no. of datasets

    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None
    Sxx = 0
    Syy = 0 #for pearson R square calc.
    Sxy = 0
    Sx = 0
    Sy = 0

    if datasigma is None:
        S = n
        for i in range(n):
            Sxx += dataX[i]**2
            Syy += dataY[i]**2
            Sxy += dataX[i] * dataY[i]
            Sx += dataX[i]
            Sy += dataY[i]

    else:
        S = 0
        for i in range(n):
            S += 1/(datasigma[i]**2)
            Sxx += (dataX[i]**2)/(datasigma[i]**2)
            Syy += (dataY[i]**2)/(datasigma[i]**2)
            Sxy += (dataX[i] * dataY[i])/(datasigma[i]**2)
            Sx += dataX[i]/(datasigma[i]**2)
            Sy += dataY[i]/(datasigma[i]**2)

    delta = (S*Sxx)-(Sx**2)
    a0 = ((Sxx*Sy) - (Sx*Sxy)) / delta
    a1 = ((Sxy*S) - (Sx*Sy)) / delta

    R2 = (((n*Sxy) - (Sx*Sy))**2)/(((n*Sxx)-(Sx**2)) * ((n*Syy)-(Sy**2)))

    return [a0,a1],R2


def px_graphdata(px,start,stop,number):
    step = (stop - start) / (number - 1)
    Xvalues = []
    Yvalues = []
    stop += step
    while start < stop:
        Xvalues.append(start)
        Yvalues.append(px_value(px,start))
        start += step
    return Xvalues, Yvalues

def integrate_midpoint(f,a,b,N):
    #integrates f over a to b by dividing to N parts

    step = (b - a) / N
    x = a + (step / 2)
    sum = 0
    for i in range(N):
        # print('x = ',x,'fx =',f(x))
        sum += (f(x))
        x += step
    sum *= step
    return sum
            
def integrate_trapezoidal(f,a,b,N):
    step = (b-a)/N
    sum = (f(a)+f(b))/2
    a += step
    for i in range(N-1):
        sum += f(a)
        a += step
    sum *= step
    return sum

def integrate_simpson(f,a,b,N):
    h = (b-a)/N
    sum = f(a)+f(b)+(4*f(a+(h/2)))
    a += h
    for i in range(N-1):
        sum += ((2*f(a)) + (4*f(a + (h/2))))
        a += h
    sum = (h/3)
    return sum

def fit_powerlaw(dataX,dataY):
    # fits the data given by dataX and dataY using (a*x^b) model
    # returns a,b and pearsons R square
    
    n = len(dataX) #no. of datasets

    #checking the data mismatch
    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None

    #convering to linear form data
    logxdata = []
    logydata = []
    for i in range(n):
        logxdata.append(m.log(dataX[i]))
        logydata.append(m.log(dataY[i]))
    
    
        #using least square fit for linear form
    px,prs = fit_linearleastsq(logxdata,logydata)

    #calculating the a and b from the linear polynomial solution
    a = m.exp(px[0])
    b = px[1]

    return a,b,prs

def fit_exponential(dataX,dataY):
    # fits the data given by dataX and dataY using (a*e^bx) model
    # returns a,b and pearsons R square

    n = len(dataX) #no. of datasets

    #checking data mismatch
    if len(dataY) != n:
        print("Data mismatch! exited!")
        return None

    #convering to linear form
    logydata = []
    for i in range(n):
        logydata.append(m.log(dataY[i]))
    
    #using least square fit for linear form
    px,prs = fit_linearleastsq(dataX,logydata) #prs is pearson r square

    #calculating the a and b from the linear polynomial solution
    a = m.exp(px[0])
    b = px[1]

    return a,b,prs

def powerlaw_data(a,b,start,stop,number):
    # gives the graph data for y = a*x^b between start and stop with "number" no. of points
    step = (stop - start) / (number - 1)
    Xvalues = []
    Yvalues = []
    stop += step
    while start < stop:
        Xvalues.append(start)
        Yvalues.append(a*(start**b))
        start += step
    return Xvalues, Yvalues


def exp_graphdata(a,b,start,stop,number):
    # gives the graph data for y = a*e^bx between start and stop with "number" no. of points
    step = (stop - start) / (number - 1)
    Xvalues = []
    Yvalues = []
    stop += step
    while start < stop:
        Xvalues.append(start)
        Yvalues.append(a*(m.exp(start*b)))
        start += step
    return Xvalues, Yvalues


            
