def createGrid(m, n):
    res = [['#'] * n for _ in range(m)]

    for i in range(n):
        res[0][i] = '.'

    for i in range(1, m):
        res[i][n - 1] = '.'

    return [''.join(row) for row in res]

print(createGrid(m = 2, n = 3))
print(createGrid(m = 3, n = 3))