def reverseParentheses(s):
    stack = []

    for ch in s:
        if ch != ")":
            stack.append(ch)

        else:
            temp = []

            while stack[-1] != "(":
                temp.append(stack.pop())

            stack.pop()

            for ch in temp:
                stack.append(ch)

    return "".join(stack)


print(reverseParentheses("(abcd)"))
print(reverseParentheses("(u(love)i)"))
print(reverseParentheses("(ed(et(oc))el)"))