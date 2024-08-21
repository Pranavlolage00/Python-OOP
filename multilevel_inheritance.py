class Team:
    def __init__(self,tname):
        self.tname=tname
class Dev(Team):
    def __init__(self,tname,role):
        super().__init__(tname)
        self.role=role
class employee(Dev):
    def __init__(self,tname,role,ename):
        super().__init__(tname,role)
        self.ename=ename
        return
    def disp(self):
        print("Team Name=",self.tname)
        print("Emp ROle=",self.role)
        print("Emp Name=",self.ename)
        return
ob=employee("mca","manager","om")
ob.disp()


        
