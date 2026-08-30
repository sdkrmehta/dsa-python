def pivotIndex(nums):
    ans = -1

    for i in range(len(nums)):
        left = nums[:i]
        right = nums[i+1:]

        if sum(left) == sum(right):
            ans = i
            break

    return ans

print(pivotIndex(nums = [1,7,3,6,5,6]))
print(pivotIndex(nums = [1,2,3]))
print(pivotIndex(nums = [2,1,-1]))