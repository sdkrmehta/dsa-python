def isAnagram(s, t):
    lst1 = list(s)
    lst2 = list(t)

    lst1.sort()
    lst2.sort()

    if lst1 == lst2:
        return True
    else:
        return False

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))