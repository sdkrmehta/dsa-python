def minimumPairRemoval(nums):
    count = 0

    while nums != sorted(nums):
        minn = float("inf")
        index = 0

        for i in range(len(nums) - 1):
            summ = nums[i] + nums[i + 1]
            if summ < minn:
                minn = summ
                index = i

        nums[index] = nums[index] + nums[index + 1]
        nums.pop(index + 1)
        count += 1

    return count

print(minimumPairRemoval(nums = [5, 2, 3, 1]))