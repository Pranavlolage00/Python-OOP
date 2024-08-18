class Emp:
    def __init__(self,*var):
        self.val=var
        return
    def disp(self):
        #print("emp information=",self.val)
        print("Employee Number=",self.val[0])
        print("Employee Name=",self.val[1])
        print("Employee Salary=",self.val[2])
        return

ob=Emp(11,"om",50000)
ob.disp()
