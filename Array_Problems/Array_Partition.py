def arrayPairSum(nums):
    nums.sort()
    ans = 0

    for i in range(0, len(nums), 2):
        ans += nums[i]

    return ans

print(arrayPairSum(nums = [1,4,3,2]))
print(arrayPairSum(nums = [6,2,6,5,1,2]))