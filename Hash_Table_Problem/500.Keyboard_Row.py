def findWords(words):
    row = {}

    for char in "qwertyuiop":
        row[char] = 1

    for char in "asdfghjkl":
        row[char] = 2

    for char in "zxcvbnm":
        row[char] = 3

    ans = []

    for word in words:
        lower_word = word.lower()

        first = row[lower_word[0]]
        same_row = True

        for char in lower_word:
            if row[char] != first:
                same_row = False
                break

        if same_row:
            ans.append(word)

    return ans


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))