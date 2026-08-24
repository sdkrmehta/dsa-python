def smallerNumbersThanCurrent(nums):
    lst = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]:
                count += 1

        lst.append(count)
    return lst

print(smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(smallerNumbersThanCurrent(nums = [7,7,7,7]))