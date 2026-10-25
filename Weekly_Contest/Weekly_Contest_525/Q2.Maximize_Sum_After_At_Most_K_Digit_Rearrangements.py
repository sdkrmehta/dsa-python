import heapq

def maximizeSum(nums, k):
    gains = []
    
    for num in nums:
        digits = sorted(str(num), reverse=True)
        max_num = int("".join(digits))
        gain = max_num - num
        gains.append((gain, max_num))

    gains.sort(reverse=True)

    total = sum(nums)

    for i in range(min(k, len(nums))):
        gain, max_num = gains[i]
        total += gain

    return total


print(maximizeSum(nums = [123,45], k = 1))
print(maximizeSum(nums = [102,90,14], k = 2))