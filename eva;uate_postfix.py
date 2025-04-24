def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():  # If token is a number
            stack.append(int(token))
        else:  # If token is an operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)  # Integer division
    return stack.pop()

# Example Usage
expression = "6 2 3 + - 3 8 2 / + *"
result = evaluate_postfix(expression)
print(f"The result of the postfix expression '{expression}' is: {result}")
