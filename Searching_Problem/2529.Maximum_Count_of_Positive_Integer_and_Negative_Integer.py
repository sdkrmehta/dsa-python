def maximumCount(nums):
    countN = 0
    countP = 0

    for i in range(len(nums)):
        if nums[i] < 0:
            countN += 1
        elif nums[i] > 0:
            countP += 1
    
    return max(countP, countN)

print(maximumCount(nums = [-2,-1,-1,1,2,3]))