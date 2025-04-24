class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BT:
    def __init__(self)->None:
        self.root = None
    
    def insertion(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            queue = [self.root]  
            while True:
                node=queue.pop(0)
                if node.left is None:
                    node.left = newnode
                    return
                else:
                    queue.append(node.left)

                if node.right is None:
                    node.right = newnode
                    return
                else:
                    queue.append(node.right)
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end='-->')
            self.inOrder(root.right)
    
    

obj = BT()
for i in [1, 2, 3, 4, 5, 6, 7]:
    obj.insertion(i)
obj.inOrder(obj.root)
print()
    
obj.insertion(100)
obj.insertion(200)
obj.inOrder(obj.root)
print()
