def checkValidString(s):
    stack1 = []
    stack2 = []

    for i in range(len(s)):
        if s[i] == "(":
            stack1.append(i)
        elif s[i] == ")":
            if len(stack1) > 0:
                stack1.pop()
            elif len(stack2) > 0:
                stack2.pop()
            else:
                return False
        else:
            stack2.append(i)

    while len(stack1) > 0:
        if len(stack2) == 0:
            return False
        if stack1[-1] > stack2[-1]:
            return False

        stack1.pop()
        stack2.pop()

    return True

print(checkValidString(s = "()"))
print(checkValidString(s = "(*)"))
print(checkValidString(s = "(*)*))"))
print(checkValidString(s = "("))
print(checkValidString(s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"))