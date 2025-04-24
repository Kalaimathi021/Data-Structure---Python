class Stack:
    def __init__(self, n):
        self.top = -1
        self.size = n
        self.stack = [-1] * n  

    def push(self, data):
        if self.top == self.size - 1:  
            print("Overflow: Stack is full")
        else:
            self.top += 1  
            self.stack[self.top] = data  

    def pop(self):
        if self.top == -1:  
            print("Underflow: Stack is empty")
        else:
            popped_value = self.stack[self.top]  
            self.top -= 1  
            print(f"Popped: {popped_value}")  

    def peek(self):
        if self.top == -1:  
            print("Underflow: Stack is empty")
        else:
            print(f"Top element: {self.stack[self.top]}")  

    def display(self):
        if self.top == -1:  
            print("Underflow: Stack is empty")
        else:
            print("Stack elements (top to bottom):", end=" ")
            for i in range(self.top, -1, -1):  
                print(self.stack[i], end=" -> ")
            print("None")

n = int(input("Enter the stack size: "))
s = Stack(n)

for i in range(n):
    data = int(input("Enter the data to push onto the stack: "))
    s.push(data)

s.display()
s.pop()
s.display()
s.peek()
