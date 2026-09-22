def sumOfUnique(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    sums = 0

    for key, value in count.items():
        if value == 1:
            sums += key

    return sums

print(sumOfUnique(nums = [1,2,3,2]))
print(sumOfUnique(nums = [1,1,1,1,1]))