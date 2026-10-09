def minInsertions(s):
    count = 0
    ans = 0
    i = 0

    while i < len(s):
        if s[i] == "(":
            count += 1
            i += 1
        else:
            if i + 1 < len(s) and s[i + 1] == ")":
                i += 2
            else:
                ans += 1
                i += 1

            if count > 0:
                count -= 1
            else:
                ans += 1

    ans += count * 2
    return ans


print(minInsertions("(()))"))   
print(minInsertions("())"))     
print(minInsertions("))())("))  