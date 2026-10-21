import heapq

def getFinalState( nums, k, multiplier):
    heap = [(num, i) for i, num in enumerate(nums)]
    heapq.heapify(heap)

    for _ in range(k):
        num, i = heapq.heappop(heap)
        num *= multiplier
        nums[i] = num
        heapq.heappush(heap, (num, i))

    return nums

print(getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))