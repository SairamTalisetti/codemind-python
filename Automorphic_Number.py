a=int(input())
q=a
b=a*a
leng=0
while a>0:
    leng=leng+1
    a=a//10
d=b%10**leng
if d==q:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")