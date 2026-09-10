def findTheDifference(s: str, t: str):
    s = list(str(s)) 
    t = list(str(t))

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                t.pop(j)
                break
            
    return t[0]

print(findTheDifference( s= "abcd", t = "abcde"))