def maxScore(s):
    digit = []

    for num in s:
        digit.append(int(num))

    prefix = [0] * len(digit)
    suffix = [0] * len(digit)
    totalP = 0

    for i in range(len(digit)):
        if digit[i] == 0:
            totalP += 1

        prefix[i] = totalP

    totals = 0

    for i in range(len(digit) -1, -1, -1):
        if digit[i] == 1:
            totals += 1

        suffix[i] = totals

    ans = []

    for i in range(len(digit) - 1):
        score = prefix[i] + suffix[i + 1]
        ans.append(score)

    return max(ans)

print(maxScore("011101"))
print(maxScore("1111"))