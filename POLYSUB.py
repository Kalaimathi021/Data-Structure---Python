class Node:
    def __init__(self,coeff,expo):
       self.coeff=coeff
       self.expo=expo
       self.next=None
class POLY:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,coeff,expo):
            newnode=Node(coeff,expo)
            if self.head is None or newnode.expo>self.head.expo:
                newnode.next=self.head
                self.head=newnode
            else:
                self.temp=self.head
                while self.temp.next is not None and newnode.expo<self.temp.next.expo:
                    self.temp=self.temp.next
                newnode.next=self.temp.next
                self.temp.next=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            if self.temp.coeff > 0 :
                print(f"{self.temp.coeff}x^{self.temp.expo}",end="+")
                self.temp = self.temp.next
            else:
                print(f"{self.temp.coeff}x^{self.temp.expo}", end="-")
                self.temp = self.temp.next
        print("None")

p1=POLY()
num=int(input("Enter the no of polynomial node:"))
for i in range(num):
    coeff=int(input("Enter the coefficient value of node:"))
    expo=int(input("Enter the exponent value of node:"))
    p1.create(coeff,expo)

p2=POLY()
num=int(input("Enter the no of polynomial node:"))
for i in range(num):
    coeff=int(input("Enter the coefficient value of node:"))
    expo=int(input("Enter the exponent value of node:"))
    p2.create(coeff,expo)

def poly_sub(p1,p2):
    a1=p1.head
    a2=p2.head
    while a1 and a2:
        if a1.expo == a2.expo:
            res.create(a1.coeff - a2.coeff,a1.expo)
            a1=a1.next
            a2=a2.next
        else:
            if (a1.expo>a2.expo):
                res.create(a1.coeff,a1.expo)
                a1=a1.next
            else:
                res.create(a2.coeff,a2.expo)
                a2=a2.next
    while a1:
        res.create(a1.coeff,a1.expo)
        a1=a1.next
    while a2:
        res.create(a2.coeff,a2.expo)
        a2=a2.next

res=POLY()
poly_sub(p1,p2)
res.display()