def minimumOperations(nums):
    count = 0

    for num in nums:
        if num % 3 != 0:
            count += 1

    return count

print(minimumOperations(nums = [1,2,3,4]))
print(minimumOperations(nums = [3,6,9]))