class Solution:
    def combinations(self, start, n, res, ans, k):
        if len(res) == k:
            ans.append(res.copy())
            return

        for i in range(start, n + 1):
            res.append(i)

            self.combinations(i + 1, n, res, ans, k)

            res.pop()

    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        ans = []

        self.combinations(1, n, res, ans, k)

        return ans

sol = Solution()

result1 = sol.combine(n = 4, k = 2)
result2 = sol.combine(n = 1, k = 1)

print(result1)
print(result2)