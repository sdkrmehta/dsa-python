def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev

        stack.append(i)

    return ans

print(dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(dailyTemperatures(temperatures = [30,40,50,60]))
print(dailyTemperatures(temperatures = [30,60,90]))