def titleToNumber(columnTitle):
    ans = 0

    for ch in columnTitle:
        value = ord(ch) - ord('A') + 1
        ans = ans * 26 + value

    return ans

print(titleToNumber(columnTitle = "A"))
print(titleToNumber(columnTitle = "JZ"))