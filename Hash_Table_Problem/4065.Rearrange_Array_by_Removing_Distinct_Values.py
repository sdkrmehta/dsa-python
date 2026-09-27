def rearrangeArray(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    values = sorted(count)
    ans = []

    while len(ans) < len(nums):
        for num in values:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1

    return ans

print(rearrangeArray(nums = [3,1,3,2,1,3]))
print(rearrangeArray(nums = [7,7,4,4,4]))