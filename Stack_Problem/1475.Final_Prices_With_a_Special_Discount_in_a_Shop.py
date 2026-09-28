def finalPrices(prices):
    stack = []

    for i in range(len(prices)):
        found = False
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                price = prices[i] - prices[j]
                stack.append(price)
                found = True
                break

        if not found:
            stack.append(prices[i])

    return stack

print(finalPrices(prices = [8,4,6,2,3]))