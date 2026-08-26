def replaceElements(arr):
    max_value = -1

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_value
        max_value = max(max_value, current)

    return arr
 
print(replaceElements(arr = [17,18,5,4,6,1]))
print(replaceElements(arr = [17]))