a=[]
ch=0
while ch!=4:
    print("\n1-push() \n2-pop() \n3-disp() \n4-exit()")
    ch=int(input("enter choice:"))
    if(ch==1):
        num=int(input("enter number to push"))
        a.append(num)
        print(a)
        print("push successfully..")
    elif(ch==2):
        val=a.pop()
        print("value pop successfully=",val)
    elif(ch==3):
        print(a)

    
    
