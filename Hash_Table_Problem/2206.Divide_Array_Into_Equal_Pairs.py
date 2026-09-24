def divideArray(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for value in count.values():
        if value % 2 == 0:
            continue
        else:
            return False

    return True

print(divideArray(nums = [3,2,3,2,2,2]))
print(divideArray(nums = [1,2,3,4]))