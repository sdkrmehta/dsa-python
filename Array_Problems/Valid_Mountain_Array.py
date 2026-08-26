def validMountainArray(arr):
    if len(arr) < 3:
        return False

    else:
        i = 0
        n = len(arr)

        # Go up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False

        # Go down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # We should reach the end
        return i == n - 1

print(validMountainArray([0, 3, 2, 1]))      
print(validMountainArray([0, 2, 3, 3, 5]))   
print(validMountainArray([2, 1]))            