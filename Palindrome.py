def pal(x):
    s=x
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    if i==s:
        return True
    else:
        return False
x=int(input())
r=pal(x)
print(r)