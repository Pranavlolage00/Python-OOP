def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if(s==n):
        print("number is perfect")
    else:
        print("Number is Not Perfect")
    return
n=int(input("Enter Number to Check"))
perfect(n)
