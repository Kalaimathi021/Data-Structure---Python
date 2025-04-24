class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def Priority(self, operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

def infixToPostfix(expr):
    s = Stack()
    postfix = []
    for char in expr:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            s.push(char)
        elif char == ')':
            while s.stack and s.stack[-1] != '(':
                postfix.append(s.pop())
            s.pop()  
        else:
            while s.stack and s.Priority(char) <= s.Priority(s.stack[-1]):
                postfix.append(s.pop())
            s.push(char)
    while s.stack:
        postfix.append(s.pop())
    return postfix

if __name__ == '__main__':
    expr = input("Enter the infix expression: ")
    result = infixToPostfix(expr)
    print(''.join(result))
