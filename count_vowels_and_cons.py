s1=input("enter string:")
c1=0
c2=0
print("input string is=",s1)
for ch in s1:
    if ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='U' or ch=='u':
        c1+=1
    else:
        c2+=1
        
print("vowels count=",c1)
print("consonant count=",c2)
