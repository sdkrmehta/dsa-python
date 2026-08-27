def moveZeroes(nums):
    count = nums.count(0)

    for i in range(count):
        nums.remove(0)
        nums.append(0)
    return nums

print(moveZeroes(nums = [0,1,0,3,12]))