class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
#end of class
a=int(input("Enter Value of A:"))
b=int(input("Enter Value of B:"))
ob=cal(a,b)
ch=1
while ch!=0:
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("0-Exit")
    ch=int(input("Enter choice"))
    if ch==1:
        print("Result=",ob.add())
    elif ch==2:
        print("Result=",ob.sub())
    elif ch==3:
        print("Result=",ob.mul())
    elif ch==4:
        print("Result=",ob.div())
    elif ch==0:
        print("Exited....!:")
    
print()
        
    
        
        
