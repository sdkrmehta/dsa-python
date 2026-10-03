def differenceOfSums(n, m):
    num1 = []
    num2 = []

    for i in range(1, n + 1):
        if i % m != 0:
            num1.append(i)
        else:
            num2.append(i)

    return sum(num1) - sum(num2)

print(differenceOfSums(n = 10, m = 3))
print(differenceOfSums(n = 5, m = 6))
print(differenceOfSums(n = 5, m = 1))