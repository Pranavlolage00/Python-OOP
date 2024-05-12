s=input("enter string:")
a={}
for val in s:
    if(val in a):
        a[val]=a[val]+1
    else:
        a[val]=1

print(a)
    
