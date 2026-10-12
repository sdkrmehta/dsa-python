def removeStars(s):
    stack = []

    for st in s:
        if st == "*":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(st)

    return "".join(stack)

print(removeStars(s = "leet**cod*e"))