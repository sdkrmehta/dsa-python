def minRange(a, b, c):
    x, y, z = sorted([a, b, c])
    return min(z - x, y)

print(minRange(a = 9, b = 2, c = 5))