class Node:
    def __init__(self,expr):
        self.expr=expr
        self.next=None
class BalanceOfparantheses:
    def __init__(self):
        self.top = None
        self.temp=None
    def validexpression(self,expr):
        for char in expr:
            if char in '[{(':
                self.push(char)
            elif char in ']})':
                if self.top is None: # To check stack is empty
                    print("Right parantheses is more than left")
                    return False
                else:
                    delete=self.pop()
                    if not self.Match(delete,char):
                        print("Parantheses mismatched",delete,char)
                        return False
        if not self.top:
            return  True
        else:
            print("Left parantheses is more than right")
            return False
        

    def push(self,expr):
        newnode=Node(expr)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):# delete the first element
        if self.top is None:
            print("Under flow!")
        else:
            self.temp=self.top
            self.top=self.top.next
            del(self.temp)
    def Match(delete,char):
        if delete =='{' and char=='}':
            return True
        if delete =='[ ' and char==']':
            return True
        if delete =='(' and char==')':
            return True
        return False








n=int(input("Enter the no of nodes:"))
s=BalanceOfparantheses()
for i in range(n):
    expr=input("Enter the expresssion value:")
    s.push(expr)
valid=s.validexpression(expr)
if  valid:
    print ("balanced")
else:
    print("UnBalanced")








    

     


