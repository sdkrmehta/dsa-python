import heapq

def findRelativeRanks(score):
    heap = []
    n = len(score)
    ans = [""] * n

    for i in range(n):
        heapq.heappush_max(heap, (score[i], i))

    rank = 0

    while heap:
        marks, idx = heapq.heappop_max(heap)

        if rank == 0:
            ans[idx] = "Gold Medal"
        elif rank == 1:
            ans[idx] = "Silver Medal"
        elif rank == 2:
            ans[idx] = "Bronze Medal"
        else:
            ans[idx] = str(rank + 1)

        rank += 1

    return ans

print(findRelativeRanks(score = [5,4,3,2,1]))
print(findRelativeRanks(score = [10,3,8,9,4]))