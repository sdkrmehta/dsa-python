class Solution:
    def combination(self, s, i, char, res, ans):
        if i == len(s):
            ans.append("".join(res))
            return

        ch = s[i]

        if ch.isalpha():
            # Choice 1: lowercase
            res.append(ch.lower())
            self.combination(s, i + 1, char, res, ans)
            res.pop()

            # Choice 2: uppercase
            res.append(ch.upper())
            self.combination(s, i + 1, char, res, ans)
            res.pop()

        else:
            # Digits remain unchanged
            res.append(ch)
            self.combination(s, i + 1, char, res, ans)
            res.pop()

    def letterCasePermutation(self, s):
        char = []
        res = []
        ans = []

        self.combination(s, 0, char, res, ans)

        return ans

sol = Solution()

result1 = sol.letterCasePermutation(s = "a1b2")
result2 = sol.letterCasePermutation(s = "3z4")

print(result1)
print(result2)