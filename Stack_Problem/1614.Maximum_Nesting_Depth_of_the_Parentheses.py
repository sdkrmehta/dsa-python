def maxDepth(s):
    count = 0
    max_num = 0

    for i in range(len(s)):
        if s[i] == "(":
            count += 1
            max_num = max(max_num, count)

        elif s[i] == ")":
            count -= 1

    return max_num


print(maxDepth("(1+(2*3)+((8)/4))+1"))