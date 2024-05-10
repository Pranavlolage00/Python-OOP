num=int(input("entrer number:"))
print("given number=",num)
c1=0
c2=0
c3=0
while(num>0):
    d=num%10
    if(d%2==0 and d!=0):
        c1+=1
    elif(d%2==1 and d!=0):
        c2+=1
    else:
        c3+=1
    num=num/10
    num=int(num)
print("even count=",c1)
print("odd count=",c2)
print("zero count=",c3)

    
