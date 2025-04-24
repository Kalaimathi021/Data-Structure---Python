def push(stack, a):
    stack.append(a)

def pop(stack):
    return stack.pop()

def match(a, b):
    if a == '(' and b == ')':
        return True
    if a == '{' and b == '}':
        return True
    if a == '[' and b == ']':
        return True
    return False


def check(exp):
    stack = []
    for char in exp:
        if char in '{[(':
            push(stack, char)
        elif char in '}])':
            if not stack:
                print("Right parenthesis is more than the left one")
                return False
            else:
                temp = pop(stack)
                if not match(temp, char):
                    print(f"Mismatched parenthesis are {temp} and {char}")
                    return False
    if stack:
        print("Left parenthesis is more than the right one")
        return False
    else:
        print("Balanced")
        return True
if __name__ == "__main__":
    exp = input("Enter an expression: ")
    valid = check(exp)
    if valid:
        print("\nExpression is balanced")
    else:
        print("\nExpression is unbalanced")
