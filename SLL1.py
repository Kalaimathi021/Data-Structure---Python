# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:  # Singly Linked List (SLL) class to handle linked list operations
    def __init__(self):
        self.head = None  # Head of the linked list
        self.temp = None  # Temporary pointer for traversing the list

    # Method to create the linked list
    def creation(self):
        num = int(input("Enter the number of nodes:"))
        for i in range(num):
            data = int(input("Enter data for node {}:".format(i + 1)))  # Data for each Node
            newnode = Node(data)  # Create a new node
            if self.head is None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode

    # Method to display the linked list
    def display(self):
        self.temp = self.head
        if self.head is None:
            print("The list is empty.")
            return
        while self.temp is not None:
            print(self.temp.data, end=" -> ")
            self.temp = self.temp.next
        print("None")

    # Method to search for a node by value
    def search(self):
        search_data = int(input("Enter the value to search for:"))
        self.temp = self.head
        while self.temp:
            if self.temp.data == search_data:
                print(f"Node with data {search_data} found.")
                return
            self.temp = self.temp.next
        print(f"Node with data {search_data} not found.")

    # Common delete method (delete by value)
    def delete(self, target_data):
        self.temp = self.head
        if self.head is None:
            print("The list is empty, cannot delete.")
            return

        # If the target node is the head
        if self.head.data == target_data:
            self.head = self.head.next
            return

        # Search for the target node and delete it
        prev = None
        while self.temp and self.temp.data != target_data:
            prev = self.temp
            self.temp = self.temp.next

        if self.temp is None:
            print(f"Node with data {target_data} not found.")
            return

        prev.next = self.temp.next
        del self.temp


# Main program to test Singly Linked List operations
a = SLL()
a.creation()
a.display()

a.search()  # Searching for a node

# Example of using the delete method by value
delete_value = int(input("Enter the node value to delete: "))
a.delete(delete_value)
a.display()
4