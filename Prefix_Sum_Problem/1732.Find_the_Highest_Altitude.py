def largestAltitude(gain):
    prefix = []
    total = 0

    for i in range(len(gain)):
        total += gain[i]
        prefix.append(total)

    return max(0, max(prefix))

print(largestAltitude(gain = [-5,1,5,0,-7]))
print(largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))
print(largestAltitude(gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]))