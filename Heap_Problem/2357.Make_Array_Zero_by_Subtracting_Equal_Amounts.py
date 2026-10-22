import heapq

def minimumOperations(nums):
    heap = [num for num in nums if num > 0]
    heapq.heapify(heap)

    count = 0

    while heap:
        smallest = heap[0]
        new_heap = []

        while heap:
            num = heapq.heappop(heap)
            if num - smallest > 0:
                new_heap.append(num - smallest)

        heap = new_heap
        heapq.heapify(heap)
        count += 1

    return count

print(minimumOperations(nums = [1,5,0,3,5]))
print(minimumOperations(nums = [0]))
print(minimumOperations(nums = [8]))