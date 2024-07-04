a={"rno":101,"name":"om","per":45}
print("dictionary=",a)
s1=str(a)
key=input("enter key to search :")
if key in s1:
    print("key is already exist in disctionary")
else:
    print("key is not found")

