def findMiddleIndex(nums):
    leftSum = [0] * len(nums)
    rightSum = [0] * len(nums)
    totalL = 0
    totalR = 0

    for i in range(len(nums)):
        totalL += nums[i]
        leftSum[i] = totalL

    for i in range(len(nums) -1, -1, -1):
        totalR += nums[i]
        rightSum[i] = totalR

    for i in range(len(leftSum)):
        if leftSum[i] == rightSum[i]:
            return i

    return -1

print(findMiddleIndex(nums = [2,3,-1,8,4]))
print(findMiddleIndex(nums = [1,-1,4]))
print(findMiddleIndex(nums = [2,5]))