class Stack:
    def __init__(self,n):
        self.size=n
        self.stack=[-1]*n
        self.top=-1
    def push(self,element):
        if self.top==self.size-1:
            print("Overflow")
        else:
            self.top += 1
            self.stack[self.top]=element
    def pop(self):
        if self.top == -1:
            print("Underflow")
        else: 
            print("Element popped",self.stack[self.top])
            self.top -= 1
  
    def peek(self):
        if self.top == -1:
            print("Underflow")
        else:
            print("Element at the top pf the stack is",self.stack[self.top])

if __name__== "_main_":
    n=int(input("Enter the size of stack"))
    s=Stack(n)
    for i in range (n):
        s.push(int(input("Enter the element to push in to the stack")))
    s.pop()
    s.peek()