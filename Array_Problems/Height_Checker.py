def heightChecker(heights):
    count = 0
    height = sorted(heights)

    for i in range(len(heights)):
        if heights[i] != height[i]:
            count += 1
    return count

print(heightChecker(heights = [1,1,4,2,1,3]))