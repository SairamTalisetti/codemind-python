x=int(input())
a=0
b=1
c=0
print(a,b,end=" ")
while c<x-2:
    a,b=b,a+b
    c+=1
    print(b,end=" ")