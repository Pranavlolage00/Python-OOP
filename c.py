a={"a":100,"b":200,"c":300}
b={"a":500,"b":410,"d":784}
print(a)
print(b)
c=dict([])
for key1 in a.keys():
    if key1 in b:
        c[key1]=a.get(key1)+b.get(key1)

print(c)
        
