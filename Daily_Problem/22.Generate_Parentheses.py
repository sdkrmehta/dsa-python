def generateParenthesis( n):
    answer = []

    def make_parentheses(current, open_count, close_count):
        if open_count == n and close_count == n:
            answer.append(current)
            return

        if open_count < n:
            make_parentheses(
                current + "(",
                open_count + 1,
                close_count
            )

        if close_count < open_count:
            make_parentheses(
                current + ")",
                open_count,
                close_count + 1
            )

    make_parentheses("", 0, 0)

    return answer

print(generateParenthesis(n = 3))
print(generateParenthesis(n = 10))