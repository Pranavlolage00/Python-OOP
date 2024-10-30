#Write a Python program to accept n numbers in list and remove duplicates from a 
#list.

a=list()
n=int(input("Enter Limit:"))
print("Enter N Numbers in an List")
for i in range(n):
    num=int(input("enter Number:"))
    a.append(num)
a=set(a)
print(a)
            
    
