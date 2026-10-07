def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1
    ans = letters[0]

    while left <= right:
        mid = (left + right) // 2

        if ord(letters[mid]) > ord(target):
            ans = letters[mid]
            right = mid - 1
        else:
            left = mid + 1

    return ans

print(nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))