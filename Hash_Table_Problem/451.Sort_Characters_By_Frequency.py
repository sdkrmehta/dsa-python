def frequencySort(s):
    count = {}

    for st in s:
        if st in count:
            count[st] += 1
        else:
            count[st] = 1

    ans = ""
    
    for key, value in sorted(count.items(), key = lambda x: x[1], reverse = True):
        ans += key * value

    return ans

print(frequencySort(s = "tree"))
print(frequencySort(s = "cccaaa"))
print(frequencySort(s = "Aabb"))