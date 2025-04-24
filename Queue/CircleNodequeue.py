#completed
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class CircularLinkedListQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   

    def enqueue(self, data):
        newnode = Node(data)
        if self.front is None and self.rear is None:  
            self.front = newnode
            self.rear = newnode
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = newnode
            self.rear = newnode
            self.rear.next = self.front  # Circular link

    def dequeue(self):
        if self.front is None and self.rear is None:  
            print("Underflow!")
        elif self.front == self.rear:  # Only one element in the queue
            print("Deleted element:", self.front.data)
            self.front = self.rear = None
        else:
            temp=self.front
            print("Deleted element:", self.front.data)
            self.front = self.front.next
            self.rear.next = self.front  
            del(temp)

    def display(self):
        if self.front is None:  
            print("Queue is empty!")
        else:
            print("Queue elements:")
            temp = self.front
            while True:
                print(temp.data, end="->")
                temp = temp.next
                if temp == self.front:  # Full circular iteration
                    break

    def peek(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            print("Front element:", self.front.data)



n=int(input("Enter the queue no of node:"))
a=CircularLinkedListQueue()
for i in range(1,n+1):
    data=int(input("Enter the data elements:"))
    a.enqueue(data)
a.display()
a.peek()
a.dequeue()
a.display()