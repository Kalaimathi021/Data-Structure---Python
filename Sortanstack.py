class Stack:
    def __init__(self,n):
        self.top = -1
        self.size = n
        self.stack = [-1]*n
    def push(self,data): # push the element for top of our stack
        if self.top == self.size - 1:
            print("Overflow!")
        else:
            self.top =self.top+1
            self.stack[self.top] = data
    def pop(self):  # Delete the top element
        if self.top == -1:
            print("Underflow!")
            return None
        else:
            popped_value = self.stack[self.top]
            self.top=self.top- 1
            return popped_value
    def peek(self): # Print the first element in our stack
        if self.top == -1:
            print("Underflow!")
            return None
        else:
            return self.stack[self.top]
    def is_empty(self):
        return self.top == -1
    def display(self):
        if self.top==-1:
            print("Stack is empty!")
        else:
            for i in range(self.top + 1):
                print(self.stack[i], end="->")
        print("None")
    def sort_stack(self):
        temp_stack = Stack(self.size)  
        while not self.is_empty():
            current = self.pop()  # Pop from original stack and move into the temp_stack

            while not temp_stack.is_empty() and temp_stack.peek() < current:
                self.push(temp_stack.pop())
            temp_stack.push(current)
    
    # Move elements back from temp_stack to the original stack in sorted order
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

if __name__=="__main__":
    n = int(input("Enter the list size: "))
    s = Stack(n)
    for i in range(n):
        data = int(input("Enter the data for stack: "))
        s.push(data)
    print("Original Stack:")
    s.display()
    s.sort_stack()
    print("Sorted Stack in Ascending Order:")
    s.display()

