def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=input("Enter NUmber1 :")
b=input("Enter NUmber2 :")
c=input("Enter NUmber3 :")

print("Maximum Number of Three=",max(a,b,c))
