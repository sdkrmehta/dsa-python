def countLargestGroup(n):
    ans = []

    for i in range(1, n + 1):
        digit = []
        num = i

        while num > 0:
            digit.append(num % 10)
            num //= 10

        ans.append([i, sum(digit)])

    count = {}
    for num, digit_sum in ans:
        if digit_sum not in count:
            count[digit_sum] = 1
        else:
            count[digit_sum] += 1

    largest = max(count.values())
    return list(count.values()).count(largest)


print(countLargestGroup(13))  # 4
print(countLargestGroup(2))   # 2