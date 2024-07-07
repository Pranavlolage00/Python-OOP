def sum(a):
    s=0
    for val in a:
        s=s+val
    return s

n=int(input("Enter Limit:"))
a=list([])
for i in range(0,n):
    val=int(input("Enter Number:"))
    a.append(val)

print("Sum of All List Memebers:",sum(a))
