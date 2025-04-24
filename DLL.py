class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.temp=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the no of data for the nodes:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
                self.prev=newnode 
            else:
                self.temp.next=newnode
                newnode.prev=self.temp
                self.temp=newnode
    def display(self):
        self.temp=self.head 
        while self.temp is not None:
            print(self.temp.data, end ="->")
            self.temp=self.temp.next
        print("None") 
    def InsertionAtBegin(self):
        print("Insertion At Begin of the list:")
        data=int(input("Enter the node data:")) 
        newnode=Node(data)
        self.temp=self.head
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def InsertionAtEnd(self):
        print("Insertion At End of the list:")
        data=int(input("Enter the node data:"))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
    
    def InsertionAtMiddle(self):
        print("Insertion At Middle of the list:")
        data=int(input("Enter the node data:"))
        newnode=Node(data)
        self.temp=self.head
        position=int(input("Enter the position value:"))
        for i in range(position-1):
            self.temp=self.temp.next
        newnode.next=self.temp
        newnode.prev=self.temp.prev
        self.temp.prev.next=newnode
        self.temp.prev=newnode
    
    def DeletionAtBegin(self):
        print("Deletion at Begin of node:")
        self.temp=self.head
        self.head=self.head.next
        del(self.temp)
        self.head.prev=None
    
    def DeletionAtEnd(self):
        print("Deletion at End of node:")
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.prev.next=None
        del(self.temp)
    
    def DeletionAtMiddle(self):
        print("Deletion at Middle of node:")
        position =int(input("Enter the position to remove from node:"))
        self.temp=self.head
        for i in range(position-1):
            self.temp=self.temp.next
        self.temp.prev.next=self.temp.next
        self.temp.next.prev=self.temp.prev.next
        del(self.temp)
    
    def count(self):
        print("count the Nodes:")
        c=0
        self.temp=self.head
        while self.temp is not None:
            self.temp=self.temp.next
            c=c+1
        print(c)
    
    def searchingelement(self):
        value=int(input("Enter  the data to search the node:"))
        self.temp=self.head
        while self.temp.next is not None:
            if (self.temp.data==value):
                print("The element is  found  in the Node")
            else:
                self.temp=self.temp.next
        if(self.temp.data==value):
            print("The element is found in the node.")
        else:
            print("The element is not found in the node.")
    
a=DLL()
a.creation()
a.display()
a.InsertionAtBegin()
a.display()
a.InsertionAtEnd()
a.display()
a.InsertionAtMiddle()
a.display()
a.DeletionAtBegin()
a.display()
a.DeletionAtEnd()
a.display()
a.DeletionAtMiddle()
a.display()
a.count()
a.searchingelement()
