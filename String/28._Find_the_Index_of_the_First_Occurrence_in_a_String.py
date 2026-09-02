def strStr(haystack, needle):
    for i in range(len(haystack)):
        found = True

        for j in range(len(needle)):

            if i + j >= len(haystack):
                found = False
                break

            if haystack[i + j] != needle[j]:
                found = False
                break

        if found:
            return i

    return -1


print(strStr("sadbutsad", "sad"))
