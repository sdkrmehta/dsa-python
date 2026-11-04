def smallestEvenMultiple(n):
    if n % 2 != 0:
        return n * 2
    else:
        return n

print(smallestEvenMultiple(n = 5))
print(smallestEvenMultiple(n = 6))