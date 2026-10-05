def findPermutationDifference(s, t):
    countS = {}
    countT = {}
    count = 0

    for index in range(len(s)):
        countS[s[index]] = index
    
    for index in range(len(t)):
        countT[t[index]] = index

    for key in countS:
        count += abs(countS[key] - countT[key])

    return count

print(findPermutationDifference(s = "abc", t = "bac"))
print(findPermutationDifference(s = "abcde", t = "edbac"))
    
    
    
    
# def findPermutationDifference(s, t):  
    # count = 0

    # for i in range(len(s)):
    #     for j in range(len(t)):
    #         if s[i] == t[j]:
    #             summ = abs(i - j)
    #             count += summ

    # return count