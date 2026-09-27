def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    count = 0

    for word in words:
        consistent = True

        for char in word:
            if char not in allowed_set:
                consistent = False
                break

        if consistent:
            count += 1

    return count


print(countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))




# def countConsistentStrings(allowed, words):
    # allowed = list(allowed)
    # ans = []

    # for i in range(len(words)):
    #     word = ""

    #     for j in range(len(words[i])):
    #         if words[i][j] not in word:
    #             word += words[i][j]

    #     ans.append(word)

    # count = 0

    # for i in range(len(ans)):
    #     consistent = True

    #     for j in range(len(ans[i])):
    #         if ans[i][j] not in allowed:
    #             consistent = False
    #             break

    #     if consistent:
    #         count += 1

    # return count