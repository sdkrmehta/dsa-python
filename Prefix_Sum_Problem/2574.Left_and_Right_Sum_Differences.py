def leftRightDifference(nums):
    leftSum = []
    rightSum = [0] * len(nums)
    totalLeft = 0
    totalRight = 0
    ans = []

    for num in nums:
        leftSum.append(totalLeft)
        totalLeft += num

    for i in range(len(nums) - 1, -1, -1):
        rightSum[i] = totalRight
        totalRight += nums[i]

    for i in range(len(nums)):
        total = abs(leftSum[i] - rightSum[i])
        ans.append(total)

    return ans

print(leftRightDifference([10, 4, 8, 3]))