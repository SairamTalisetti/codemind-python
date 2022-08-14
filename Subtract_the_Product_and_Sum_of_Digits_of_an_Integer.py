x=int(input())
s=0
p=1
while x>0:
    r=x%10
    x=x//10
    s+=r
    p*=r
print(p-s)