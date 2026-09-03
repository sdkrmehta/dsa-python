def generate(numRows):

    sol = [[]]

    if numRows == 1:
        sol = [[1]]

    elif numRows == 2:
        sol = [[1], [1, 1]]

    else:
        sol = [[1], [1, 1]]

        for i in range(2, numRows):
            row = [1]

            for j in range(1, len(sol[-1])):
                row.append(sol[-1][j - 1] + sol[-1][j])

            row.append(1)
            sol.append(row)

    return sol


print(generate(5))
