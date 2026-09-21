def hasAlternatingBits(n):
    num = str(bin(n))
    for i in range(2, len(num) -1):
        if num[i] != num[i + 1]:
            continue
        else:
            return False
        
    return True

print(hasAlternatingBits(n = 11))
print(hasAlternatingBits(n = 5))