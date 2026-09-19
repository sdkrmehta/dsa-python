def findShortestSubArray(nums):

    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    max_freq = max(count.values())

    first = {}
    last = {}

    for i in range(len(nums)):
        if nums[i] not in first:
            first[nums[i]] = i

        last[nums[i]] = i

    ans = len(nums)

    for num in count:
        if count[num] == max_freq:
            length = last[num] - first[num] + 1
            ans = min(ans, length)

    return ans

print(findShortestSubArray(nums = [1,2,2,3,1]))