x=int(input())
l=list(map(int,input().split()))
y=int(input())
k=list(map(int,input().split()))
t=[]
for i in range(x):
    t.insert(k[i],l[i])
print(*t)