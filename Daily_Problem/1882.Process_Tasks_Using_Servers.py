import heapq

def assignTasks(servers, tasks):

    free = [(w, i) for i, w in enumerate(servers)]
    heapq.heapify(free)

    ans, busy = [], []

    for s, t in enumerate(tasks):

        while busy and busy[0][0] <= s:
            heapq.heappush(free, heapq.heappop(busy)[1:])

        if free:
            start, w, i = s, *heapq.heappop(free)
        else:
            start, w, i = heapq.heappop(busy)

        heapq.heappush(busy, (start + t, w, i))
        ans.append(i)

    return ans

print(assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))
print(assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]))