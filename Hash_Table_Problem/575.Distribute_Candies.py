def distributeCandies(candyType):
    n = len(candyType) // 2
    ans = set(candyType)

    if len(ans) < n:
        return len(ans)

    else:
        return n    

print(distributeCandies(candyType = [1,1,2,2,3,3]))
print(distributeCandies(candyType = [6,6,6,6]))