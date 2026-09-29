def clearDigits(s):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    stack = []

    for i in range(len(s)):
        if s[i] in nums:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)

print(clearDigits(s = "abc"))
print(clearDigits(s = "cb34"))