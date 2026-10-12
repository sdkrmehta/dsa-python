def findEvenNumbers(digits):
    sett = set()

    for i in range(len(digits)):
        if digits[i] != 0:
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if digits[k] % 2 == 0:
                        if ((digits[i] * 100) + (digits[j] * 10) + (digits[k] * 1)) % 2 == 0 and i != j and j != k and k != i:
                            sett.add(((digits[i] * 100) + (digits[j] * 10) + (digits[k] * 1)))
    
    return sorted(list(sett))
    
print(findEvenNumbers(digits = [2,1,3,0]))