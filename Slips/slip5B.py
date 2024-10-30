def show(n):
    f=0
    s=1
    for i in range(n+1):
        t=f+s
        f=s
        s=t
        yield t

n=int(input("Enter Limit:"))
print(0,end="")
print(1,end="")
for i in show(n):
    print(i,end="")


