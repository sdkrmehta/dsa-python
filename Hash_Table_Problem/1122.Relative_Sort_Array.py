def relativeSortArray(arr1, arr2):
    count = {}
    ans = []

    for num in arr1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr2:
        if num in count:
            ans.extend([num] * count[num])
            count.pop(num)

    for key in sorted(count):
        ans.extend([key] * count[key])

    return ans

print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))