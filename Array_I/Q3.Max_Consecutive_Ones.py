def findMaxConsecutiveOnes(nums):
    ans = 0
    curr = 0

    for i in range(0, len(nums)):
        if nums[i] == 1:
            curr += 1
            ans = max(ans, curr)
        else:
            curr = 0
    return ans

print(findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))