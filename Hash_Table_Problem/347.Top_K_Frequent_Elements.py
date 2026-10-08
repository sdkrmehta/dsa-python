def topKFrequent(nums, k):
    nums.sort()
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return list(count.keys())[:k]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))
print(topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))