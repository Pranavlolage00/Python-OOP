n=int(input("enter limit:"))

for i in range(1,n):
    f=0
    num=i
    for j in range(2,num):
        if(num%j==0):
          f=1
          break
        if(f==0):
          print(j)


        
        
    
    
    
    

