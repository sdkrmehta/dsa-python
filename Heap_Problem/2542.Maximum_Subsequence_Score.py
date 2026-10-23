import heapq

def maxScore(nums1, nums2, k):
    pairs = sorted(zip(nums2, nums1), reverse=True)

    heap = []
    total = 0
    maxx = 0

    for num2, num1 in pairs:
        heapq.heappush(heap, num1)
        total += num1

        if len(heap) > k:
            total -= heapq.heappop(heap)

        if len(heap) == k:
            maxx = max(maxx, total * num2)

    return maxx


print(maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
print(maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))



# def maxScore(nums1, nums2, k):
#     maxx = float('-inf')
#     minn = float('inf')

#     for i in range(len(nums1) - k + 1):
#         for j in range(len(nums2) - k + 1):
#             if i == j:
#                 minn = min(nums2[j:j + k])
#                 total = sum(nums1[i:i + k]) * minn
#                 maxx = max(maxx, total)

#     return maxx