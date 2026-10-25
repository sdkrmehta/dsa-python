class Solution:
    def getAllSubsets(self, nums, ans, i, allSubsets):
        if i == len(nums):
            allSubsets.append(ans.copy())
            return

        ans.append(nums[i])
        self.getAllSubsets(nums, ans, i + 1, allSubsets)

        ans.pop()

        self.getAllSubsets(nums, ans, i + 1, allSubsets)

    def subsets(self, nums):
        allSubsets = []
        ans = []

        self.getAllSubsets(nums, ans, 0, allSubsets)

        return allSubsets

sol = Solution()
result = sol.subsets(nums = [1, 2, 3])
print(result)