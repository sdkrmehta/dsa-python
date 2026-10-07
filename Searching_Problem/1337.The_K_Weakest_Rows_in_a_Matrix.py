def kWeakestRows(mat, k):
    ans = []

    for i in range(len(mat)):
        left = 0
        right = len(mat[i])

        while left < right:
            mid = (left + right) // 2
            if mat[i][mid] == 1:
                left = mid + 1
            else:
                right = mid

        ans.append((left, i))

    ans.sort()
    return [row[1] for row in ans[:k]]

print(kWeakestRows(mat = [[1,1,0,0,0],
                          [1,1,1,1,0],
                          [1,0,0,0,0],
                          [1,1,0,0,0],
                          [1,1,1,1,1]], k = 3))