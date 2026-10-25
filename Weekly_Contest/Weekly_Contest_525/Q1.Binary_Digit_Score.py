def calculateScore(a, b):
    a = bin(a)
    b = bin(b)
    
    s1 = a.count('1')
    s2 = b.count('1')

    if s1 > s2:
        return s1 * s2
    else:
        return s2 // s1

print(calculateScore(a = 14, b = 6))