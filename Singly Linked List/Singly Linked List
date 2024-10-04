# Node class to represent each node in the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL:# Singly Linked List (SLL) class to handle linked list operations
    def __init__(self):
        self.head = None # Head of the linked list
        self.temp = None # Temporary pointer for traversing the list
    def creation(self):
        num = int(input("Enter the no of nodes:"))
        for i in range(num):
            data = int(input("Enter the no of datas for the nodes:")) # Data for each Node
            newnode =Node(data) # create a newnode
            if self.head is None:
                self.head = newnode   
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode
# Method to display the linked list   
    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end ="->")
            self.temp = self.temp.next 
        print("None")


# Method to insert a node at the beginning of the list
    def insertionAtBegin(self):
        print("Insertion At Begin of the list:")
        data = int(input("Enter the node data:"))
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode


# Method to insert a node at the end of the list 
    def insertionAtEnd(self):
        print("Insertion At End of the list:")
        data = int(input("Enter the node value add in end of the list:"))
        newnode = Node(data)
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = newnode

# Method to insert a node at the middle of the list
    def insertionAtMiddle(self):
        print("Insertion At Middle of the list:")
        data = int(input("Enter the data value:"))
        newnode = Node(data)
        position = int(input("Enter the position value:"))
        self.temp = self.head
        for i in range(position-1):            
            prev = self.temp
            self.temp = self.temp.next
        newnode.next = self.temp
        prev.next = newnode

# Method to delete a  node from the beginning of the list
    def DeletionAtBegin(self):
        print("Deletion At Begin of the list:")
        self.temp = self.head
        self.head = self.head.next
        del(self.temp)

# Method to delete a node  from the end of the list
    def DeletionAtEnd(self):
        print("Deletion At End of the list:")
        self.temp = self.head
        while self.temp.next is not None:
            prev = self.temp
            self.temp = self.temp.next
        prev.next = None
        del(self.temp)

# Method to delete a node from the middle of the list
    def DeletionAtMiddle(self):
        print("Deletion At Middle of the list:")
        position = int(input("Enter the position value to remove:"))
        self.temp = self.head
        for i in range(position-1):
            prev = self.temp
            self.temp = self.temp.next
        prev.next = self.temp.next
        del(self.temp)
# method to count the number of nodes in the list       
    def count (self):
        print("The count Node:")
        self.temp=self.head
        c = 0
        while self.temp is not None:
            c=c+1
            self.temp=self.temp.next
        print(c)
    

a=SLL() 
a.creation()
a.display()   
a.insertionAtBegin()
a.display()   
a.insertionAtEnd()
a.display()
a.insertionAtMiddle()
a.display()
a.DeletionAtBegin()
a.display()
a.DeletionAtEnd()
a.display()
a.DeletionAtMiddle()
a.display()
a.count()

