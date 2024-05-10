num=int(input("enter number:"))
s=0
print("given number=",num)
while(num>0):
    d=num%10
    s+=d
    num=num/10
    num=int(num)
print("sum of digit=",s)
