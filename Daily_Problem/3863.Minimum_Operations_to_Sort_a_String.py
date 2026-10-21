def minOperations(s):
    if s == "".join(sorted(s)):
        return 0
        
    n = len(s)
    if n == 2:
        return -1
        
    min_c = 0
    max_c = 0

    for i in range(n):
        if s[i] < s[min_c]:
            min_c = i
        if s[i] >= s[max_c]:
            max_c = i

    if min_c == 0 or max_c == n - 1:
        return 1
        
    if min_c == n - 1 and max_c == 0:
        return 3
        
    return 2

print(minOperations(s = "dog"))
print(minOperations(s = "card"))
print(minOperations(s = "gf"))