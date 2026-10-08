def findDays(weights, cap):
    days = 1
    load = 0

    for weight in weights:
        if load + weight > cap:
            days += 1
            load = weight
        else:
            load += weight

    return days

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left <= right:
        mid = (left + right) // 2
        numberOfDays = findDays(weights, mid)

        if numberOfDays <= days:
            right = mid - 1
        else:
            left = mid + 1

    return left

print(shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
print(shipWithinDays(weights = [1,2,3,1,1], days = 4))