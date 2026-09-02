def reverseString(s):
    i = 0
    j = len(s) - 1

    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

        i += 1
        j -= 1

        
s = ["h","e","l","l","o"]
reverseString(s)
print(s)