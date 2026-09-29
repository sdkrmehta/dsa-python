def removeDuplicates(s):
    stack = []

    for i in range(len(s)):
        if len(stack) > 0:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return "".join(stack)

print(removeDuplicates(s = "abbaca"))
print(removeDuplicates(s = "azxxzy"))