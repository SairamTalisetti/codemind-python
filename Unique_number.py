x=int(input())
s=x
lst=[]
k=0
while x!=0:
    r=x%10
    lst.append(r)
    x=x//10
while s!=0:
    e=s%10
    s=s//10
    if lst.count(e)==1:
        k+=1
    else:
        k-=1
if len(lst)==k:
    print("Unique Number")
else:
    print("Not Unique Number")