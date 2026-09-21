def isUgly(n):
    if n <= 0:
        return False

    if n == 1:
        return True

    ans = set()
    i = 2

    while i * i <= n:
        while n % i == 0:
            ans.add(i)
            n = n // i

        i += 1

    if n > 1:
        ans.add(n)

    for i in ans:
        if i != 2 and i != 3 and i != 5:
            return False

    return True


print(isUgly(6))
print(isUgly(14))
print(isUgly(1))