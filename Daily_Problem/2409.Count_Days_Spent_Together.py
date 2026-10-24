def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):

    def day_of_year(date):
        month = int(date[:2])
        day = int(date[3:])

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total = day

        for i in range(month - 1):
            total += days_in_month[i]

        return total

    alice_start = day_of_year(arriveAlice)
    alice_end = day_of_year(leaveAlice)

    bob_start = day_of_year(arriveBob)
    bob_end = day_of_year(leaveBob)

    start = max(alice_start, bob_start)
    end = min(alice_end, bob_end)

    if start > end:
        return 0

    return end - start + 1

print(countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
print(countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))