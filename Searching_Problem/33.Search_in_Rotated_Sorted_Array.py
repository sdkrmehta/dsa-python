class Solution:
    def findPivot(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return right

    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums: list[int], target: int) -> int:
        pivotIndex = self.findPivot(nums)

        idx = self.binarySearch(nums, 0, pivotIndex - 1, target)

        if idx != -1:
            return idx

        return self.binarySearch(nums, pivotIndex, len(nums) - 1, target)

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
solution = Solution()
answer = solution.search(nums, target)
print(answer)