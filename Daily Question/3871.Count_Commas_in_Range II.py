def countCommas(n):
    count = 0

    start = 1000
    commas = 1

    while start <= n:

        end = start * 1000 - 1

        if end > n:
            end = n

        numbers = end - start + 1

        count += numbers * commas

        start = start * 1000
        commas += 1

    return count

print(countCommas(n = 1002))