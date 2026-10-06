def mySqrt(x):
    if x == 0:
        return 0
    
    left = 1
    right = x
    ans = 1

    while left <= right:
        mid = (left + right) // 2
        midsq = mid * mid

        if midsq > x:
            right = mid -1
        else:
            ans = mid
            left = mid + 1

    return ans

print(mySqrt(x = 9))
print(mySqrt(x = 0))
print(mySqrt(x = 5))