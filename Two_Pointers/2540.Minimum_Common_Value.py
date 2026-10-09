def getCommon(nums1, nums2):
    left = 0
    right = 0

    while left < len(nums1) and right < len(nums2):
        if nums1[left] == nums2[right]:
            return nums1[left]
        elif nums1[left] > nums2[right]:
            right += 1
        else:
            left += 1

    return -1

print(getCommon(nums1 = [1,2,3], nums2 = [2,4]))