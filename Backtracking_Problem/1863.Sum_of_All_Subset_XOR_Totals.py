class Solution:
    def getAllsubset(self, nums, ans, i, allSubsets):
        if i == len(nums):
            allSubsets.append(ans.copy())
            return

        ans.append(nums[i])
        self.getAllsubset(nums, ans, i + 1, allSubsets)

        ans.pop()

        self.getAllsubset(nums, ans, i + 1, allSubsets)

    def calXOR(self, sub):
        if len(sub) == 0:
            return 0
        
        if len(sub) == 1:
            return sub[0]

        return sub[0] ^ self.calXOR(sub[1:])

    def subsetXORSum(self, nums: list[int]) -> int:
        allSubsets = []
        ans = []
        total = 0

        self.getAllsubset(nums, ans, 0, allSubsets)

        for sub in allSubsets:
            xor = self.calXOR(sub)
            total += xor

        return total

sol = Solution()
result1 = sol.subsetXORSum(nums = [1,3])
result2 = sol.subsetXORSum(nums = [5,1,6])
result3 = sol.subsetXORSum(nums = [3,4,5,6,7,8])
print(result1)
print(result2)
print(result3)