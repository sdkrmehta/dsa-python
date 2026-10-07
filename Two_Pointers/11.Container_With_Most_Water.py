def maxArea(height):
    left = 0
    right = len(height) - 1
    maxx = 0

    while left < right:
        dist = right - left
        minn = min(height[left], height[right])
        prod = minn * dist
        maxx = max(maxx, prod)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return maxx

print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(maxArea(height = [1,1]))