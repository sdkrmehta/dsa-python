def calPoints(operations):
    stack = []

    for i in range(len(operations)):
        if operations[i] == "C":
            stack.pop()
        elif operations[i] == "D":
            top = int(stack[-1])
            ans = str(top * 2)
            stack.append(ans)
        elif operations[i] == "+":
            top = int(stack[-1])
            second = int(stack[-2])
            sums = top + second
            stack.append(str(sums))
        else:
            stack.append(operations[i])

    int_list = []

    for x in stack:
        int_list.append(int(x))

    total = sum(int_list)

    return total

print(calPoints(["5","2","C","D","+"]))