def findAndReplacePattern(words, pattern):
    ans = []

    for word in words:
        map1 = {}
        map2 = {}
        match = True

        for p, w in zip(pattern, word):

            if p in map1 and map1[p] != w:
                match = False
                break

            if w in map2 and map2[w] != p:
                match = False
                break

            map1[p] = w
            map2[w] = p

        if match:
            ans.append(word)

    return ans

print(findAndReplacePattern(words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern = "abb"))
print(findAndReplacePattern(words = ["a", "b", "c"], pattern = "a"))