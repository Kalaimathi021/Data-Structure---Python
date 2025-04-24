class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newnode=Node(data)
        if(self.front is None and self.rear is None):
            self.rear=newnode
            self.front=newnode
        else:
            self.rear.next=newnode
            self.rear=self.rear.next
    def dequeue(self):
        if (self.front==None and self.rear==None):
            print("Under flow!")
        elif(self.front==self.rear):
            temp=self.front
            self.rear=None
            self.front=None
            del(temp)
        else:
            temp=self.front
            self.front=self.front.next
            del(temp)
    def peek(self):
        print("The first element:",self.front.data)
    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            current = self.front
            print("The Queue linked list elements:")
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None") 

n=int(input("Enter the queue no of node:"))
a=Queue()
for i in range(1,n+1):
    data=int(input("Enter the data elements:"))
    a.enqueue(data)
a.display()
a.peek()
a.dequeue()
a.display()

