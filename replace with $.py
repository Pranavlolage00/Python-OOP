s=input("enter string:")
s1=s[0]
print("print given string:",s)
for i in range(1,len(s)):
    if(s[i]==s[0]):
        s1=s1+'$'
    else:
        s1=s1+s[i]
print("RESULT=",s1)
