import heapq

def maxSubsequence(nums, k):
    if len(nums) == k:
        return nums
    
    min_heap = []
        
    for idx, val in enumerate(nums):
        heapq.heappush(min_heap, (val, idx))
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    min_heap.sort(key=lambda x: x[1])
    return [val for val, idx in min_heap]

print(maxSubsequence(nums = [2,1,3,3], k = 2))
print(maxSubsequence(nums = [-1,-2,3,4], k = 3))
print(maxSubsequence(nums = [3,4,3,3], k = 2))
print(maxSubsequence(nums = [50,-75], k = 2))