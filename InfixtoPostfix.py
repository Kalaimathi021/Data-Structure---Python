class stack:
    def __init__(self):
        self.stack=[]
    def push(self,char):
        self.stack.append(char)
    def pop(self):
        self.stack.pop()
    def priority(char):
        if char=='^':
            return 3
        elif char =='*' or char=='/':
            return 2
        elif char=='+' or char=='-':
            return 1
        return 0
def infixtopostfix (expr):
        postfix=[]
        s=stack()
        for char in expr:
            if char=='(':
                s.push(char)
            elif char.isalnum():
                postfix.append(char)
            elif char==')':
                x=s.pop()
                while x!='(':
                   postfix.append(x)
                   x=s.pop()
            else:
                while s.stack and s.priority(char)<=s.priority(s.stack[-1]):
                    postfix.append(s.pop())
                s.push(char)
        while s.stack:
            postfix.append(s.pop())
        return ''.join(postfix)
if __name__=='__main__':
    expr=input("Enter the expression:")
    print("Postfix expression:",infixtopostfix(expr))