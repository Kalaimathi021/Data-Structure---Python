#completed
class Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.q=[0]*size

    def EnQueue_At_Rear(self,data):

        if (self.rear+1)%self.size==self.front:
            print("Overflow")

        elif self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.q[self.rear]=data
        
        elif self.rear==self.size-1:
            self.rear=0
            self.q[self.rear]=data

        else:
            self.rear+=1
            self.q[self.rear]=data

    def EnQueue_At_Front(self,data):

        if (self.rear+1)%self.size==self.front:
            print("Overflow")

        elif self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.q[self.front]=data
        
        elif self.front==0:
            self.front=self.size-1
            self.q[self.front]=data

        else:
            self.front-=1
            self.q[self.front]=data

    def DeQueue_At_Front(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow")

        elif self.rear == self.front:
            print("Deleted Element", self.q[self.front])
            self.front = self.rear = -1   

        elif self.front==self.size-1:
            print("Deleted Element", self.q[self.front])
            self.front=0

        else:
            print("Deleted Element", self.q[self.front])
            self.front += 1

    def DeQueue_At_Rear(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow")

        elif self.rear == self.front:
            print("Deleted Element", self.q[self.rear])
            self.front = self.rear = -1   

        elif self.rear==0:
            print("Deleted Element", self.q[self.rear])
            self.rear=self.size-1

        else:
            print("Deleted Element", self.q[self.rear])
            self.rear-=1


    def Peek(self):
        return self.q[self.front]
    
    def Display(self):
        i=self.front
        while(i!=self.rear):
            print(self.q[i],end=" ")
            i=(i+1)%self.size
        print(self.q[i])

obj=Queue(5)

obj.EnQueue_At_Rear(10)
obj.EnQueue_At_Rear(20)
obj.EnQueue_At_Rear(30)

obj.EnQueue_At_Front(40)
obj.EnQueue_At_Front(50)

obj.Display()

obj.DeQueue_At_Front()
obj.DeQueue_At_Rear()

obj.Display()