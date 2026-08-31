def diagonalPrime(nums):

    n = len(nums)

    sol = []
    prime = []

    for i in range(n):
        sol.append(nums[i][i])

        if i != n - 1 - i:
            sol.append(nums[i][n - 1 - i])

    # Prime Number
    for num in sol:
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

    if prime:
        return max(prime)

    return 0

print(diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]]))
print(diagonalPrime(nums = [[1,2,3],[5,17,7],[9,11,10]]))