x=int(input())
a=0
b=1
while b<x:
    a,b=b,a+b
print(b==x)