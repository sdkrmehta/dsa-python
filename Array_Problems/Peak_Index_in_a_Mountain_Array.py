def peakIndexInMountainArray(arr):
    n = len(arr)
    l = 0
    r = n-2
    ans = n-1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1

    return ans

print(peakIndexInMountainArray(arr = [0,1,0]))
print(peakIndexInMountainArray(arr = [0,2,1,0]))
print(peakIndexInMountainArray(arr = [0,10,5,2]))