def getSneakyNumbers(nums):
    count = {}
    ans = []

    for num in nums:
        if num in count:
            ans.append(num)
        else:
            count[num] = 1

    return ans

print(getSneakyNumbers(nums = [7,1,5,4,3,4,6,0,9,5,8,2]))
print(getSneakyNumbers(nums = [0,3,2,1,3,2]))