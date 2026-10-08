def findThePrefixCommonArray(A, B):
    countA = {}
    countB = {}
    count = 0
    ans = []

    for i in range(len(A)):
        countA[A[i]] = 1
        countB[B[i]] = 1

        if A[i] in countB:
            count += 1

        if B[i] in countA and A[i] != B[i]:
            count += 1

        ans.append(count)

    return ans

print(findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))