def countPartitions(nums):

    left = []
    right = [0] * len(nums)

    totalL = 0
    totalR = 0
    countE = 0
    countO = 0

    for i in range(len(nums)):
        totalL += nums[i]
        left.append(totalL)

    for i in range(len(nums) - 1, -1, -1):
        totalR += nums[i]
        right[i] = totalR

    for i in range(len(nums) - 1):
        if (left[i] - right[i + 1]) % 2 == 0:
            countE += 1
        else:
            countO += 1

    return countE


print(countPartitions([10, 10, 3, 7, 6]))
print(countPartitions([1, 2, 2]))