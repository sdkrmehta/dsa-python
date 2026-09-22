def repeatedCharacter(s):
    ans = set()

    for i in range(len(s)):
        if s[i] in ans:
            return s[i]
        else:
            ans.add(s[i])

print(repeatedCharacter("abccbaacz"))
print(repeatedCharacter("abcdd"))
print(repeatedCharacter("nwcn"))