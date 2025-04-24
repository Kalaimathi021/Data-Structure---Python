class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        
        return root

    def calculate_height(self, node):
        if node is None:
            return -1  # Height of an empty tree is -1

        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        return 1 + max(left_height, right_height)

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(node.data, end=" ")
            self.inorderTraversal(node.right)

if __name__ == '__main__':
    n = int(input("Enter number of nodes: "))
    root_data = int(input("Enter root node data: "))
    bst = BinarySearchTree(root_data)
    
    for _ in range(n - 1):
        data = int(input("Enter node data: "))
        bst.insertNode(bst.root, data)

    print("Inorder traversal: ")
    bst.inorderTraversal(bst.root)
    print("\nHeight of the tree: ")
    print(bst.calculate_height(bst.root))
