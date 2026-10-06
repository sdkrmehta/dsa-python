def minStartValue(nums):
    total = 0
    minn = 0

    for i in range(len(nums)):
        total += nums[i]
        minn = min(minn, total)

    return 1 - minn

print(minStartValue(nums = [-3,2,-3,4,2]))