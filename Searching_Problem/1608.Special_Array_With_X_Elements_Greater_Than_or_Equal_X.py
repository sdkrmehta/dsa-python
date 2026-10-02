def specialArray(nums):
    for x in range(len(nums) + 1):
        count = 0

        for num in nums:
            if num >= x:
                count += 1

        if count == x:
            return x

    return -1

print(specialArray(nums = [3,5]))
print(specialArray(nums = [0,0]))
print(specialArray(nums = [0,4,3,0,4]))
print(specialArray(nums = [3,6,7,7,0]))