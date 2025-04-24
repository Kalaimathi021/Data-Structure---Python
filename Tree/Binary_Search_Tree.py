class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inOrder(self, temp):
        if temp is None:
            return
        self.inOrder(temp.left)
        print(temp.data, end=" ")
        self.inOrder(temp.right)

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = new
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new
                        break
                    else:
                        temp = temp.right

# Create BST object and insert values
obj = BST()
for i in [30, 20, 40, 70, 60, 80]:
    obj.insert(i)

# Print in-order traversal of the tree
obj.inOrder(obj.root)
print()

# Insert another value and print in-order traversal again
obj.insert(100)
obj.inOrder(obj.root)
print()