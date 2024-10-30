#Write a Python script using class, which has two methods get_String and 
#print_String. get_String accept a string from the user and print_String print the string in 
#upper case.

class Demo:
    def get_String(self):
        self.s1=input("Enter String :")
        return
    def print_String(self):
        self.s1=self.s1.upper()
        print(self.s1)
        return

ob=Demo()
ob.get_String()
ob.print_String()
