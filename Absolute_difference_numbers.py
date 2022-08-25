def rev(x):
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i
def le(x):
    y=0
    while x>0:
        x//=10
        y+=1
    return y
n,x=map(int,input().split())
r=le(n)
a=n%10**x
b=r-x
c=n//10**b
print(abs(a-c))
