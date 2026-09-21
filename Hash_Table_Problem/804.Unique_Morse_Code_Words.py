def uniqueMorseRepresentations(words):
    code = [
        ".-", "-...", "-.-.", "-..", ".", "..-.",
        "--.", "....", "..", ".---", "-.-", ".-..",
        "--", "-.", "---", ".--.", "--.-", ".-.",
        "...", "-", "..-", "...-", ".--", "-..-",
        "-.--", "--.."
    ]

    table = {}

    for i in range(26):
        table[chr(97 + i)] = code[i]

    ans = set()

    for word in words:
        morse = ""

        for ch in word:
            morse += table[ch]

        ans.add(morse)

    return len(ans) 

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))




# def uniqueMorseRepresentations(words):
#     code = [
#         ".-", "-...", "-.-.", "-..", ".", "..-.",
#         "--.", "....", "..", ".---", "-.-", ".-..",
#         "--", "-.", "---", ".--.", "--.-", ".-.",
#         "...", "-", "..-", "...-", ".--", "-..-",
#         "-.--", "--.."
#     ]

#     ans = set()

#     for i in range(len(words)):
#         morse = ""

#         for j in range(len(words[i])):
#             ascii_value = ord(words[i][j])
#             val = ascii_value - 97
#             morse += code[val]

#         ans.add(morse)

#     return len(ans)