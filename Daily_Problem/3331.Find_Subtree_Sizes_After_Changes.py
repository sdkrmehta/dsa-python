def findSubtreeSizes(parent, s):
    children = [[] for _ in s]
    for x in range(1, len(s)):
        children[parent[x]].append(x)
    size, last = [1] * len(s), {}

    def dfs(x: int) -> None:
        c = s[x]
        above = last.get(c, -1)
        last[c] = x
        for child in children[x]:
            dfs(child)
        last[c] = above
        if x:
            size[above if above >= 0 else parent[x]] += size[x]

    dfs(0)
    return size


print(findSubtreeSizes(parent = [-1,0,0,1,1,1], s = "abaabc"))
print(findSubtreeSizes(parent = [-1,0,4,0,1], s = "abbba"))