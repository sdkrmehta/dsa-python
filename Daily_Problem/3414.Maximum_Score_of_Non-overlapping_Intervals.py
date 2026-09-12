def maximumWeight(intervals):
    n = len(intervals)
    a = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
    a.sort(key=lambda x: x[1])

    ends = [x[1] for x in a]
    prev = [0] * n

    for i in range(n):
        prev[i] = bisect_left(ends, a[i][0]) - 1
    dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

    for k in range(1, 5):
        for i in range(1, n + 1):
            best = dp[k][i - 1]

            l, r, w, idx = a[i - 1]
            p = prev[i - 1] + 1

            old_score, old_indices = dp[k - 1][p]

            take_score = old_score + w
            take_indices = old_indices + (idx,)
            take_indices = tuple(sorted(take_indices))

            if take_score > best[0]:
                dp[k][i] = (take_score, take_indices)

            elif take_score == best[0]:
                dp[k][i] = min(best, (take_score, take_indices))

            else:
                dp[k][i] = best

    return list(dp[4][n][1])