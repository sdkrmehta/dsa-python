def checkString(s):    
    sorted_text = "".join(sorted(s))
    return s == sorted_text

print(checkString(s = "aaabbb"))
print(checkString(s = "abab"))
print(checkString(s = "bbb"))