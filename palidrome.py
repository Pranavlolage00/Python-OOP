n=int(input("enter number:"))
print("given number=",n)
rev=0
num=n
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n/10
    n=int(n)
if(rev==num):
    print("number is palindrome...",rev)
else:
    print("number is not palindrome..",rev)
    
    

