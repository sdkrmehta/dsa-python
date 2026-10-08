def minimumTime(time, totalTrips):
    left = 1
    right = min(time) * totalTrips

    while left < right:
        mid = (left + right) // 2
        count = 0

        for i in range(len(time)):
            count += (mid // time[i])

        if count >= totalTrips:
            right = mid
        else:
            left = mid + 1

    return left

print(minimumTime(time = [1,2,3], totalTrips = 5))
print(minimumTime(time = [2], totalTrips = 1))
print(minimumTime(time = [10, 20, 30, 40], totalTrips = 100))