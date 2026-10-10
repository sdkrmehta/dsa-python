def kthCharacter(k):
    s = "a"

    while len(s) < k:
        for i in range(len(s)):
            if s[i] == "z":
                s[i] == "a"
            else:
                s += chr(ord(s[i]) + 1)

    return s[k - 1]

print(kthCharacter(k = 10))