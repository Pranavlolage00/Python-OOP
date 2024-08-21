class Circle:
    def accept(self):
        self.r=float(input("enter radius"))
        return
class demo(Circle):
    def find_Area(self):
        ans=3.14*self.r*self.r
        print("Area of Circle=",ans)
        return
    
ob=demo()
ob.accept()
ob.find_Area()
        
