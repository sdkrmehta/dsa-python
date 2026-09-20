def reverseDegre(s):
    result = 0

    for i in range(len(s)):
        ascii_value = ord(s[i])
        value = 123 - ascii_value
        result += value * (i + 1)

    return result


print(reverseDegre("abc"))
print(reverseDegre("zaza"))



# def reverseDegre(s):
#     ans = [] 

#     for st in s:
#         ascii_values = ord(st)
#         values = 123 - ascii_values
#         ans.append(values)

#     result = 0

#     for i in range(len(ans)):
#         result += ans[i] * (i + 1)

#     return result