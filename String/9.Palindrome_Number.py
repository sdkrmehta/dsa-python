def isPalindrome(x):
    x = list(str(x))
    y = x[::-1]
    ans = False

    if x == y:
        ans = True

    return ans

print(isPalindrome(x = -121))
print(isPalindrome(x = 121))