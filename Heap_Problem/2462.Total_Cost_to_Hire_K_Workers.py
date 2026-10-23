import heapq

def totalCost(costs, k, candidates):
    n = len(costs)
    pq1 = []
    pq2 = []
    
    ans = 0
    hired = 0
    i = 0
    j = n - 1
    
    while hired < k:
        while len(pq1) < candidates and i <= j:
            heapq.heappush(pq1, costs[i])
            i += 1
            
        while len(pq2) < candidates and j >= i:
            heapq.heappush(pq2, costs[j])
            j -= 1
            
        min_pq1 = pq1[0] if pq1 else float('inf')
        min_pq2 = pq2[0] if pq2 else float('inf')
        
        if min_pq1 <= min_pq2:
            ans += min_pq1
            heapq.heappop(pq1)
        else:
            ans += min_pq2
            heapq.heappop(pq2)
            
        hired += 1
        
    return ans

print(totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
print(totalCost(costs = [1,2,4,1], k = 3, candidates = 3))