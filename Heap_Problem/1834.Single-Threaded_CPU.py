import heapq

def getOrder(tasks):
    tasks_with_index = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
    tasks_with_index.sort(key=lambda x: x[0])
    
    res = []
    min_heap = []
    i = 0
    n = len(tasks)
    current_time = 0
    
    while len(res) < n:
        while i < n and tasks_with_index[i][0] <= current_time:
            heapq.heappush(min_heap, (tasks_with_index[i][1], tasks_with_index[i][2]))
            i += 1
            
        if not min_heap:
            current_time = tasks_with_index[i][0]
        else:
            proc_time, index = heapq.heappop(min_heap)
            res.append(index)
            current_time += proc_time
            
    return res

print(getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))