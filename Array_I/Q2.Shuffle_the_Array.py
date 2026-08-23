def shuffle(nums,n):
    ans = []
    for i in range(0, n):
        ans.append(nums[i])
        ans.append(nums[i+n])
        
    return ans

print(shuffle(nums = [2,5,1,3,4,7], n = 3))
print(shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))