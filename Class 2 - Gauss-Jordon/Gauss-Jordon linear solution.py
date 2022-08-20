def print_mat(A):
    for r in range(len(A)):
        for c in range(len(A[0])):
            print('{:.4f}   '.format(A[r][c]),end='')
        print('')  
    print('')

def solve_GJ(A,B):
    #solves linear equations using Gauss-Jordon method
    #takes the A and B matrix as input from the form A.X = B where X is the unknown matrix
    #returns solved X 

    #constructing augmented matrix 
    augmat = A
    for row in range(len(augmat)):
        augmat[row].append(B[row])
    
    for curr in range(len(augmat)): #curr takes the index of each column we are processing
        #row swap if zero
        if augmat[curr][curr] == 0:
            max_row = curr
            for row in range(curr + 1,len(augmat)):

                if abs(augmat[row][curr]) > abs(augmat[max_row][curr]):
                    max_row = row
            if max_row == curr: #if max elemnt is still zero, max_row is not changed; no unique solution
                return None
            augmat[curr],augmat[max_row] = augmat[max_row], augmat[curr]

        #making the pivot element 1
        if augmat[curr][curr] != 1:
            pivot_term = augmat[curr][curr]
            for i in range(len(augmat[curr])):
                augmat[curr][i] = augmat[curr][i] / pivot_term

        #making others zero
        for i in range(0,len(augmat)):
            if i == curr: #skipping the pivot point
                continue
            if augmat[i][curr] != 0:
                lead_term = augmat[i][curr]
                for j in range(curr,len(augmat[i])): #elements before the curr column are zero in curr row, so no need to calculate
                    augmat[i][j] = augmat[i][j] - (augmat[curr][j] * lead_term)
        print_mat(augmat)
    solution = []
    for i in range(len(augmat)):
        solution.append([augmat[i][-1]]) #Taking last elements into a list to form column matrix
    return solution


A = [[0,1,1,-2],[1,2,-1,0],[2,4,1,-3],[1,-4,-7,-1]]
B = [-3, 2, -2, -19]

solution = solve_GJ(A,B)

print(solution)

print(None)
