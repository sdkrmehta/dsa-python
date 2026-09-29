def timeRequiredToBuy(tickets, k):
    queue = []

    for i in range(len(tickets)):
        queue.append(i)

    time = 0

    while tickets[k] > 0:
        person = queue.pop(0)

        tickets[person] -= 1
        time += 1

        if tickets[person] > 0:
            queue.append(person)

    return time

print(timeRequiredToBuy(tickets = [2,3,2], k = 2))