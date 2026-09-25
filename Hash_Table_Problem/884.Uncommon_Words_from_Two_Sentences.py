def uncommonFromSentences(s1, s2):
    count1 = {}
    count2 = {}

    for word in s1.split():
        if word in count1:
            count1[word] += 1
        else:
            count1[word] = 1

    for word in s2.split():
        if word in count2:
            count2[word] += 1
        else:
            count2[word] = 1

    ans = []

    for word in count1:
        if count1[word] == 1 and word not in count2:
            ans.append(word)

    for word in count2:
        if count2[word] == 1 and word not in count1:
            ans.append(word)

    return ans

print(uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(uncommonFromSentences(s1 = "apple apple", s2 = "banana"))