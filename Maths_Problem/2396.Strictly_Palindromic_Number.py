def isStrictlyPalindromic(n):
    ans = []

    for i in range(2, n - 1):
        string = ""
        num = n

        while num > 0:
            remainder = num % i
            string = str(remainder) + string
            num = num // i

        ans.append(string)

    for a in ans:
        if a != a[::-1]:
            return False

    return True

print(isStrictlyPalindromic(9))
print(isStrictlyPalindromic(4))