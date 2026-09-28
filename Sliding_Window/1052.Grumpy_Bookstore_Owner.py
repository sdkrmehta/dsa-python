def maxSatisfied(customers, grumpy, minutes):
    curr_sum = 0
    max_sum = 0

    for i in range(minutes):
        if grumpy[i] == 1:
            curr_sum += customers[i]

    max_sum = curr_sum

    for i in range(minutes, len(customers)):
        if grumpy[i] == 1:
            curr_sum += customers[i]

        if grumpy[i - minutes] == 1:
            curr_sum -= customers[i - minutes]

        max_sum = max(max_sum, curr_sum)

    ans = 0

    for i in range(len(customers)):
        if grumpy[i] == 0:
            ans += customers[i]

    return ans + max_sum


print(maxSatisfied(
    customers=[1,0,1,2,1,1,7,5],
    grumpy=[0,1,0,1,0,1,0,1],
    minutes=3
))

print(maxSatisfied(
    customers=[4,10,10],
    grumpy=[1,1,0],
    minutes=2
))