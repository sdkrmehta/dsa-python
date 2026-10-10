def maxProductPair(nums, target):
        maxx = float("-inf")
        ans = [-1, -1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and nums[i] > nums[j]:
                    prod = nums[i] * nums[j]

                    if prod > maxx:
                        maxx = prod
                        ans = [i, j]

        return ans

print(maxProductPair(nums = [1,2,3,4], target = 5))