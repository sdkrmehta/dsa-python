def isPerfectSquare(num):
    if num == 0 or num == 1:
        return True

    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid

        if num == sq:
            return True
        elif sq > num:
            right = mid - 1
        else:
            left = mid + 1

    return False

print(isPerfectSquare(num = 0))
print(isPerfectSquare(num = 1))
print(isPerfectSquare(num = 2))
print(isPerfectSquare(num = 3))
print(isPerfectSquare(num = 4))
print(isPerfectSquare(num = 5))
print(isPerfectSquare(num = 6))