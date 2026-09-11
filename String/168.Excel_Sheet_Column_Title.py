def convertToTitle(columnNumber):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""

    while columnNumber > 0:
        columnNumber -= 1

        remainder = columnNumber % 26
        ans = letters[remainder] + ans

        columnNumber = columnNumber // 26

    return ans

print(convertToTitle(columnNumber = 28))