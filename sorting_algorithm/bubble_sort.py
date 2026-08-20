def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        isSwap = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                # swap
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

                isSwap = True

        # This must be outside the inner loop
        if not isSwap:
            break

    return nums


print(bubble_sort([5, 2, 3, 1]))