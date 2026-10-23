def sortPermutation(nums):
    k = -1

    for i, num in enumerate(nums):
        if num != i:
            k &= num

    return max(k, 0)

print(sortPermutation(nums = [0,3,2,1]))
print(sortPermutation(nums = [0,1,3,2]))
print(sortPermutation(nums = [3,2,1,0]))