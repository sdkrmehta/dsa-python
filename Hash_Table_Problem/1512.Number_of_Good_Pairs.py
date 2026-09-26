def numIdenticalPairs(nums):
    count = {}
    ans = 0

    for num in nums:
        if num in count:
            ans += count[num]
            count[num] += 1
        else:
            count[num] = 1

    return ans


print(numIdenticalPairs(nums = [1,2,3,1,1,3]))
print(numIdenticalPairs(nums = [1,1,1,1]))



# def numIdenticalPairs(nums):
#     count = 0

#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if (i != j) and (nums[i] == nums[j]):
#                 count += 1

#     return count // 2