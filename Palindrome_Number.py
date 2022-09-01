def pal(x):
    k=x
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    if i==k:
        return 1
    else:
        return 0
t=int(input())
for i in range(t):
    x=int(input())
    p=pal(x)
    if p==1:
        print(True)
    else:
        print(False)