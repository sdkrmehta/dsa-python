import math
def gcdOfOddEvenSums(n):
    n = 2*n
    even = []
    odd = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    a = sum(even)
    b = sum(odd)

    return math.gcd(a,b)

print(gcdOfOddEvenSums(10))
