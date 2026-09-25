def maxFreqSum(s):
    vowels = ["a", "e", "i", "o", "u"]
    countV = {}
    countC = {}

    for st in s:
        if st in vowels:
            if st in countV:
                countV[st] += 1
            else:
                countV[st] = 1
        else:
            if st in countC:
                countC[st] += 1
            else:
                countC[st] = 1

    max_vowel = max(countV.values(), default=0)
    max_con = max(countC.values(), default=0)

    return max_vowel + max_con

print(maxFreqSum(s = "successes"))
print(maxFreqSum(s = "aeiaeia"))