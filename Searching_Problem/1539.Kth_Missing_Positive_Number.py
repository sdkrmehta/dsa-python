def findKthPositive(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        miss = arr[mid] - (mid + 1)

        if miss < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k

print(findKthPositive(arr = [2,3,4,7,11], k = 5))




# def findKthPositive(arr, k):
#     ans = []

#     for i in range(1, len(arr) + k + 1):
#         if i not in arr:
#             ans.append(i)

#     return ans[k - 1]