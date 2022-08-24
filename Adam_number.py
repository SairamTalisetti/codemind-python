def rev(x):
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i
x=int(input())
s=x*x
r=rev(x)
s1=r*r
print(s==rev(s1))