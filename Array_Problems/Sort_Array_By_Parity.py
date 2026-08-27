def sortArrayByParity(nums):
    start = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
    return nums

print(sortArrayByParity(nums = [3,1,2,4]))