def subarraySum(nums, k):
    count = 0
    total = 0
    hashmap = {0: 1}

    for num in nums:
        total += num

        if total - k in hashmap:
            count += hashmap[total - k]

        if total in hashmap:
            hashmap[total] += 1
        else:
            hashmap[total] = 1

    return count

# def subarraySum(nums, k):   
#     count = 0

#     for i in range(len(nums)):
#         sum = 0

#         for j in range(i, len(nums)):
#             sum += nums[j]
            
#             if sum == k:
#                 count += 1

#     return count



print(subarraySum(nums = [1,1,1], k = 2))