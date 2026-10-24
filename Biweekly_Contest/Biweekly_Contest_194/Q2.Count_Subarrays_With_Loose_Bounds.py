def countSubarrays(nums, minK, maxK):
    count = 0
    ans = 0

    for num in nums:
        if minK <= num <= maxK:
            count += 1
            ans += count
        else:
            count = 0

    return ans

print(countSubarrays(nums = [1,4,7,3], minK = 1, maxK = 5))
print(countSubarrays(nums = [1,1], minK = 1, maxK = 1))


# # TLE

# def countSubarrays(nums, minK, maxK):
#     sub = []
#     ans = []
#     count = 0

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums) + 1):
#             sub.append(nums[i:j])

#     for i in range(len(sub)):
#         valid = True
#         for j in range(len(sub[i])):
#             if sub[i][j] > maxK or sub[i][j] < minK:
#                 valid = False
#                 break

#         if valid:
#             ans.append(sub[i])
#             count += 1

#     return count