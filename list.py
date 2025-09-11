a=[]
n=int(input("enter the numbere of elements to be included"))
for i in range(0,n):
    m=int(input("enter the number"))
    a.append(m)
print(a)
a.extend([2,3,4])
print(a)
