a=[]
print("enter 5 numbers")
for i in range(0,5):
    num=input("enter number:")
    a.append(num)
print("\n list elements=",a,end="")
b=set(a)
print("\nprint the set of elements",b,end="")
if(len(a)!=len(b)):
    print("\n duplicate")
else:
    print("\n not duplicate")



    
