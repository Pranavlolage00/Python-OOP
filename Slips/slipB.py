#Define a class Employee having members id, name, department, salary. Create a 
#subclass called manager with member bonus. Define methods accept and display in 
#both the classes. Create n objects of the manager class and display the details of the 
#manager having the maximum total salary (salary+bonus).

class Employee:
    def accepte(self):
        self.id=int(input("Enter Employee id"))
        self.name=input("Enter Employee name:")
        self.dept=input("Enter Employee department:")
        self.sal=int(input("Enter Employee salary"))
        return

class manager(Employee):
    def acceptb(self):
        self.bonus=int(input("Enter Bonus:"))
        return
    
    def disp(self):
        print("Employee id=",self.id)
        print("Employee name=",self.dept)
        print("Employee department=",self.sal)
        return

n=int(input("Enter Limit:"))
obj=[]
for i in range(n):
    ob=manager()
    ob.accepte()
    ob.acceptb()
    obj.append(ob)

        
        
        
 
