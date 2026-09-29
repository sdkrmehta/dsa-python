def minOperations(logs):
    stack = []

    for i in range(len(logs)):
        if logs[i] == "../":
            if len(stack) > 0:
                stack.pop()
        elif logs[i] == "./":
            continue
        else:
            stack.append(logs[i])

    return len(stack)

print(minOperations(logs = ["d1/","d2/","../","d21/","./"]))
print(minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
print(minOperations(logs = ["d1/","../","../","../"]))