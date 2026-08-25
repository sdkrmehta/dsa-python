def sortedSquares(nums):
    my_list = []
    for i in range(len(nums)):
        my_list.append(nums[i]**2)
    my_list.sort()
    return my_list

print(sortedSquares(nums = [-7,-3,2,3,11]))
print(sortedSquares(nums = [-4,-1,0,3,10]))

    