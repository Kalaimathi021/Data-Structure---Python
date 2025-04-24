class DoubleendedQueue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0]*self.size

    def enqueueatrear(self, data):
        print("Enqueue At Rear:")
        if (self.rear + 1) % self.size == self.front:  
            print("Overflow!")
        elif self.front == -1 and self.rear == -1:  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        elif self.rear == self.size - 1:  
            self.rear = 0
            self.queue[self.rear]=data
        else:
            self.rear = self.rear+1
            self.queue[self.rear] = data

    def enqueueatfront(self, data): 
        print("Enqueue At Front:")
        if (self.rear + 1) % self.size == self.front:  
            print("Overflow!")
        elif self.front == -1 and self.rear == -1:  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        elif self.front == 0:
            self.front = self.size - 1
            self.queue[self.front] = data
        else:
            self.front = self.front - 1      
            self.queue[self.front] = data

    def dequeueatfront(self):
        print("Dequeue At Front:")
        if self.front == -1 and self.rear == -1:  
            print("Underflow!")
        elif self.front == self.rear:  
            print("Deleted element:", self.queue[self.front])
            self.front = self.rear = -1
        elif self.front == self.size - 1:  
            print("Deleted element:", self.queue[self.front])
            self.front = 0
        else:
            print("Deleted element:", self.queue[self.front])
            self.front = self.front + 1

    def dequeueatrear(self): # unusual content
        print("Dequeue At Rear:")
        if self.front == -1 and self.rear == -1:  
            print("Underflow!")
        elif self.front == self.rear:  # Only one element left
            print("Deleted element:", self.queue[self.rear])
            self.front = self.rear = -1
        elif self.rear == 0:  
            print("Deleted element:", self.queue[self.rear])
            self.rear = self.size - 1
        else:
            print("Deleted element:", self.queue[self.rear])
            self.rear = self.rear - 1

    def display(self):
        if self.front == -1 and self.rear==-1:
            print("Queue is empty!")
        i = self.front
        while (i != (self.rear + 1) % self.size):
            print(self.queue[i], end=" -> ")
            i = (i + 1) % self.size
        print(self.queue[self.rear], "None")  
    def peek(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Front element:", self.queue[self.front])


size = int(input("Enter the queue size: "))
a = DoubleendedQueue(size)
for i in range(1, size + 1):
    data = int(input("Enter data element: "))
    a.enqueueatrear(data)
a.display()
a.dequeueatfront()  
a.display()