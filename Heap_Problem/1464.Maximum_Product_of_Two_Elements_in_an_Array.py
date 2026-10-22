import heapq

def maxProduct(nums):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > 2:
            heapq.heappop(min_heap)

    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)

    return (a - 1) * (b - 1)

print(maxProduct(nums = [3,4,5,2]))
print(maxProduct(nums = [1,5,4,5]))
print(maxProduct(nums = [3,7]))
print(maxProduct(nums = [10,2,5,2]))