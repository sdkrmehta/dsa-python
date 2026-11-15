def countConsistent(nums):
    ans = 0
    intervals = []
    pos = {}

    for r, x in enumerate(nums):
        pos[x] = r
        new = []

        for val, L, R in intervals:
            new_val = val & x

            if new and new[-1][0] == new_val:
                new[-1][2] = R
            else:
                new.append([new_val, L, R])

        if new and new[-1][0] == x:
            new[-1][2] = r
        else:
            new.append([x, r, r])

        intervals = new

        for val, L, R in intervals:
            if val in pos:
                p = pos[val]
                if p >= L:
                    ans += min(R, p) - L + 1

    return ans

print(countConsistent(nums = [5,3,1,2]))