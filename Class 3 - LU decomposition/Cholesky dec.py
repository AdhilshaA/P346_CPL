import mylibrary as lib

def Chol_dec(A):
    #function that performs the Cholesky decomposition on A and returns L (Lower filled) when A = (L)(Ltranspose)

    #if detA is 0 then dont , add feauture later

    #IF NOT SYMMETRIC, EXIT.
    if lib.check_symmetry(A) == False:
        print('Matrix not symmetric!')
        return None
    
    from math import sqrt

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
    
    # for row in range(n):
    #     for col in range(row + 1,n):
    #         A[row][col] = 0
        
    return A

def Cholesky_solve(A,B): 
    #solves AX = B using cholesky DEcomposition

    A = Chol_dec(A)
    if A is None:
        print('Cholesky Solve not possible!')
        return None

    # Finding Y from (L)(Y) = B by backward substitution

    # Finding X from (Lt)(X) = (Y)

    return
A1 = [[4,12,-16],[12,37,-43],[-16,-43,98]]
A = [[3,-1,2],[-1,2,-1],[2,-1,4]]
B = [[8],[-5],[11]]
lib.print_mat(Cholesky_solve(A,B))
