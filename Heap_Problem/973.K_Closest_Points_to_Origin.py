import heapq
import math

def kClosest(points, k):
    heap = []
    ans = []

    for i in range(len(points)):
        dist = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
        heapq.heappush(heap, [dist, points[i]])

    for _ in range(k):
        if heap:
            dis, cord = heapq.heappop(heap)
            ans.append(cord)

    return ans

print(kClosest(points = [[1,3],[-2,2]], k = 1))
print(kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))