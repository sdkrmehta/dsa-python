def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # swap
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

print(selection_sort([5, 2, 3, 1]))