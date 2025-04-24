class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  
        self.front = self.rear = -1  
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty")
        elif self.front == self.rear:
            print("Deleted Element:", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Deleted Element:", self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty")
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[i])  

a = CircularQueue(5)
a.enqueue(14)
a.enqueue(28)
a.enqueue(34)
a.enqueue(20)
a.display()  

a.dequeue() 
a.display()  

a.enqueue(4) 
a.dequeue()   
a.display()   
