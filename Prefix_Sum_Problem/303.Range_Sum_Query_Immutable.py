class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0

        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]

nums = [1, 2, 3, 4, 5]
obj = NumArray(nums)

print(obj.sumRange(1, 3))
print(obj.sumRange(0, 2))