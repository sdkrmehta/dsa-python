import math

def maxLength(nums):
    n = len(nums)
    ans = 0

    for i in range(n):
        gcd = 0
        lcm = 1
        prod = 1

        for j in range(i, n):
            num = nums[j]

            gcd = math.gcd(gcd, num)
            lcm = math.lcm(lcm, num)
            prod *= num

            if gcd * lcm == prod:
                ans = max(ans, j - i + 1)

    return ans


print(maxLength([1, 2, 1, 2, 1, 1, 1]))
print(maxLength([2, 3, 4, 5, 6]))
print(maxLength([1, 2, 3, 1, 4, 5, 1]))