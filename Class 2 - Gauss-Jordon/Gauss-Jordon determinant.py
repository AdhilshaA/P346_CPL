import mylibrary as lib

def mat_det(A):
    n = len(A)
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

        #making others zero
        for i in range(curr + 1,n):
            if A[i][curr] != 0:
                lead_term = A[i][curr]/A[curr][curr]
                for j in range(curr,len(A[i])): #elements before the curr column are zero in curr row, so no need to calculate
                    A[i][j] = A[i][j] - (A[curr][j] * lead_term)
    prdct = 1
    for i in range(n):
        prdct *= A[i][i]
    return prdct

A = [[2,-3,1.4],[2.5,1,-2],[-0.8,0,3.1]]
print(mat_det(A))