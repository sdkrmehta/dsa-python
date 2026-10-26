class Solution:
    def getCombinations(self, candidates, target, start, ans, res):
        if target == 0:
            res.append(ans.copy())
            return

        if target < 0:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]

            ans.append(num)

            self.getCombinations(
                candidates, target - num, i, ans, res
            )

            ans.pop()

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        ans = []

        self.getCombinations(candidates, target, 0, ans, res)

        return res

sol = Solution()

print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([2, 3, 5], 8))