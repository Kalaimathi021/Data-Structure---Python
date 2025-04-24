class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack1:
    def __init__(self):
        self.top=None
        self.temp=None
    def push(self,data):
        newnode=Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):# delete the first element
        if self.top is None:
            print("Under flow!")
        else:
            self.temp=self.top
            self.top=self.top.next
            del(self.temp)
    def peek(self):# print the first node data
        if self.top is None:
            print("Under flow!")
        else:
            print(f"The first node data:{self.top.data}")
    def display(self):
        if self.top is None:
            print("Under flow!")
        else:
            self.temp=self.top
            while self.temp is not None:
                print(self.temp.data ,end="->")
                self.temp=self.temp.next
            print("None")

s=Stack1()
n=int(input("Enter the number of nodes:"))
for i in range(n):
    data=int(input("Enter the data for list:"))
    s.push(data)
s.display()
s.pop()
s.display()
s.peek()


