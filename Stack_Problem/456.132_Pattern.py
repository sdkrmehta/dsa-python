def find132pattern(nums):
        stack = []
        second = float('-inf')

        for num in reversed(nums):
            if num < second:
                return True

            while stack and num > stack[-1]:
                second = stack.pop()

            stack.append(num)

        return False

print(find132pattern(nums = [1, 2, 3, 4]))
print(find132pattern(nums = [3, 1, 4, 2]))
print(find132pattern(nums = [-1, 3, 2, 0]))