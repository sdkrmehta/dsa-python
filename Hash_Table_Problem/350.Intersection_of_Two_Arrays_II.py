from collections import Counter

def intersect(nums1, nums2):
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        ans = []

        for num in counter1:
            if num in counter2:
                count = min(counter1[num], counter2[num])

                for i in range(count):
                    ans.append(num)

        return ans

print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))