class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
        self.temp = None
        self.temp1 = None
        
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self.temp = self.root
            queue = [self.temp]  # Use a queue to implement level order insertion
            
            while queue:
                self.temp = queue.pop(0)
                
                if self.temp.left is None:
                    self.temp.left = node
                    break
                else:
                    queue.append(self.temp.left)
                    
                if self.temp.right is None:
                    self.temp.right = node
                    break
                else:
                    queue.append(self.temp.right)
    
    def inorder(self, temp):
        if temp is None:
            return 
        self.inorder(temp.left)
        print(temp.data, end=" ")
        self.inorder(temp.right)
        
    def preorder(self, temp):
        if temp is None:
            return 
        print(temp.data, end=" ")
        self.preorder(temp.left)       
        self.preorder(temp.right)

if __name__ == "__main__":  # Fixed the syntax error here
    obj = BinaryTree()
    
    while True:
        choice = int(input("Enter 1 to insert, 0 to exit: "))
        if choice == 1:
            data = int(input("Enter the element: "))
            obj.insert(data)
        else:
            break
    
    print("\nInorder traversal of the tree:")
    obj.inorder(obj.root)
    
    print("\nPreorder traversal of the tree:")
    obj.preorder(obj.root)
