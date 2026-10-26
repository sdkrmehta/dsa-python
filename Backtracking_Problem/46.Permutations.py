class Solution:
    def getPermutations(self, nums, ans, allPermutations):
        if len(ans) == len(nums):
            allPermutations.append(ans.copy())
            return 

        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
                self.getPermutations(nums, ans, allPermutations)
                ans.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        allPermutations = []
        ans = []

        self.getPermutations(nums, ans, allPermutations)

        return allPermutations

sol = Solution()

result1 = sol.permute(nums = [1,2,3])
result2 = sol.permute(nums = [0,1])
result3 = sol.permute(nums = [1])

print(result1)
print(result2)
print(result3)