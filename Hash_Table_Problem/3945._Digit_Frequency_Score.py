def digitFrequencyScore(n):
    digit_list = []

    while n > 0:
        digit_list.append(n % 10)
        n //= 10
        
    digit_list.reverse()

    count = {}

    for num in digit_list:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    sums = 0

    for keys, values in count.items():
        sums += keys * values

    return sums

print(digitFrequencyScore(n = 122))
print(digitFrequencyScore(n = 101))