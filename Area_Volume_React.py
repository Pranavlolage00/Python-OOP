class Rectangle:
    def accept(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        return
    def Area(self):
        self.a=self.l*self.w
        print("Area of rectangle=",self.a)
        return
    def Volume(self):
        self.v=self.l*self.w*self.h
        print("Volume of rectangle=",self.v)
        return

ob=Rectangle()
ob.accept(2,5,6)
ob.Area()
ob.Volume()
        
