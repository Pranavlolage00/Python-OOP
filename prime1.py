n=int(input("enter number:"))
for i in range(2,n):
    if n%i==0:
      break
if(i==n-1):
    print("number is prime")
else:
    print("number is not prime")    
    
      
      
      
