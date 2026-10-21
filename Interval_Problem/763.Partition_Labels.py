def partitionLabels(s):
    count = {}

    for i in range(len(s)):
        count[s[i]] = i

    ans = []
    start = 0
    end = 0

    for i in range(len(s)):
        end = max(end, count[s[i]])

        if i == end:
            ans.append(end - start + 1)
            start = i + 1

    return ans

print(partitionLabels(s = "ababcbacadefegdehijhklij"))
print(partitionLabels(s = "eccbbbbdec"))