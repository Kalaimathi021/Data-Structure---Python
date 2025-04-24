#completed 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def Create(self):
        num = int(input("Enter number of nodes: "))
        for _ in range(num):
            data = int(input("Enter data: "))
            newnode = Node(data)

            if self.head is None:
                self.head = newnode
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = newnode

    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def Insert_begin(self):
        data = int(input("\nEnter data: "))
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def Insert_middle(self):
        data = int(input("\nEnter data: "))
        n = int(input("Enter the position: "))
        newnode = Node(data)
        
        if n <= 0:
            print("Invalid position.")
            return
        
        if n == 1:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        for i in range(n - 2):
            if temp is None:
                print("Position exceeds list length.")
                return
            temp = temp.next
        
        newnode.next = temp.next if temp else None
        if temp:
            temp.next = newnode

    def Insert_end(self):
        data = int(input("\nEnter data: "))
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def Delete_start(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def Delete_middle(self):
        n = int(input("Enter the position: "))
        if n <= 0 or self.head is None:
            print("Invalid position or list is empty.")
            return

        if n == 1:
            self.Delete_start()
            return

        temp = self.head
        for i in range(n - 2):
            if temp is None or temp.next is None:
                print("Position exceeds list length.")
                return
            temp = temp.next

        if temp.next is not None:
            del_node = temp.next
            temp.next = del_node.next
            del del_node

    def Delete_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            del self.head
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        del_node = temp.next
        temp.next = None
        del del_node

    def Count(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print("Node count:", count)

# Example usage
s1 = SLL()
s1.Create()
s1.Display()
s1.Insert_begin()
s1.Display()
s1.Insert_middle()
s1.Display()
s1.Insert_end()
s1.Display()
s1.Delete_start()
s1.Display()
s1.Delete_middle()
s1.Display()
s1.Delete_end()
s1.Display()
s1.Count()
