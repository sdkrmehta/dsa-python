def makeGood(s):
    stack = []

    for i in range(len(s)):
        if len(stack) > 0:
            if abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])        

    return "".join(stack)

print(makeGood(s = "leEeetcode"))
print(makeGood(s = "abBAcC"))
print(makeGood(s = "s"))