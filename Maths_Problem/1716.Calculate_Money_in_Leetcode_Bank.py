def totalMoney(n):
    monday = 0
    count = 0
    total = 0

    for i in range(1, n + 1):
        if count == 7:
            monday = i // 7 + 1
            count = 0
        else:
            monday += 1

        total += monday
        count += 1

    return total

print(totalMoney(n = 4))
print(totalMoney(n = 10))
print(totalMoney(n = 20))