def minSubArrayLen(target, nums):
    left = 0
    total = 0
    ans = len(nums) + 1

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            length = right - left + 1

            if length < ans:
                ans = length

            total -= nums[left]
            left += 1

    if ans == len(nums) + 1:
        return 0

    return ans


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))