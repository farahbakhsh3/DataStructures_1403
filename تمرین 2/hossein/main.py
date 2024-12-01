#ساخت آرایه پشته
class Stack:
    data:list=list()
    def __init__(self,data:list):
        self.data=data
    def __eq__(self,other):
        self.data==other
    def __str__(self):
        return str(self.data)
    @staticmethod
    def use():
        return Stack.data.pop()
#تبدیل عبارت میانوندی به عبارت پسوندی
def suffix():
    postfix=list()
    for ent in input("enter the phrase: "):
        if ent=="(" or ent==")" or ent=="*" or ent=="+" :
            Stack.data.append(ent)
        else:
            postfix.append(ent)
    while len(Stack.data)!=0:
        if Stack.data[len(Stack.data)-1]=="(" or Stack.data[len(Stack.data)-1]==")":
            Stack.data.pop()
        else:
            postfix.append(Stack.data.pop())
    ext=str()
    for ex in postfix:
        ext+=ex
    print("your suffix phrase is: "+ext)
#تبدیل عبارت میانوندی به عبارت پیشوندی
def prefix():
    postfix=list()
    inp=input("enter the phrase: ")
    for i in range(len(inp)-1,-1,-1):
        if inp[i]==")" or inp[i]=="*" or inp[i]=="+":
            Stack.data.append(inp[i])
        elif inp[i]=="(":
            j=0
            while j!=2:
                if Stack.data[len(Stack.data)-1]=="+" or Stack.data[len(Stack.data)-1]=="*":
                    postfix.append(Stack.data.pop()) 
                      
                else:
                    Stack.data.pop()
                j+=1
        else:
            postfix.append(inp[i])
    if len(Stack.data)==0:
        ext=""
        for ex in [postfix[i] for i in range(len(postfix)-1,-1,-1)]:
            ext+=ex
    print("your prefix phrase is: "+ext)
if __name__=="__main__":
    pass