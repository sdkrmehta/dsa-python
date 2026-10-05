def numberOfPairs(nums1, nums2, k):
    count1 = {}
    count2 = {}
    count = 0

    for num in nums1:
        if num in count1:
            count1[num] += 1
        else:
            count1[num] = 1
    
    for num in nums2:
        if num in count2:
            count2[num] += 1
        else:
            count2[num] = 1

    for num1 in count1:
        for num2 in count2:
            if num1 % (num2 * k) == 0:
                count += count1[num1] * count2[num2]

    return count

print(numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
print(numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3))




# def numberOfPairs(nums1, nums2, k):
#     count = 0

#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums1[i] % (nums2[j] * k) == 0:
#                 count += 1

#     return count