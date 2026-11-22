def minCost(nums):
    n = len(nums)

    if n <= 1:
        return 0

    ans = float('inf')
    i = 0

    while i < n:
        j = i + 1

        while j < n and nums[j] == nums[i]:
            j += 1

        if i < n - 1 and j > 1:
            run = j - i
            cost = (n - run) * nums[i]
            ans = min(ans, cost)

        i = j

    return ans

print(minCost(nums = [1, 2, 3]))
print(minCost(nums = [3, 3, 3, 6, 3, 3]))
print(minCost(nums = [3, 4, 4, 5, 4, 4, 3]))