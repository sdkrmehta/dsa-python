def pivotInteger(n):
    prefix = []
    suffix = [0] * n
    totalP = 0
    totalS = 0
    nums = []

    for i in range(n):
        nums.append(i + 1)

    for num in nums:
        totalP += num
        prefix.append(totalP)

    for i in range(len(nums) -1, -1, -1):
        totalS += nums[i]
        suffix[i] = totalS

    for i in range(len(prefix)):
        if prefix[i] == suffix[i]:
            return i + 1

    return -1

print(pivotInteger(n = 8))
print(pivotInteger(n = 1))
print(pivotInteger(n = 4))
    