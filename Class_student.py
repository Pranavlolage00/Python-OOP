class student:
    def accept(self):
        self.rno=input("enter number:")
        self.sname=input("enter Sname:")
        self.per=input("enter percentage:")
        return
    def disp(self):
        print("roll Number=",self.rno)
        print("Student name=",self.sname)
        print("student percentage=",self.per)
        return

ob=student()
ob.accept()
ob.disp()
