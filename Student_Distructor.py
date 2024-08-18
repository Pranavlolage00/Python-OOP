class Student:
    def accept(self):
        self.rno=input("Enter Roll no:")
        self.sname=input("Enter Sname:")
        print("Enter Three subject marks:")
        self.m=[]
        for i in range(0,3):
            val=int(input("Enter Marks:"))
            self.m.append(val)
        return
    def disp(self):
        self.s=0
        for i in range(0,3):
            self.s=self.s+self.m[i]
        print("Student Roll No=",self.rno)
        print("Student Name=",self.sname)
        print("Student Total Marks=",self.s)
        print("Student percentage=",self.s/3)
        return
    def __del__(self):
        del self.rno
        del self.sname
        del self.m
        print("Memory freee...!")
        return


n=int(input("Enter Limit:"))
a=[]
for i in range(0,n):
      ob=Student()
      ob.accept()
      a.append(ob)
print("Display n Students..")
for i in range(0,n):
      a[i].disp()
            
         
        
