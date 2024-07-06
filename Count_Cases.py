def Count(s1):
    u=0
    l=0
    for val in s1:
        if val>='A' and val<='Z':
            u+=1
        else:
            l+=1
    print("upercase Charecter=",u)
    print("Lowercase Charecter=",l)
    return
s1=input("Enter String:)
Count(s1)
