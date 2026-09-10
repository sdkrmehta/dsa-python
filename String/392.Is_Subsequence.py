def isSubsequence(s: str, t: str):
    s = list(str(s))
    t = list(str(t))

    j = 0

    for i in range(len(t)):
        if j < len(s) and s[j] == t[i]:
            j += 1

    if j == len(s):
        return True

    return False

print(isSubsequence(s = "abc", t = "ahbgdc"))