def thirdMax(nums):
    num = set(nums)
    num = list(num)

    if len(num) < 3:
        return max(num)

    num = sorted(num, reverse = True)
    return num[2]

print(thirdMax(nums = [3,2,1]))
print(thirdMax(nums = [2,2,3,1]))
print(thirdMax(nums = [2,1]))