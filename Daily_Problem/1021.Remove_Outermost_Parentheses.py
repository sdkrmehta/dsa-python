def removeOuterParentheses(s):
    stack = []
    ans = []
    count1 = 0
    count2 = 0

    for i in range(len(s)):
        if s[i] == "(":
            count1 += 1
            stack.append(s[i])
        else:
            count2 += 1
            stack.append(s[i])

        if count1 == count2:
            stack.pop(0)
            stack.pop()
            ans.extend(stack)
            stack = []
            count1 = 0
            count2 = 0

    return "".join(ans)

print(removeOuterParentheses(s = "(()())(())(()(()))"))