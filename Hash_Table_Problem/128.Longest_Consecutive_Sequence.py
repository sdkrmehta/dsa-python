def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest

print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive(nums = [100,4,200,1,3,2]))
print(longestConsecutive(nums = [1,0,1,2]))