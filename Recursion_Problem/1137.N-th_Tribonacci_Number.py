def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)

print(tribonacci(n = 4))
print(tribonacci(n = 25))