def evalRPN(tokens):
    stack = []

    for num in tokens:

        if num not in ["+", "-", "*", "/"]:
            stack.append(int(num))

        else:
            b = stack.pop()
            a = stack.pop()

            if num == "+":
                result = a + b

            elif num == "-":
                result = a - b

            elif num == "*":
                result = a * b

            elif num == "/":
                result = int(a / b)

            stack.append(result)

    return stack[0]

print(evalRPN(tokens = ["2","1","+","3","*"]))
print(evalRPN(tokens = ["4","13","5","/","+"]))
print(evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))