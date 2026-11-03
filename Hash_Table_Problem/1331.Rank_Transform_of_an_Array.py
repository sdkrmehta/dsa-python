def arrayRankTransform(arr):
    sett = set(arr)
    sett = sorted(sett)
    count = {}

    for i in range(len(sett)):
        count[sett[i]] = i + 1

    ans = []

    for num in arr:
        ans.append(count[num])

    return ans

print(arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))
print(arrayRankTransform(arr = [40,10,20,30]))
print(arrayRankTransform(arr = [100,100,100]))