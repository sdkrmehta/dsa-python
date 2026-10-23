import heapq

def findKthLargest(nums, k):
    heapq.heapify_max(nums)
    ans = 0

    for _ in range(k):
        maxx = heapq.heappop_max(nums)
        ans = maxx

    return ans

print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))