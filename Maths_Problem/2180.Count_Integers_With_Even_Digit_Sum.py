def countEven(num):
    count = 0

    for i in range(1, num + 1):
        digit = []
        n = i

        while n > 0:
            digit.append(n % 10)
            n //= 10

        if sum(digit) % 2 == 0:
            count += 1

    return count

print(countEven(num = 4))
print(countEven(num = 30))