def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        sol = (mid * (mid + 1)) // 2

        if sol == n:
            return mid
        elif sol < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

print(arrangeCoins(n = 5))
print(arrangeCoins(n = 1))