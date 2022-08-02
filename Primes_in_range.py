def prime(x):
    if x==1:
        return False
    for i in range(2,(int(x**0.5+1))):
        if x%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
c=0
for i in range(x,y+1):
    if prime(i)==True:
        c+=1
print(c)