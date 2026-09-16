def findMissingElements(nums):
    ans1 = {}
    ans2 = []

    for num in nums:
        if num in ans1:
            ans1[num] += 1
        else:
            ans1[num] = 1

    max1 = max(nums)
    min1 = min(nums)

    for i in range(min1, max1 ):
        if i not in ans1:
            ans2.append(i)

    return ans2

print(findMissingElements(nums = [1,4,2,5]))
print(findMissingElements(nums = [7,8,6,9]))
print(findMissingElements(nums = [5, 1]))