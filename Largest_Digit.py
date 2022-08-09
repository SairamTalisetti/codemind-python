x=int(input())
i=0
while x>0:
    r=x%10
    x=x//10
    if r>i:
        i=r
print(i)
        