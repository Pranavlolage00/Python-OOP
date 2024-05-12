s1=input("enter string:")
for i in range(len(s1)):
    if(s1.count(s1[i])>=2):
        k=s1.count(s1[i]) 
        print(s1[i],k)

        
    
