def reversePrefix(word, ch):
    if ch not in word:
        return word

    stack = []
    ans = []
    count = 0

    for i in range(len(word)):
        if word[i] == ch:
            stack.append(word[i])
            count += 1
            break
        else:
            stack.append(word[i])
            count += 1

    for i in range(count, len(word)):
        ans.append(word[i])

    stack.reverse()
    stack = "".join(stack) + "".join(ans)

    return stack

print(reversePrefix(word = "xyxzxe", ch = "z"))
print(reversePrefix(word = "abcdefd", ch = "d"))
print(reversePrefix(word = "abcd", ch = "z"))