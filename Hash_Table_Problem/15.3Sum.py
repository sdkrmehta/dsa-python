def threeSum(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        hashset = set()

        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                result.add(tuple(temp))
            hashset.add(nums[j])

    ans = list(result)
    return ans

print(threeSum(nums = [-1,0,1,2,-1,-4]))
print(threeSum(nums = [0,0,0,0]))


# def threeSum(nums):
#     n = len(nums)
#     ans = []

#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):

#                 if nums[i] + nums[j] + nums[k] == 0:
#                     triplet = [nums[i], nums[j], nums[k]]

#                     if triplet not in ans:
#                         ans.append(triplet)

#     return ans