import heapq

def fillCups(amount):
    heap = [-x for x in amount if x > 0]

    heapq.heapify(heap)
    seconds = 0

    while heap:
        first = -heapq.heappop(heap)
        
        if heap:
            second = -heapq.heappop(heap)
            second -= 1
            if second > 0:
                heapq.heappush(heap, -second)
        
        first -= 1
        if first > 0:
            heapq.heappush(heap, -first)
        
        seconds += 1

    return seconds

print(fillCups(amount = [1,4,2]))
print(fillCups(amount = [5,4,4]))
print(fillCups(amount = [5,0,0]))