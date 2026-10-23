import heapq
import math

def minStoneSum(piles, k):
    heapq.heapify_max(piles)

    while k > 0:
        largest = heapq.heappop_max(piles)
        remaining = largest - math.floor(largest / 2)
        heapq.heappush_max(piles, remaining)
        k -= 1

    return sum(piles)

print(minStoneSum(piles = [5,4,9], k = 2))
print(minStoneSum(piles = [4,3,6,7], k = 3))