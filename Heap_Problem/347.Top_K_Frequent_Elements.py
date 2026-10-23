import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []
    ans = []

    for val, freq in count.items():
        heapq.heappush(heap, (-freq, -val))
        
    for _ in range(k):
        freq, val = heapq.heappop(heap)
        ans.append(-val)

    return ans

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))
print(topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))
print(topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))