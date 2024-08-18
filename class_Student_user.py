class Student:
    def accept(self,rno,sname,per):
        self.rno=rno
        self.sname=sname
        self.per=per
        return
    def disp(self):
        print("Roll Number=",self.rno)
        print("Student Sname=",self.sname)
        print("Student Per=",self.per)
        return

ob=Student()
rno=input("Enter Number:")
sname=input("Enter Sname:")
per=input("Enter percentage")
ob.accept(rno,sname,per)
ob.disp()
