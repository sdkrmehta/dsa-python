def countDominantElements(nums):
    if len(nums) == 1:
        return 1
        
    count = 0

    for i in range(len(nums)):
        if i == 0 and nums[i] >= nums[i + 1]:
            count += 1
        elif i == len(nums) - 1 and nums[i] >= nums[i - 1]:
            count += 1
        elif 0 < i < len(nums) - 1:
            if nums[i] >= ((nums[i - 1] + nums[i + 1]) / 2):
                count += 1

    return count

print(countDominantElements(nums = [1, 10, 2]))
print(countDominantElements(nums = [6, 4, 2]))