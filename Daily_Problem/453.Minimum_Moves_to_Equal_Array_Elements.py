def minMoves(nums):
        return sum(nums) - len(nums) * min(nums)

print(minMoves(nums = [1,2,3]))