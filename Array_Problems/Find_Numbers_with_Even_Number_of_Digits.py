def findNumbers(nums):
    count = 0

    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1
    return count

print(findNumbers(nums=[12,345,2,6,7896]))
