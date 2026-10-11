def sumOfSquares(nums):
    total = 0
    for i in range(len(nums)):
        if len(nums) % (i + 1) == 0:
            total += (nums[i] ** 2)

    return total

print(sumOfSquares(nums = [1,2,3,4]))
print(sumOfSquares(nums = [2,7,1,19,18,3]))