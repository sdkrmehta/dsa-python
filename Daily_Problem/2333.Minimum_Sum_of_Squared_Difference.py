def minSumSquareDiff(nums1, nums2, k1, k2):
    n = len(nums1)
    operations = k1 + k2
    diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
    max_diff = max(diff)
    count = [0] * (max_diff + 1)

    for d in diff:
        count[d] += 1

    for d in range(max_diff, 0, -1):
        if operations == 0:
            break

        use = min(count[d], operations)
        count[d] -= use
        count[d - 1] += use
        operations -= use

    if operations > 0:
        return 0

    ans = 0

    for d in range(len(count)):
        ans += d * d * count[d]

    return ans

print(minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0))
print(minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))