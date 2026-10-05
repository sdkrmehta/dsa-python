def sumOddLengthSubarrays(arr):
    total = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if len(arr[i:j]) % 2 != 0:
                total += sum(arr[i:j])

    return total


print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))