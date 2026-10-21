def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    count = 1
    end = points[0][1]

    for point in points:
        if point[0] > end:
            count += 1
            end = point[1]

    return count

print(findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))