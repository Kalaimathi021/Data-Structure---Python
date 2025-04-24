class PolyNode:
    def __init__(self, coeff, exp):
        self.coeff = coeff  # Coefficient of the term
        self.exp = exp      # Exponent of the term
        self.next = None    # Pointer to the next term

class Polynomial:
    def __init__(self):
        self.head = None  # Head of the linked list

    def add_term(self, coeff, exp):
        new_node = PolyNode(coeff, exp)
        if not self.head or self.head.exp < exp:  # Insert at the head if the list is empty or exponent is highest
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.exp >= exp:  # Traverse to the correct position
                temp = temp.next
            #if temp.exp == exp:  # If same exponent exists, add coefficients
                #temp.coeff += coeff
            #else:
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

def add_polynomials(poly1, poly2):
    result = Polynomial()
    p1 = poly1.head
    p2 = poly2.head

    while p1 and p2:
        if p1.exp > p2.exp:
            result.add_term(p1.coeff, p1.exp)
            p1 = p1.next
        elif p1.exp < p2.exp:
            result.add_term(p2.coeff, p2.exp)
            p2 = p2.next
        else:
            result.add_term(p1.coeff + p2.coeff, p1.exp)
            p1 = p1.next
            p2 = p2.next

    while p1:
        result.add_term(p1.coeff, p1.exp)
        p1 = p1.next

    while p2:
        result.add_term(p2.coeff, p2.exp)
        p2 = p2.next

    return result

# Example Usage
poly1 = Polynomial()
poly1.add_term(5, 3)
poly1.add_term(4, 2)
poly1.add_term(2, 0)

poly2 = Polynomial()
poly2.add_term(3, 4)
poly2.add_term(4, 3)
poly2.add_term(1, 2)
poly2.add_term(6, 0)

print("Polynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()

result = add_polynomials(poly1, poly2)
print("Resultant Polynomial:")
result.display()
