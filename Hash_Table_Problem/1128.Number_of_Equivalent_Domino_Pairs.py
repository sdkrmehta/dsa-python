def numEquivDominoPairs(dominoes):
    ans = []
    for domi in dominoes:
        d = sorted(domi)
        ans.append(d)

    count = {}

    for domi in ans:
        domi = tuple(domi)
        if domi in count:
            count[domi] += 1
        else:
            count[domi] = 1

    total = 0

    for val in count.values():
        if val > 1:
            pairs = (val * (val - 1)) // 2
            total += pairs

    return total

print(numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))