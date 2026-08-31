def diagonalSum(mat):

    n = len(mat)
    sol = 0

    for i in range(n):
        sol += mat[i][i]

        if i != n - 1 - i:
            sol += mat[i][n - 1 - i]

    return sol


print(diagonalSum(mat = [[1,2,3],
                         [4,5,6],
                         [7,8,9]]))

print(diagonalSum(mat = [[1,1,1,1],
                         [1,1,1,1],
                         [1,1,1,1],
                         [1,1,1,1]]))