def wordPattern(pattern, s):
    words = s.split(' ')
    if len(words) != len(pattern): 
        return False

    letter_to_word = {}
    sett = set()

    for i in range(len(pattern)):
        if pattern[i] not in letter_to_word:
            if words[i] in sett: 
                return False
            else:
                letter_to_word[pattern[i]] = words[i]
                sett.add(words[i])
        elif letter_to_word[pattern[i]] != words[i]:
            return False

    return True

print(wordPattern( pattern = "abba", s = "dog cat cat dog"))