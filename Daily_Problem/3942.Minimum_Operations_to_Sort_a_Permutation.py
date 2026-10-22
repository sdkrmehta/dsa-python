from math import inf

def minOperations(nums):
    n = len(nums)
    zero = nums.index(0)
    
    def check(step):
        for i in range(1, n):
            prev = (zero + (i - 1) * step) % n
            curr = (zero + i * step) % n
            if nums[prev] > nums[curr]:
                return False
        return True
        
    ans = inf
    
    if check(1):
        ans = min(ans, zero)
        ans = min(ans, n - zero + 2)
        
    if check(-1):
        ans = min(ans, zero + 2)
        ans = min(ans, n - zero)
        
    return ans if ans != inf else -1

print(minOperations(nums = [0,2,1]))
print(minOperations(nums = [1,0,2]))