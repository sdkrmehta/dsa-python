def numOfUnplacedFruits(fruits, baskets):
    count = 0

    for i in range(len(fruits)):
        for j in range(len(baskets)):
            if fruits[i] <= baskets[j]:
                baskets.pop(j)
                break
        else:
            count += 1

    return count

print(numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))
print(numOfUnplacedFruits(fruits = [5], baskets = [3]))