def countIntersectingIntervals(intervals):
    count = 0

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                count += 1
    return count

print(countIntersectingIntervals(intervals = [[1,2],[2,3],[3,4]]))
print(countIntersectingIntervals(intervals = [[1,5],[2,4],[3,6]]))