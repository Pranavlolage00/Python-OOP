class Internal:
    def accepti(self):
        self.inter=int(input("Enter Internal Marks:"))
        return
class External:
    def accepte(self):
        self.exter=int(input("Enter External Marks:"))
        return
class result(Internal,External):
    def calc(self):
        self.res=self.inter+self.exter/5
        print("Percentage=",self.res)
        return

ob=result()
ob.accepti()
ob.accepte()
ob.calc()
        
