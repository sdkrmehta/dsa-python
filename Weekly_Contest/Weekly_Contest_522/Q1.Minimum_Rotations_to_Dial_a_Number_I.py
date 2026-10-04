def minRotations(s):
    nums = []
    ans = []

    for x in s:
        nums.append(int(x))    

    for i in range(len(nums)):
        if i == 0:
            diff = abs(nums[i] - 0)
        else:
            diff = abs(nums[i] - nums[i - 1])

        minn = min(diff, 10 - diff)
        ans.append(minn)

    return sum(ans)

print(minRotations(s = "0192837465"))
print(minRotations(s = "1200210200"))
print(minRotations(s = "6042195975"))