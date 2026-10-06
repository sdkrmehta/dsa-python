def countValidSelections(nums):
    total = sum(nums)
    left_sum = 0
    count = 0

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]

        if nums[i] == 0:
            if left_sum == right_sum:
                count += 2
            elif abs(left_sum - right_sum) == 1:
                count += 1

        left_sum += nums[i]

    return count

print(countValidSelections(nums = [1,0,2,0,3]))