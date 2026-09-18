def longestPalindrome(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    ans = 0
    odd = False

    for char in count:
        if count[char] % 2 == 0:
            ans += count[char]
        else:
            ans += count[char] - 1
            odd = True

    if odd:
        ans += 1

    return ans

print(longestPalindrome("abccccdd"))