a=int(input())
re=0
neg=0
if a<0:
    a=-a
    neg=1
while a>0:
    b=a%10
    a=a//10
    re=re*10+b
if neg==0:
    print(re)
else:
    print(-re)
    