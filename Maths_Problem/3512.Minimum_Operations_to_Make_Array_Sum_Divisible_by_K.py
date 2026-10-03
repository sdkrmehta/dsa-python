def minOperations(nums, k):
    return sum(nums) % k

print(minOperations(nums = [3,9,7], k = 5))