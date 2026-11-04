def minElement(nums):
    minn = float('inf')

    for num in nums:
        summ = 0

        while num > 0:
            digit = num % 10
            summ += digit
            num //= 10

        minn = min(minn, summ)

    return minn


print(minElement([10, 12, 13, 14]))  
print(minElement([999, 19, 199]))    
print(minElement([1, 2, 3, 4]))      