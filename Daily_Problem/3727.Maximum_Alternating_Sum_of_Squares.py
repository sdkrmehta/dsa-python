def maxAlternatingSum(nums):
    A = sorted(a * a for a in nums)
        
    return sum(A) - sum(A[:len(A) // 2]) * 2

print(maxAlternatingSum(nums = [1,2,3]))
print(maxAlternatingSum(nums = [1,-1,2,-2,3,-3]))