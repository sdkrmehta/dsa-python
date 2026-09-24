def rearrangeCharacters(s, target):
    countS = {}
    countT = {}

    for st in s:
        if st in countS:
            countS[st] += 1
        else:
            countS[st] = 1

    for st in target:
        if st in countT:
            countT[st] += 1
        else:
            countT[st] = 1

    ans = []

    for key, value in countT.items():
        if key in countS:
            val = countS[key] // countT[key]
            ans.append(val)
        else:
            return 0

    return min(ans)

print(rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))
print(rearrangeCharacters(s = "abcba", target = "abc"))