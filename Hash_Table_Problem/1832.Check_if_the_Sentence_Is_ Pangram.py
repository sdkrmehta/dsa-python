def checkIfPangram(sentence):
    ans = set(sentence)
    return len(ans) == 26

print(checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram(sentence = "leetcode"))