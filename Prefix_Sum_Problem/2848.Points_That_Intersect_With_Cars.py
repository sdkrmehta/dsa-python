def numberOfPoints(nums):
    sett = set()

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if j == 0:
                for k in range(nums[i][j], nums[i][j + 1] + 1):
                    sett.add(k)

    return len(sett)

print(numberOfPoints(nums = [[3,6],[1,5],[4,7]]))