import math

def subtractProductAndSum(n):
    ans = []
    while n > 0:
        ans.append(n % 10)
        n //= 10
    
    return math.prod(ans) - sum(ans)

print(subtractProductAndSum(n = 234))
print(subtractProductAndSum(n = 4421))