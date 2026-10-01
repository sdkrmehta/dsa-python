from collections import deque

def deckRevealedIncreasing(deck):
    deck.sort()
    n = len(deck)
    queue = deque(range(n))
    ans = [0] * n

    for card in deck:
        index = queue.popleft()
        ans[index] = card

        if queue:
            queue.append(queue.popleft())

    return ans

print(deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))