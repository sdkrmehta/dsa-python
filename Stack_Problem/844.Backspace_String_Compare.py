def backspaceCompare(s, t):
    stackS = []
    stackT = []

    for i in range(len(s)):
        if s[i] == "#":
            if len(stackS) > 0:
                stackS.pop()
        else:
            stackS.append(s[i])

    for i in range(len(t)):
        if t[i] == "#":
            if len(stackT) > 0:
                stackT.pop()
        else:
            stackT.append(t[i])

    joinS = "".join(stackS)
    joinT = "".join(stackT)

    return joinS == joinT

print(backspaceCompare(s = "ab#c", t = "ad#c"))
print(backspaceCompare(s = "ab##", t = "c#d#"))
print(backspaceCompare(s = "a#c", t = "b"))
print(backspaceCompare(s = "a##c", t = "#a#c"))