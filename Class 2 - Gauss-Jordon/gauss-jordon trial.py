A = [[0,1,1,-2],[1,2,-1,0],[2,4,1,-3],[1,-4,-7,-1]]
B = [-3, 2, -2, -19]

augmat = A
for row in range(len(augmat)):
    augmat[row].append(B[row])

#row swap if zero
if augmat[0][0] == 0:
    max_row = 0
    for row in range(1,len(augmat)):
        if abs(augmat[row][0]) >= abs(augmat[max_row][0]):
            max_row = row
    augmat[0],augmat[max_row] = augmat[max_row], augmat[0]

#making the pivot 1
if augmat[0][0] != 1:
    pivot_term = augmat[0][0]
    for i in range(len(augmat[0])):
        augmat[0][i] = augmat[0][i] / pivot_term

#making others zero
for i in range(1,len(augmat)):
    if augmat[i][0] != 0:
        lead_term = augmat[i][0]
        for j in range(len(augmat[i])):
            augmat[i][j] = augmat[i][j] - (augmat[0][j] * lead_term)

print(augmat)
