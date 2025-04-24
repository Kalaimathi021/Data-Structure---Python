class PolyNode:
    def __init__(self, coeff, exp):
        self.coeff = coeff  
        self.exp = exp      
        self.next = None    

class Polynomial:
    def __init__(self):
        self.head = None 

    def insert_term(self, coeff, exp):
        new_node = PolyNode(coeff, exp)
        if not self.head or self.head.exp < exp:  
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.exp >= exp:  
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            if temp.exp != 0:
                print(f"{temp.coeff}x^{temp.exp}", end=" + " if temp.next else "")
            else:
                print(f"{temp.coeff}", end="")
            temp = temp.next
        print()


poly = Polynomial()
poly.insert_term(4, 3)  # 4x^3
poly.insert_term(3, 2)  # 3x^2
poly.insert_term(5, 1)  # 5x
poly.insert_term(7, 0)  # 7


poly.display()  # Output: 4x^3 + 3x^2 + 5x + 7
