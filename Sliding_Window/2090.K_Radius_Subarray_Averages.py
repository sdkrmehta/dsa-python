def getAverages(nums, k):
    n = len(nums)
    ans = [-1] * n
    window_size = 2 * k + 1

    if window_size > n:
        return ans

    curr_sum = 0

    for i in range(window_size):
        curr_sum += nums[i]

    ans[k] = curr_sum // window_size

    for i in range(k + 1, n - k):
        curr_sum += nums[i + k]
        curr_sum -= nums[i - k - 1]
        ans[i] = curr_sum // window_size

    return ans

print(getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3))
print(getAverages(nums = [100000], k = 0))
print(getAverages(nums = [8], k = 100000))