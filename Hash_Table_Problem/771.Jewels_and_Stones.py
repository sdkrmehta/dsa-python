def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    stones_list = list(stones)

    count = 0

    for i in range(len(stones_list)):
        if stones_list[i] in jewels_set:
            count += 1
    return count

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))