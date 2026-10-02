def findTheDistanceValue(arr1, arr2, d):
    count = 0

    for i in range(len(arr1)):
        valid = True

        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) <= d:
                valid = False
                break
        if valid == True:
            count += 1

    return count

print(findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))