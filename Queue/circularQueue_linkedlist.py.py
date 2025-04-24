class Node:
    def _init_(self,data):
        self.data=data
        self.next=None


class Queue:
    def _init_(self):
        self.front=None
        self.rear=None

    def EnQueue (self,data):

        if self.front==None and self.rear==None:
            newnode = Node(data)
            self.front=newnode
            self.rear=newnode

        else:
            newnode = Node(data)
            self.rear.next = newnode
            self.rear=self.rear.next

    def Dequeue(self):
        if self.front==None and self.rear==None:
            print("Underflow")
        
        elif(self.rear==self.front):
            temp=self.front
            print("Deleted Node:",self.rear.data)
            self.rear=self.front=None
            del(temp)
        else:
            temp=self.front
            print("Deleted Node:",self.front.data)
            self.front=self.front.next
            del(temp)

    def Display(self):
        temp=self.front
        while temp.next is not None:
            print(temp.data, end="->")
            temp=temp.next
        print()

obj=Queue()
obj.EnQueue(10)
obj.EnQueue(20)
obj.EnQueue(30)
obj.EnQueue(40)

obj.Display()

obj.Dequeue()
obj.Display()