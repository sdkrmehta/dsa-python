def equalFrequency(word):
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    freq = {}
    for value in count.values():
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1

    if len(freq) == 1:
        value = next(iter(freq))
        if value == 1 or len(count) == 1:
            return True
        return False

    if len(freq) == 2:

        values = list(freq.keys())

        a = values[0]
        b = values[1]

        if a == 1 and freq[a] == 1:
            return True
        if b == 1 and freq[b] == 1:
            return True
        if a == b + 1 and freq[a] == 1:
            return True
        if b == a + 1 and freq[b] == 1:
            return True

    return False

print(equalFrequency(word = "abcc"))
print(equalFrequency(word = "aazz"))