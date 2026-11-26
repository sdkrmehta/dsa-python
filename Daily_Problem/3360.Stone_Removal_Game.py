def canAliceWin(n):
    count = 10
    ans = 0

    while n >= count:
        n -= count
        count -= 1
        ans += 1

    return ans % 2 == 1

print(canAliceWin(n = 12))
print(canAliceWin(n = 1))
print(canAliceWin(n = 10))
print(canAliceWin(n = 50))