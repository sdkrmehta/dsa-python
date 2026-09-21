def checkPerfectNumber(num):
    if num <= 1:
        return False

    ans = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ans += i

            if i != num // i:
                ans += num // i

    return ans == num

print(checkPerfectNumber(num = 28))
print(checkPerfectNumber(num = 7))

# def checkPerfectNumber(num):
#     n = (num // 2) + 1
#     ans = 0

#     if (num % 2) == 0:
#         for i in range(1, n):
#             if (num % i) == 0:
#                 ans += i

#     else:
#         for i in range(1, n, 2):
#             if (num % i) == 0:
#                 ans += 1

#     return ans == num