import heapq
from collections import Counter

def busiestServers(k, arrival, load):
    free = list(range(k))
    heapq.heapify(free)

    handled, busy = [], []

    for i, (t, d) in enumerate(zip(arrival, load)):
        while busy and busy[0][0] <= t:
            _, server = heapq.heappop(busy)
            heapq.heappush(free, i + (server - i) % k)

        if free:
            x = heapq.heappop(free) % k
            heapq.heappush(busy, (t + d, x))
            handled.append(x)

    count = Counter(handled)
    maximum = max(count.values(), default=0)

    return [server for server in range(k) if count[server] == maximum]

print(busiestServers(k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]))