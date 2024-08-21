class Area:
    def accepts(self):
        self.s=float(input("Enter Side :"))
        return
    def acceptr(self):
        self.b=float(input("Enter Base:"))
        self.h=float(input("Enter height:"))
        return
class Square(Area):
    def calcs(self):
        ans=self.s*self.s
        print("Area of Square=",ans)
        return
class React(Area):
    def calcr(self):
        ans=self.b*self.h
        print("Area of Reactangle=",ans)
        return

ob1=React()
ob2=Square()

ob2.accepts()
ob2.calcs()

ob1.acceptr()
ob1.calcr()
    
