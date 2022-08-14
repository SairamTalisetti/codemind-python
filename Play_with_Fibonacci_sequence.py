x=int(input())
a=0
b=1
print(a,b,end=" ")
while x>2:
    a,b=b,a+b
    print(b,end=" ")
    x-=1
