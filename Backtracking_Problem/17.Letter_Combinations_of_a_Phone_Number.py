class Solution:
    def getCombinations(self, digits, word, ans):
        letters = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        if len(digits) == len(word):
            ans.append(word)
            return

        digit = digits[len(word)]

        for ch in letters[digit]:
            word += ch
            self.getCombinations(digits, word, ans)
            word = word[:-1]

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        word = ""
        ans = []

        self.getCombinations(digits, word, ans)

        return ans

sol = Solution()
print(sol.letterCombinations(digits = "23"))
print(sol.letterCombinations(digits = "2"))