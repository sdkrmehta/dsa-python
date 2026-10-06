def minAddToMakeValid(s):
    count1 = 0
    count2 = 0

    if len(s) == 0:
        return 0

    for i in range(len(s)):
        if s[i] == "(":
            count1 += 1
        else:
            if count1 > 0:
                count1 -= 1
            else:
                count2 += 1

    return count1 + count2

print(minAddToMakeValid(s = "())"))
print(minAddToMakeValid(s = "((("))
print(minAddToMakeValid(s = "()))(("))
print(minAddToMakeValid(s = "(()()))(("))