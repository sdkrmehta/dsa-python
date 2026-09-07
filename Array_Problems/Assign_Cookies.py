def findContentChildren( g, s):
    g.sort()
    s.sort()

    count = 0
    j = 0

    for i in range(len(g)):
        while j < len(s):
            if s[j] >= g[i]:
                count += 1
                j += 1
                break
            else:
                j += 1

    return count

print(findContentChildren(g = [1,2,3], s = [1,1]))