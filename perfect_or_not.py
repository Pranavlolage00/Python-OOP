n=int(input("enter number:"))
s=0
num=n
print("input number=",num)
for i in range(1,n):
    if(n%i==0):
        s=s+i

if(s==num):
    print("number is perfect")
else:
    print("number is not perfect")
    

    

