def subarraySum(nums):
    left = []
    ans = []
    leftSum = 0

    for i in range(len(nums)):
        leftSum += nums[i]
        left.append(leftSum)

    for i in range(len(nums)):
        start = max(0, i - nums[i])
        if start == 0:
            ans.append(left[i])
        else:
            ans.append((left[i] - left[start - 1]))

    return sum(ans)

print(subarraySum(nums = [2,3,1]))