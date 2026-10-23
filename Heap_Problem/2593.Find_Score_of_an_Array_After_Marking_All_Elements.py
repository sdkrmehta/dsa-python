import heapq

def findScore(nums):
    heap = []
    marked = [False] * len(nums)
    ans = 0

    for i in range(len(nums)):
        heapq.heappush(heap, (nums[i], i))

    while heap:
        num, idx = heapq.heappop(heap)

        if marked[idx]:
            continue

        ans += num
        marked[idx] = True

        if idx > 0:
            marked[idx - 1] = True

        if idx < len(nums) - 1:
            marked[idx + 1] = True

    return ans

print(findScore(nums = [2,1,3,4,5,2]))
print(findScore(nums = [2,3,5,1,3,2]))