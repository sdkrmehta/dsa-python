import re

def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    words = re.findall(r'\b\w+\b', paragraph)
    count = {}

    for word in words:
        if word not in banned:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    return max(count, key=count.get)

print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(mostCommonWord(paragraph = "a.", banned = []))