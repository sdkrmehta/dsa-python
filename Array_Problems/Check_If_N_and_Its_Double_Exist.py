def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j] * 2:
                return True

    return False

print(checkIfExist([10, 2, 5, 3]))  
print(checkIfExist([3, 1, 7, 11]))  
