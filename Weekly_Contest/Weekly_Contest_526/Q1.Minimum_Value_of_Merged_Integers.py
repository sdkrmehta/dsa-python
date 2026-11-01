def minMergedInteger(nums):
        ans = float('inf')

        for i in range(0, len(nums), 2):
            merged = int(str(nums[i]) + str(nums[i + 1]))
            ans = min(ans, merged)

        return ans

print(minMergedInteger(nums = [23,55,42,21]))