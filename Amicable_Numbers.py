n=int(input())
m=int(input())
a=0
b=0
for i in range(1,(n//2)+1):
    if n%i==0:
        a=a+i
for i in range(1,(m//2)+1):
    if m%i==0:
        b=b+i
if n==b and m==a:
    print("Amicable")
else:
    print("Not Amicable")