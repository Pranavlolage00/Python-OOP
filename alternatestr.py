str=input("enter string:")
print("\nprint the alternate string charecters forword direction")
for i in range(0,len(str),2):
    print(str[i],end="")

print("\nprint the alternate string charecters backword direction")
for i in range(len(str)-1,0,-2):
    print(str[i],end="")

