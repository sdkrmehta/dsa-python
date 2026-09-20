def shortestCompletingWord(licensePlate, words):
    licensePlate = licensePlate.lower()
    count = {}

    for ch in licensePlate:
        if 'a' <= ch <= 'z':
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

    shortest = None

    for word in words:
        word_count = {}

        for ch in word:
            if ch in word_count:
                word_count[ch] += 1
            else:
                word_count[ch] = 1

        valid = True

        for ch in count:
            if ch not in word_count or word_count[ch] < count[ch]:
                valid = False
                break

        if valid:
            if shortest is None or len(word) < len(shortest):
                shortest = word

    return shortest


print(shortestCompletingWord(
    "1s3 PSt",
    ["step", "steps", "stripe", "stepple"]
))