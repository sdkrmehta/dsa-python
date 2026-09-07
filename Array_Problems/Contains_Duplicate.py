def containsDuplicate(nums):
    ans = set()

    for i in range(len(nums)):
        if nums[i] in ans:
            return True
        else:
            ans.add(nums[i])

    return False

print(containsDuplicate(nums = [1,2,3,1]))