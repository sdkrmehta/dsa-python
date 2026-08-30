def dominantIndex(nums):
    ans = max(nums)
    index = nums.index(ans)

    for i in range(len(nums)):
        if i != index:
            if ans < 2 * nums[i]:
                return -1

    return index

print(dominantIndex(nums = [3,6,1,0]))
print(dominantIndex(nums = [1,2,3,4]))