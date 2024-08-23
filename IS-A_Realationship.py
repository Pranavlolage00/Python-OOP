class emp:
    def accepte(self):
        self.eno=input("Enter Eno:")
        self.ename=input("Enter Ename:")
        self.sal=input("Enter salary")
        return
class Demo(emp):
    def disp(self,ob):
        print("Employee Number=",ob.eno)
        print("Employee Name=",ob.ename)
        print("Emloyee salary=",ob.sal)
        return

ob=emp()
ob1=Demo()
ob.accepte()
ob1.disp(ob)
