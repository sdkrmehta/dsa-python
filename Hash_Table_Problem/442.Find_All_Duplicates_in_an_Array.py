def findDuplicates(nums):
    ans = []

    for num in nums:
        idx = abs(num) - 1

        if nums[idx] < 0:
            ans.append(abs(num))
        else:
            nums[idx] = -nums[idx]

    return ans

print(findDuplicates(nums = [4, 3, 2, 7, 8, 2, 3, 1]))
print(findDuplicates(nums = [1, 1, 2]))
print(findDuplicates(nums = [1]))
print(findDuplicates(nums = []))