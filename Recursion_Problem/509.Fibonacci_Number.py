def fib(n):
    # base case
    if n==0 or n==1:
        return n
    # rescursive case
    return fib(n-1) + fib(n-2)

print(fib(4))