def frequencySort(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    ans = sorted(count, key=lambda x: (count[x], -x))
    result = []

    for num in ans:
        for i in range(count[num]):
            result.append(num)

    return result


print(frequencySort([1, 1, 2, 2, 2, 3]))