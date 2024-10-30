#Write a python script to define a class student having members roll no, name, age, 
#gender. Create a subclass called Test with member marks of 3 subjects. Create three 
#objects of the Test class and display all the details of the student with total marks.

class student:
    def accepts(self):
        self.rno=int(input("Enter Roll No:"))
        self.sname=input("Enter Sname:")
        self.age=int(input("Enter your age:"))
        self.gender=input("Enter Your Gender:")
        return
class Test(student):
    def acceptm(self):
        m1=int(input("Enter MArk"))
        m2=int(input("Enter MArk"))
        m3=int(input("Enter MArk"))
        self.tot=m1+m2+m3
        return
    def disp(self):
        print("Roll no=",self.rno)
        print("Student Name=",self.sname)
        print("Age=",self.age)
        print("Gender=",self.gender)
        print("Total Marks=",self.tot)
        return

obj1=Test()
obj2=Test()
obj3=Test()

obj1.accepts()
obj1.acceptm()
obj1.disp()

obj2.accepts()
obj2.acceptm()
obj2.disp()

obj3.accepts()
obj3.acceptm()
obj3.disp()


            
        
                     
        
