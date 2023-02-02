n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
t=[]
for i in range(a,b+1):
    if i in l:
        l.remove(i)
if len(l)>0:
    print(max(l))
else:
    print(-1)