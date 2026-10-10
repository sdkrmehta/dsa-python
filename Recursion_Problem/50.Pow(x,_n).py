def findPow(x, n):
    if n == 0:
        return 1

    a = findPow(x, n // 2)

    if n % 2 == 0:
        return a * a
    else:
        return a * a * x

def myPow(x, n):
    if n >= 0:
        return findPow(x, n)
    else:
        return 1 / findPow(x, -n)

print(myPow(x = 2.00000, n = 10))