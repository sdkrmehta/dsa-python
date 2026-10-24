import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    heap = []
    pair = []

    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    while heap and len(pair) < k:
        total, i, j = heapq.heappop(heap)

        pair.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[j + 1], i, j + 1)
            )

    return pair

print(kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
print(kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))








    # ans = []
    # pair = []

    # for num1 in nums1:
    #     for num2 in nums2:
    #         ans.append([[num1, num2], [num1 + num2]])

    # res = sorted(ans, key = lambda x:x[1])

    # for _ in range(k):
    #     pair.append(res[0][0])

    # return pair