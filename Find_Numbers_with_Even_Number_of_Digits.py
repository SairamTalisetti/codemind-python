x=int(input())
l=list(map(int,input().split()))
e=[]
s=0
for i in l:
    s=str(i)
    if len(s)%2==0:
        e.append(i)
print(len(e))