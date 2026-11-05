def kidsWithCandies(candies, extraCandies):
    ans = []
    maxx = max(candies)

    for candy in candies:
        candy_extra =candy + extraCandies
        if candy_extra >= maxx:
            ans.append(True)
        else:
            ans.append(False)

    return ans

print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))