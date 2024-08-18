class Demo:
    def __init__(self):
        self.s1=input("enter String")
        return

    def __add__(self,obj):
        print("Concatnet of two Strings.",obj.s1+self.s1)
        return

ob1=Demo()
ob2=Demo()
ob1+ob2
