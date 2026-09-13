def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    ans1 = set1 - set2
    ans2 = set2 - set1

    return [ans1, ans2]

print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))