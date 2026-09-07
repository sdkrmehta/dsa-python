def intersect(nums1, nums2):
    ans = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums2[j] == nums1[i]:
                ans.append(nums1[i])
                nums2.pop(j)
                break
    return ans

print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))