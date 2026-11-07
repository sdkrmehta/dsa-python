import itertools

def countValidSubstrings(s):
    count = 0
    left = -1

    for i in range(len(s)):
        if i >= 2 and s[i - 2] == "a" and s[i - 1] == "b" and s[i] == "c":
            left = i - 2
            
        count += i - left

    return count

print(countValidSubstrings(s = "abac"))
print(countValidSubstrings(s = "abc"))