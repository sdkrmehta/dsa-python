import heapq

def largestInteger(num):
    digits = list(str(num))

    even = []
    odd = []

    for d in digits:
        if int(d) % 2 == 0:
            heapq.heappush(even, -int(d))
        else:
            heapq.heappush(odd, -int(d))

    ans = []

    for d in digits:
        if int(d) % 2 == 0:
            ans.append(str(-heapq.heappop(even)))
        else:
            ans.append(str(-heapq.heappop(odd)))

    return int("".join(ans))

print(largestInteger(num = 1234))
print(largestInteger(num = 65875))




# def largestInteger(num):
#     digit = []
#     even = []
#     odd = []

#     while num > 0:
#         digit.append(num % 10)
#         num //= 10

#     for i in digit:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)

#     ans = []
#     even.sort()
#     odd.sort()

#     for i in range(len(digit) -1, -1, -1):
#         if digit[i] % 2 == 0:
#             ans.append(even[-1])
#             even.pop(-1)
#         else:
#             ans.append(odd[-1])
#             odd.pop()

#     return int("".join(str(x) for x in ans))