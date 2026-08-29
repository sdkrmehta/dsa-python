def romanToInt(s):
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ans = 0

    for i in range(len(s) - 1):
        if nums[s[i]] < nums[s[i + 1]]:
            ans -= nums[s[i]]
        elif nums[s[i]] >= nums[s[i + 1]]:
            ans += nums[s[i]]

    ans += nums[s[-1]]

    return ans

print(romanToInt("MCMXCIV"))
print(romanToInt("LVIII"))

