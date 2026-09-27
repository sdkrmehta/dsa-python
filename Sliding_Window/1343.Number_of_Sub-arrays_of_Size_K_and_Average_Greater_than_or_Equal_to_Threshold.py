def numOfSubarrays(arr, k, threshold):
    n = len(arr)
    curr_sum = 0
    count = 0

    for i in range(k):
        curr_sum += arr[i]

    if curr_sum / k >= threshold:
        count += 1

    for i in range(k, n):
        curr_sum += arr[i]
        curr_sum -= arr[i - k]

        avg = curr_sum / k

        if avg >= threshold:
            count += 1

    return count


print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
print(numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))