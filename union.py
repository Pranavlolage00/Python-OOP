def union(s1,s2):
    s1=s1.split(" ")   
    s2=s2.split(" ")
    s1=set(s1)
    s2=set(s2)
    s1.update(s2)
    li=list([])
    for val in s1:
        li.append(val)
    print("union of two Strings=",li)
    return

def intersect(s1,s2):
    s1=s1.split(" ")
    s2=s2.split(" ")
    li=list([])
    for val in s1:
        if val in s2:
            li.append(val)
    print("intersection of two list=",li)
    return

s1=input("Enter String 1:")
s2=input("Enter String 2:")
union(s1,s2)
intersect(s1,s2)
