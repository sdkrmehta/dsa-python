def minOperations(nums):
    count = 0

    for i in range(len(nums) - 2):
        if nums[i] == 0:
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            count += 1

    if 0 in nums:
        return -1

    return count

print(minOperations(nums = [0,1,1,1,0,0]))
print(minOperations(nums = [0, 1, 1, 1]))