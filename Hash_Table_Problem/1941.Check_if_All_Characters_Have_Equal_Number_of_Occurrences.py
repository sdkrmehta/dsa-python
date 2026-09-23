def areOccurrencesEqual(s):
    count = {}

    for st in s:
        if st in count:
            count[st] += 1
        else:
            count[st] = 1

    max_value = max(count.values())

    for value in count.values():
        if value % max_value != 0:
            return False

    return True

print(areOccurrencesEqual(s = "abacbc"))
print(areOccurrencesEqual(s = "aaabb"))
print(areOccurrencesEqual(s = "tveixwaeoezcf"))