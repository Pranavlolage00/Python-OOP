a={"a":100,"b":200,"c":300}
b={"a":300,"b":200,"d":400}
print("dictionary one=",a)
print("dictionary two=",b)
c=dict([])
for key1 in a.keys():
    if key1 in b:
        c[key1]=a.get(key1)+b.get(key1)
    elif key1 not in b:
        c[key1]=a.get(key1)
        
for key2 in b.keys():
    if key2 not in c:
        c[key2]=b.get(key2)

print("Result=",c)
        
        
