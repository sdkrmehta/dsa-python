def addDigits(num):
    while num >= 10:
        ans = []

        while num > 0:
            ans.append(num % 10)
            num //= 10

        num = sum(ans)

    return num

print(addDigits(38))