def minMoves(nums):
    maxx = max(nums)
    count = 0

    for num in nums:
        if num != maxx:
            count += maxx - num

    return count

print(minMoves(nums = [2,1,3]))
print(minMoves(nums = [4,4,5]))