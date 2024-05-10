s1=input("enter string:")
print("input string=",s1)
c1=0
c2=0
v="AaEeIiOoUu"
for ch in s1:
    if ch in v:
        c1+=1
    else:
        c2+=1
print("vowels count=",c1)
print("consonant count=",c2)
