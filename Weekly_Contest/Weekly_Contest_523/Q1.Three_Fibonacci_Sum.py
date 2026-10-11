def threeFibonacciSum( n: int) -> bool:
        fibo = [0, 1]

        while fibo[-1] + fibo[-2] <= n:
            fibo.append(fibo[-1] + fibo[-2])

        for i in range(len(fibo)):
            for j in range(i, len(fibo)):
                for k in range(j, len(fibo)):
                    if fibo[i] + fibo[j] + fibo[k] == n:
                        return True

        return False

print(threeFibonacciSum(n = 8))