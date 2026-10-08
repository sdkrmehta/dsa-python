def successfulPairs(spells, potions, success):
    potions.sort()
    ans = []

    for spell in spells:
        left = 0
        right = len(potions) - 1

        while left <= right:
            mid = (left + right) // 2

            if spell * potions[mid] >= success:
                right = mid - 1
            else:
                left = mid + 1

        ans.append(len(potions) - left)

    return ans

print(successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))