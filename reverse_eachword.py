str=input("enter String")
s1=str.split(" ")
print(s1)
for w in s1:
    print(w[::-1],end=" ")
