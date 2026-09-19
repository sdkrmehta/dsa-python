def findLHS(nums):
    count = {}
    ans = 0

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for i in range(len(nums)):
        minNum = nums[i]
        maxNum = minNum + 1

        if maxNum in count:
            ans = max(ans, count[minNum] + count[maxNum])

    return ans


print(findLHS(nums = [1, 3, 2, 2, 5, 2, 3, 7]))
print(findLHS(nums = [3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3]))