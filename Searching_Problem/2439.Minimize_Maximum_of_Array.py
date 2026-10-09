class Solution:
    def isValid(self, nums, mid):
        arr = nums.copy()

        for i in range(len(arr) - 1):
            if arr[i] > mid:
                return False

            buffer = mid - arr[i]
            arr[i + 1] -= buffer

        return arr[-1] <= mid

    def minimizeArrayValue(self, nums):
        left = 1
        right = max(nums)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.isValid(nums, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

sc = Solution()
print(sc.minimizeArrayValue(nums = [3,7,1,6]))
print(sc.minimizeArrayValue(nums = [4,7,2,2,9,19,16,0,3,15]))