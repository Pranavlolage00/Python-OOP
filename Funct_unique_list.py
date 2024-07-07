def Unique_list(a):
    print("Orignal List=",a)
    b=set(a)
    a=list([])
    for val in b:
        a.append(val)
    return a
a=[]
n=int(input("Enter Limit"))
for i in range(0,n):
    val=int(input("Enter Element:"))
    a.append(val)

print("unique List=",Unique_list(a))
