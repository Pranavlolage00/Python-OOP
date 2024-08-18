class Student:
    def accept(self,rno,sname,per):
        self.rno=rno
        self.sname=sname
        self.per=per
        return
    def disp(self):
        print("Roll Number=",self.rno)
        print("Sname Number=",self.sname)
        print("Per Number=",self.per)
        return

ob=Student()
ob.accept("101","om","55.66")
ob.disp()
