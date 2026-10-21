import heapq

def lastStoneWeight(stones):
    heapq.heapify_max(stones)

    while len(stones) > 1:
        sm1 = heapq.heappop_max(stones)
        sm2 = heapq.heappop_max(stones)
        sm = abs(sm1 - sm2)

        if sm != 0:
            heapq.heappush_max(stones, sm)

    return stones[0] if stones else 0

print(lastStoneWeight(stones = [2,7,4,1,8,1]))