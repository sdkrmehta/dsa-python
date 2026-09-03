def generate(numRows):

    sol = [[1]]

    for i in range(1, numRows + 1):

        row = [1]

        for j in range(1, len(sol[-1])):
            row.append(sol[-1][j - 1] + sol[-1][j])

        row.append(1)

        sol.append(row)

    return sol[numRows]


print(generate(10))