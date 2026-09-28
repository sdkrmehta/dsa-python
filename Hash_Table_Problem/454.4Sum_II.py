def fourSumCount(nums1, nums2, nums3, nums4):
    count = 0
    count1 = {}

    for num1 in nums1:
        for num2 in nums2:
            total = num1 + num2

            if total in count1:
                count1[total] += 1
            else:
                count1[total] = 1

    for num3 in nums3:
        for num4 in nums4:
            total = num3 + num4

            if -total in count1:
                count += count1[-total]

    return count



print(fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))







# def fourSumCount(nums1, nums2, nums3, nums4):
#     count1 = {}
#     count2 = {}
#     count3 = {}
#     count4 = {}
#     count = 0

#     for num in nums1:
#         if num in count1:
#             count1[num] += 1
#         else:
#             count1[num] = 1

#     for num in nums2:
#         if num in count2:
#             count2[num] += 1
#         else:
#             count2[num] = 1

#     for num in nums3:
#         if num in count3:
#             count3[num] += 1
#         else:
#             count3[num] = 1

#     for num in nums4:
#         if num in count4:
#             count4[num] += 1
#         else:
#             count4[num] = 1

#     for key1, value1 in count1.items():
#         for key2, value2 in count2.items():
#             for key3, value3 in count3.items():
#                 for key4, value4 in count4.items():
#                     if (key1 + key2 + key3 + key4) == 0:
#                         count += value1 * value2 * value3 * value4

#     return count