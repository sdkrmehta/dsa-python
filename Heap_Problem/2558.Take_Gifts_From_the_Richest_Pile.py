import heapq
import math

def pickGifts(gifts, k):
    heapq.heapify_max(gifts)

    for i in range(k):
            maxx = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.isqrt(maxx))

    return sum(gifts)

print(pickGifts(gifts = [25,64,9,4,100], k = 4))
print(pickGifts(gifts = [1,1,1,1], k = 4))