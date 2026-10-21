def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key = lambda x:x[0])

    ans = []
    
    for interval in intervals:
        if not ans or interval[0] > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans

print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))