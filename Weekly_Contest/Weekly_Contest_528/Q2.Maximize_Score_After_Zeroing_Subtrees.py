def maxScore(parent, op, score):
    n = len(parent)

    if n == 1:
        return score[0]

    children = [[] for _ in range(n)]

    for i in range(1, n):
        children[parent[i]].append(i)

    order = [0]
    head = 0

    while head < len(order):
        u = order[head]
        head += 1

        for c in children[u]:
            order.append(c)

    dp = [0] * n
    
    for u in reversed(order):
        if not children[u]:
            dp[u] = score[u]
        else:
            child_scores = [dp[c] for c in children[u]]
            total = sum(child_scores)
            minn = min(child_scores)

            if op[u] == 0:
                dp[u] = score[u] + total - min(0, minn)
            else:
                dp[u] = score[u] + total - minn

    return dp[0]

print(maxScore(parent = [-1,0,0,0,1,2,3,3], op = [1,1,0,0,1,1,0,1], score = [5,6,1,2,3,2,3,-3]))