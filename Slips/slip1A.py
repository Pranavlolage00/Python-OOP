# Write a Python program to accept n numbers in list and remove duplicates from a 
#list.
a=[]
n=int(input("Enter Limit :"))
for i in range(0,n):
    num=int(input("Enter Number:"))
    a.append(num)
print("Print Orignal List")
print(a)
a=set(a)
a=list(a)
print(a)
            
    
