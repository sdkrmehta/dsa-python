def findDisappearedNumbers(nums):
    nums_set = set(nums)
    lst = []

    for i in range(1, len(nums)+1):
        if i not in nums_set:
            lst.append(i)
    return lst

print(findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers(nums = [1,1]))