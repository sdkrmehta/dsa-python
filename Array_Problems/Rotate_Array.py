nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

k = k % len(nums)

last = nums[-k:]
first = nums[:-k]

nums[:] = last + first

print(nums)