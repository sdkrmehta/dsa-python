def findErrorNums(nums):
    seen = set()
    for num in nums:
        if num in seen:
            dup = num
        seen.add(num)

    for num in range(1, len(nums)+1):
        if num not in seen:
            miss = num
            break

    return [dup, miss]

print(findErrorNums(nums = [1,2,2,4]))
print(findErrorNums(nums = [1,1]))
print(findErrorNums(nums = [2,2]))
