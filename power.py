def pow(x,y):
    a=1
    for i in range(1,y+1):
        a=x*a
    print("Power=",x,"^",y,"=",a)
    return

x=int(input("Enter value of x:"))
y=int(input("Enter value of Y:"))

pow(x,y)

    
