from collections import deque

def findTheWinner(n, k):
    queue = deque(range(1, n + 1))

    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())

        queue.popleft()

    return queue[0]

print(findTheWinner(n = 5, k = 2))