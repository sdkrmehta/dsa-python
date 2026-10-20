def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    ans = []

    for interval in intervals:
        if not ans or interval[0] > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans

print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))