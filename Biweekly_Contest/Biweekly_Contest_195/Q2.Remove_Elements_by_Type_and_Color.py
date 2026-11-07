def canRemoveAll(types, colors, groupSize):
    stack = []

    for t, c in zip(types, colors):
        if stack and stack[-1][0] == t and stack[-1][1] == c:
            stack[-1][2] += 1
        else:
            stack.append([t, c, 1])

        if stack[-1][2] == groupSize[t]:
            stack.pop()

    return len(stack) == 0

print(canRemoveAll(types = [0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]))
print(canRemoveAll(types = [0,1,0], colors = [9,9,9], groupSize = [3,2]))