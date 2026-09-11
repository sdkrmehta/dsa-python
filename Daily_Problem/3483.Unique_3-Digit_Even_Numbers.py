def totalNumbers(digits):
    count = 0
    ans = set()

    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                if i != j and k != i and k != j:
                    if digits[i] == 0:
                        continue

                    nums = (100 * digits[i]) + (10 * digits[j]) + digits[k]

                    if nums % 2 == 0:
                        if nums not in ans:
                            ans.add(nums)
                            count += 1

    return count

print(totalNumbers([1, 2, 3, 4]))
print(totalNumbers([0, 2, 2]))