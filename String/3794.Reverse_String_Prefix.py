def reversePrefix(self, s: str, k: int) -> str:
    sol1 = list(s[:k])
    sol2 = s[k:]

    for i in range(len(sol1)):
        f = sol1.pop()
        sol1.insert(i, f)

    ans = "".join(sol1) + sol2
    return ans

print(reversePrefix("abcdefd", 4))