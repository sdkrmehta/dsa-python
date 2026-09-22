def findFinalValue(nums, original):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    while original in count:
        original *= 2

    return original

print(findFinalValue(nums = [5,3,6,1,12], original = 3))
print(findFinalValue(nums = [2,7,9], original = 4))