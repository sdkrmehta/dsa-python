class Solution:
    def getAllSubsets(self, nums, ans, i, allSubsets):
        allSubsets.append(ans.copy())

        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue

            ans.append(nums[j])
            self.getAllSubsets(nums, ans, j + 1, allSubsets)
            ans.pop()

    def subsetsWithDup(self, nums):
        nums.sort()

        allSubsets = []
        ans = []

        self.getAllSubsets(nums, ans, 0, allSubsets)

        return allSubsets

sol = Solution()
result = sol.subsetsWithDup(nums = [1, 2, 2])
print(result)