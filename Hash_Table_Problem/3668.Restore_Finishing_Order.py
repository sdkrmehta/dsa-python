def recoverOrder(order, friends):
    friends = set(friends)
    ans = []

    for i in range(len(order)):
        if order[i] in friends:
            ans.append(order[i])

    return ans

print(recoverOrder(order = [3,1,2,5,4], friends = [1,3,4]))
print(recoverOrder(order = [1,4,5,3,2], friends = [2,5]))